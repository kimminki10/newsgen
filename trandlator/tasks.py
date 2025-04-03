from contextlib import contextmanager
from celery import shared_task

from trandlator.models import Article

from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List

from journalist.gemini_api import GeminiAPI

import pandas as pd
import requests
import io



@contextmanager
def get_browser():
    with sync_playwright() as p:
        iphone = p.devices['iPhone 13']
        browser = p.webkit.launch(headless=False)
        context = browser.new_context(**iphone)
        page = context.new_page()
        try:
            yield page
        finally:
            browser.close()


def get_nasdaq_tickers_with_yfinance():
    url = "https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt"
    response = requests.get(url)
    df = pd.read_csv(io.StringIO(response.text), sep="|")
    df = df.dropna()
    tickers = df['Symbol'].tolist()
    tickers = [ticker for ticker in tickers if not ticker.startswith('File ')]    
    return tickers


@dataclass
class NewsItem:
    title: str
    url: str
    tickers: List[str]
    source: str
    time_ago: str


def parse_news_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    news_items = []
    
    # Find all news rows
    news_rows = soup.find_all('tr', class_='news_table-row')
    
    for row in news_rows:
        # Extract time ago
        time_cell = row.find('td', class_='news_date-cell')
        time_ago = time_cell.text.strip() if time_cell else ""
        
        # Extract news link cell which contains title, url and tickers
        link_cell = row.find('td', class_='news_link-cell')
        if not link_cell:
            continue
        
        # Extract main news link (title and URL)
        news_link = link_cell.find('a', class_='nn-tab-link')
        if not news_link:
            continue
            
        title = news_link.text.strip()
        url = news_link.get('href', '')
        
        # Find source
        source_span = link_cell.find('span', class_='news_date-cell')
        source = source_span.text.strip() if source_span else ""
        
        # Extract all ticker symbols
        tickers = []
        ticker_links = link_cell.find_all('a', class_='fv-label')
        for ticker_link in ticker_links:
            ticker_span = ticker_link.find('span', class_='select-none')
            if ticker_span:
                tickers.append(ticker_span.text.strip())
        
        news_items.append(NewsItem(
            title=title,
            url=url,
            tickers=tickers,
            source=source,
            time_ago=time_ago
        ))
    
    return news_items


def parse_yahoo_article(url: str):
    with get_browser() as page:
        page.goto(url)
        title = page.query_selector(selector='.cover-title').inner_text()
        contents = page.query_selector_all('.body > .atoms-wrapper > p')
        contents += page.query_selector_all('.body > .read-more-wrapper > p')
        content = ''
        for c in contents:
            content += c.inner_text()
        return title, content
    return '', ''


def crawl_finviz() -> List[NewsItem]:
    with get_browser() as page:
        page.goto("https://finviz.com/news.ashx?v=3")
        page.wait_for_selector('.news_table-row')
        html_content = page.content()
        news_items = parse_news_html(html_content)
        # Print the parsed news items
        return news_items
    return []


@shared_task
def periodic_task():
    news_items = crawl_finviz()
    for news_item in news_items:
        if not news_item.url.startswith('https://finance.yahoo.com/'):
            continue

        if Article.objects.filter(origin_url=news_item.url).exists():
            continue

        title, content = parse_yahoo_article(news_item.url)

        Article.objects.create(
            title=GeminiAPI('title').get_response(title),
            content=GeminiAPI('long_content').get_response(content),
            summary=GeminiAPI('short_content').get_response(content),
            origin_url=news_item.url,
        )