from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def crawl_yahoo_article(url):
    # Selectors
    title_selector = "#nimbus-app > section > section > section > article > div > div.article-wrap.no-bb > div.cover-wrap.yf-1o1tx8g > h1"
    time_selector = "#nimbus-app > section > section > section > article > div > div.article-wrap.no-bb > div.byline.yf-1k5w6kz > div.byline-attr.yf-1k5w6kz > div > div.byline-attr-time-style > time"
    article_selector = "#nimbus-app > section > section > section > article > div > div.article-wrap.no-bb > div.body-wrap.yf-i23rhs"
    continue_button_selector = ".secondary-btn.fin-size-large.readmore-button.rounded.yf-15mk0m"
    continue_link_button_selector = ".secondary-btn.fin-size-large.continue-reading-button.rounded.rightAlign.yf-15mk0m"

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

        # Check for "Read More" button
        article_element = driver.find_element(By.CSS_SELECTOR, article_selector)
        read_more_buttons = article_element.find_elements(By.CSS_SELECTOR, continue_button_selector)
        if read_more_buttons:
            read_more_buttons[0].click()

        # Check for "Continue Reading" link
        new_link_element = article_element.find_elements(By.CSS_SELECTOR, continue_link_button_selector)
        if new_link_element:
            return "@", "@", "다른사이트로 넘어감"

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
    yahoo_url = "https://finance.yahoo.com/m/bc6187f2-0fb8-3446-b630-c0539fe957f6/back-trouble-and-brain-fog.html"  # Replace with the actual Yahoo article URL
    title, time, article = crawl_yahoo_article(yahoo_url)
    print("Title:", title)
    print("Time:", time)
    print("Article:", article)
