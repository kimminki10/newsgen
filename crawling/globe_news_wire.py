from selenium import webdriver
from selenium.webdriver.common.by import By
from .chrome_driver import get_driver

title_selector = "#container-article > div.main-container-content > div.main-header-container > h1"
time_selector = "#container-article > div.main-container-content > div.main-header-container > p > span.d-flex.justify-content-start > span.article-published > time"
article_selector = "#main-body-container"

def get_text(driver, selector):
    elem = driver.find_element(By.CSS_SELECTOR, selector)
    return elem.text


def crawl(driver, url):
    driver.get(url)
    title = get_text(driver, title_selector)
    time = get_text(driver, time_selector)
    article = get_text(driver, article_selector)
    return title, time, article



