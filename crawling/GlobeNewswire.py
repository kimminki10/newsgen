from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

url = "https://www.globenewswire.com/news-release/2024/12/13/2996591/0/en/Mountain-Lake-Acquisition-Corp-Announces-the-Pricing-of-Upsized-210-000-000-Initial-Public-Offering.html"
driver.get(url)

title_selector = "#container-article > div.main-container-content > div.main-header-container > h1"
time_selector = "#container-article > div.main-container-content > div.main-header-container > p > span.d-flex.justify-content-start > span.article-published"
article_selector = "#container-article > div.main-container-content > div.main-scroll-container"

def get_text(selector):
    elem = driver.find_element(By.CSS_SELECTOR, selector)
    return elem.text


def crawl(url):
    driver.get(url)
    title = get_text(title_selector)
    time = get_text(time_selector)
    article = get_text(article_selector)
    return title, time, article

