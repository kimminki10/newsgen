from crawling.db_service_folder.db_services import add_article, check_article_exists_by_url, update_article_tts
from crawling import finviz
from crawling import chrome_driver
from crawling import news_crawler
from trandlator.automation.jobs_status import is_job_registered

from journalist.azure_api import AzureAPI
from journalist.prompts import prompts_dict
from journalist.announcer import request_tts
from crawling.services.upload_to_blob import upload_tts

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
    
def create_tts(content, id) -> str:
    path = request_tts(content, id)
    if path is "":
        return ""
    url = upload_tts(path, f"tts_audio{id}.mp3")
    return url


def create_article(content):
    results = { 
        k: AzureAPI(k).get_response(content) 
        for k in prompts_dict.keys()
    }
    return results


def add_new_articles(isAdmin=True):
    article_lists = crawl_article_data()
    print(f'crawled article lists: {article_lists[:3]}')
    count = 0
    for article in article_lists:
        if isAdmin == False and is_job_registered("scheduled_automate") == False:
            #스케줄러 강제 종료시 반목분 종료 코드
            print("Job already registered. scheduled_Article.")
            break
        
        try:
            crawled_data = crawl_article(article)
        except Exception as e:
            print(f"article Error : {e}")
            crawled_data = None
            continue

        

        if crawled_data is None: continue
        title, time, content = crawled_data

        try:
            results = create_article(content)
        except Exception as e:
            print(f"create article Error : {e}")
            results = None
            continue

        if results is None: continue

        ticker = article[0]
        origin_url = article[1]
        title = results['title']
        short_content = results['short_content']
        long_content = results['long_content']
        tts_content = results['tts']
        try:
            created_article = add_article(title, short_content, long_content, tts_content, ticker, origin_url)
            tts_url = create_tts(tts_content, f"tts{created_article.get("id")}")
            update_article_tts(tts_url=tts_url, article_id=created_article.get("id"))
        except Exception as e:
            print(f"add article Error : {e}")
            continue   
        count += 1
    return count
