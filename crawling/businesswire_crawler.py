from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def crawl_businesswire_article(url):
    # Selectors
    title_selector = ".epi-fontLg.bwalignc"
    time_selector = ".bw-release-timestamp"
    article_selector = ".bw-release-body"

    # Initialize WebDriver
    options = webdriver.ChromeOptions()
    # Uncomment the line below if you want the browser to remain open after execution
    # options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        # Get title and time
        def get_text(selector):
            try:
                elem = driver.find_element(By.CSS_SELECTOR, selector)
                return elem.text
            except Exception as e:
                print(f"Error finding element with selector {selector}: {e}")
                return ""

        title = get_text(title_selector)
        time = get_text(time_selector)
        # Get article content
        article = get_text(article_selector)
        return title, time, article
    except Exception as e:
        print(f"An error occurred: {e}")
        return "", "", "Error occurred"
    finally:
        driver.quit()

# Example usage
if __name__ == "__main__":
    yahoo_url = "https://www.businesswire.com/news/home/20241212043058/en/"  # Replace with the actual Yahoo article URL
    title, time, article = crawl_businesswire_article(yahoo_url)
    print("Title:", title)
    print("Time:", time)
    print("Article:", article)
