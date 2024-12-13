from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

url = "https://qz.com/costco-q1-2025-earnings-retail-consumer-inflation-1851720096"
driver.get(url)

title_selector = "body > div:nth-child(5) > div.sc-101yw2y-7.fgAtaA > div.sc-157agsr-1.sc-157agsr-2.bDcOAo.ivPAJA > div.sc-9tztzq-3.iqvmIY > header > h1"
time_selector = "body > div:nth-child(5) > div.sc-101yw2y-7.fgAtaA > div.sc-157agsr-0.kQaSNa > main > div > div > div.sc-1fofo4n-0.dvJeFx > div > div.sc-83o472-0.ehisvA > div.sc-83o472-10.YLYps > div.sc-1jc3ukb-2.hHUrUU > time"
article_selector = "body > div:nth-child(5) > div.sc-101yw2y-7.fgAtaA > div.sc-157agsr-0.kQaSNa > main > div > div > div.js_regwalled-content > div > div > div.sc-xs32fe-0.hKyVvC.js_post-content > div"

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