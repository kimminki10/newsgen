from chrome_driver import get_driver
from selenium.webdriver.common.by import By


tbody_cell_selector = "td.news_link-cell > div"
link_selector = "a.nn-tab-link"
ticker_selector = "a.fv-label.stock-news-label > span"
def get_text(driver, selector):
    elem = driver.find_element(By.CSS_SELECTOR, selector)
    return elem.text

def crawl(driver, url):
    """
    crawl the news page of finviz
    return: [(ticker, link, title), ...]
    """
    result = []
    driver.get(url)
    tbody_cells = driver.find_elements(By.CSS_SELECTOR, tbody_cell_selector)
    for cell in tbody_cells:
        ticker_elements = cell.find_elements(By.CSS_SELECTOR, ticker_selector)
        link_cell = cell.find_element(By.CSS_SELECTOR, link_selector)
        link = link_cell.get_attribute("href")
        title = link_cell.text
        ticker = []
        for ticker_element in ticker_elements:
            ticker.append(ticker_element.text)
        result.append((ticker, link, title))
    return result

# if __name__ == "__main__":
#     driver = get_driver()
#     url = "https://finviz.com/news.ashx?v=3"
#     rows = crawl(driver, url)
#     for row in rows:
#         print(row)