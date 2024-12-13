from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

url = "https://www.digitimes.com/news/a20241212PD223/apple-iphone-ultra-thin-design-foldable.html"
driver.get(url)

title_selector = "body > div.my-container > div.row > div.col-12.col-lg-8 > div.news-content-frame > div.main-title > h1"
time_selector = "body > div.my-container > div.row > div.col-12.col-lg-8 > div.news-content-frame > div.info > span.date > time"
article_selector = "#content > p"

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