from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

url = "https://www.globenewswire.com/news-release/2024/12/12/2996582/32716/en/BioAge-Labs-BIOA-Azelaprag-Trial-Halt-Raises-Questions-About-Pre-IPO-Disclosures-Hagens-Berman.html"
driver.get(url)

title_selector = "#container-article > div.main-container-content > div.main-header-container > h1"
time_selector = "#container-article > div.main-container-content > div.main-header-container > p > span.d-flex.justify-content-start > span.article-published > time"
article_selector = "#main-body-container"

def get_text(selector):
    elem = driver.find_element(By.CSS_SELECTOR, selector)
    return elem.text


def crawl(url):
    driver.get(url)
    title = get_text(title_selector)
    time = get_text(time_selector)
    article = get_text(article_selector)
    return title, time, article



if __name__ == "__main__":
    title, time, article = crawl(url)
    print(title)
    print(time)
    print(article)
    driver.quit()