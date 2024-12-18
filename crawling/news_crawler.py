from .chrome_driver import get_driver
from . import yahoo_crawler, basic_crawler


def crawler(driver, url: str):
    if url.startswith("https://finance.yahoo.com/"):
        print("Crawling yahoo")
        crawler, title, time, article = yahoo_crawler.crawl_yahoo_article(driver, url)
    elif url.startswith("https://qz.com/"):
        title_selector = "body > div:nth-child(5) > div.sc-101yw2y-7.fgAtaA > div.sc-157agsr-1.sc-157agsr-2.bDcOAo.ivPAJA > div.sc-9tztzq-3.iqvmIY > header > h1"
        time_selector = "body > div:nth-child(5) > div.sc-101yw2y-7.fgAtaA > div.sc-157agsr-0.kQaSNa > main > div > div > div.sc-1fofo4n-0.dvJeFx > div > div.sc-83o472-0.ehisvA > div.sc-83o472-10.YLYps > div.sc-1jc3ukb-2.hHUrUU > time"
        article_selector = "body > div:nth-child(5) > div.sc-101yw2y-7.fgAtaA > div.sc-157agsr-0.kQaSNa > main > div > div > div.js_regwalled-content > div > div > div.sc-xs32fe-0.hKyVvC.js_post-content > div"
        crawler, title, time, article = basic_crawler.crawler(driver, url, title_selector, time_selector, article_selector)
    elif url.startswith("https://www.prnewswire.com/"):
        title_selector = "#main > article > header > div > div:nth-child(1) > div > div > div.col-sm-8.col-vcenter.col-xs-12 > h1"
        time_selector = "#main > article > header > div > div:nth-child(4) > div.col-lg-8.col-md-8.col-sm-7.swaping-class-left > p"
        article_selector = "#main > article > section > div > div"
        crawler, title, time, article = basic_crawler.crawler(driver, url, title_selector, time_selector, article_selector)
    elif url.startswith("https://www.globenewswire.com/"):
        title_selector = "#container-article > div.main-container-content > div.main-header-container > h1"
        time_selector = "#container-article > div.main-container-content > div.main-header-container > p > span.d-flex.justify-content-start > span.article-published > time"
        article_selector = "#main-body-container"
        crawler, title, time, article = basic_crawler.crawler(driver, url, title_selector, time_selector, article_selector)
    elif url.startswith("https://www.digitimes.com/"):
        title_selector = "body > div.my-container > div.row > div.col-12.col-lg-8 > div.news-content-frame > div.main-title > h1"
        time_selector = "body > div.my-container > div.row > div.col-12.col-lg-8 > div.news-content-frame > div.info > span.date > time"
        article_selector = "#content > p"
        crawler, title, time, article = basic_crawler.crawler(driver, url, title_selector, time_selector, article_selector)
    elif url.startswith("https://www.businesswire.com/"):
        title_selector = ".epi-fontLg.bwalignc"
        time_selector = ".bw-release-timestamp"
        article_selector = ".bw-release-body"
        crawler, title, time, article = basic_crawler.crawler(driver, url, title_selector, time_selector, article_selector)
    else:
        print("해당 url을 crawling 하는 기능은 아직 구현되지 않음")
        return None
    if crawler:
        #print(title, time, article)
        return title, time, article
    print(crawler, title)
    return None
        
# if __name__ == "__main__":
#     driver = get_driver()
#     print(crawler(driver, "https://finance.yahoo.com/news/private-equity-making-big-money-050026774.html"))
