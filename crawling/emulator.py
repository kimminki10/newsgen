from playwright.sync_api import sync_playwright, Playwright

def get_context(playwright: Playwright):
    iphone_13 = playwright.devices['iPhone 13']
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_13,
    )
    return context

def open_page(context, url):
    page = context.new_page()
    page.goto(url)
    return page

def search_selector(page, selector):
    elem = page.query_selector(selector)
    return elem

if __name__ == "__main__":
    with sync_playwright() as playwright:
        url = "https://www.accesswire.com/954208/loop-industries-completes-convertible-preferred-financing-with-reed-societe-generale-group-and-sells-first-technology-license-for-an-infinite-loop-manufacturing-facility-in-europe"
        title_selector = "#articleHeading"
        article_selector = "#articleBody"

        context = get_context(playwright)
        page = open_page(context, url)
        title_elem = search_selector(page, title_selector)
        article_elem = search_selector(page, article_selector)
        print(title_elem.text_content())
        print(article_elem.text_content())



