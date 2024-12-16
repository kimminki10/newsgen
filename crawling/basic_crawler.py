import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By

def get_text(driver, selector):
    elem = driver.find_element(By.CSS_SELECTOR, selector)
    return elem.text

def crawler(driver: selenium.webdriver, url: str, title_selector: str, time_selector: str, article_selector: str):
    driver.get(url)
    title = get_text(driver, title_selector)
    time = get_text(driver, time_selector)
    article = get_text(driver, article_selector)
    return title, time, article