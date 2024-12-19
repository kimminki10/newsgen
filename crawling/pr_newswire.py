from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

url = "https://www.prnewswire.com/news-releases/lument-finance-trust-inc-declares-quarterly-cash-dividends-for-its-common-and-preferred-stock-and-announces-special-cash-dividend-distribution-302330846.html"
driver.get(url)
#main > article > header > div > div:nth-child(1) > div > div > div.col-sm-8.col-vcenter.col-xs-12 > h1
title_selector = "#main > article > header > div > div:nth-child(1) > div > div.row.detail-headline > div > h1"
time_selector = "#main > article > header > div > div:nth-child(4) > div.col-lg-8.col-md-8.col-sm-7.swaping-class-left > p"
article_selector = "#main > article > header > div > div:nth-child(4) > div.col-lg-8.col-md-8.col-sm-7.swaping-class-left > a > strong"
content_selector = "#main > article > section.release-body.container  > div > div > p"
def get_text(selector):
    elem = driver.find_element(By.CSS_SELECTOR, selector)
    return elem.text
def get_contents(selector):
    elems = driver.find_elements(By.CSS_SELECTOR, selector)
    result = ""
    for elem in elems:
        result += elem.text + "\n"
    return  result

def crawl(url):
    driver.get(url)
    title = get_text(title_selector)
    time = get_text(time_selector)
    article = get_text(article_selector)
    contents = get_contents(content_selector)
    return title,time, article,contents



