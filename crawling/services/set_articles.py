from crawling.db_service_folder.db_services import add_article, check_article_exists_by_url
from crawling import finviz
from crawling import chrome_driver
from crawling import news_crawler

from journalist.azure_api import AzureAPI
from journalist.prompts import prompts_dict

driver = None
def get_crawling_driver():
    global driver
    if driver is None:
        driver = chrome_driver.get_driver()
    return driver


def crawl_article_data():
    """
    crawl the news page of finviz
    return: [(ticker, link, title), ...]
    """
    article_lists = finviz.crawl(get_crawling_driver(), "https://finviz.com/news.ashx?v=3")
    return article_lists


def crawl_article(article):
    ticker, link, title = article
    if check_article_exists_by_url(link): return
    
    crawled_data = news_crawler.crawler(get_crawling_driver(), link)
    if crawled_data is None: 
        print(f'해당 링크는 crawl이 잘 되지 않음 {link}')
        return
    return crawled_data
    

def create_article(content):
    results = { 
        k: AzureAPI(k).get_response(content) 
        for k in prompts_dict.keys()
    }
    return results


def add_new_articles():
    article_lists = crawl_article_data()
    print(f'crawled article lists: {article_lists[:3]}')
    count = 0
    for article in article_lists:
        crawled_data = crawl_article(article)
        if crawled_data is None: continue
        title, time, content = crawled_data
        results = create_article(content)
        
        ticker = article[0]
        origin_url = article[1]
        title = results['title']
        short_content = results['short_content']
        long_content = results['long_content']
        tts_content = results['tts']
        add_article(title, short_content, long_content, tts_content, ticker, origin_url)
        count += 1
    return count
