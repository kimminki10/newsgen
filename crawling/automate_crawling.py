import finviz, news_crawler, openAI
import chrome_driver


def automate_crawler():
    #finviz에서 리스트 긁어오기
    driver = chrome_driver.get_driver()
    lists = finviz.crawl(driver, "https://finviz.com/news.ashx?v=3")
    for list in lists[:3]: #테스트를 위해 3개만, 다하면 리소슷 많이써서 혼남
        # (ticker, link, title)
        ticker = list[0]
        url_link = list[1]
        e_title = list[2]
        # if link or title in db, do not crawl or send it to openAI  나중에 추가하기 일단 되는거 확인하자!
        crawled_data = news_crawler.crawler(driver, list[1])
        # title, time, article
        #crawl이 잘 됬으면, 
        print("===================================================================================================")
        print("===================================================================================================")
        print("===================================================================================================")
        if crawled_data is not None:
            #OpenAI에 요약 부탁하기
            title = crawled_data[0]
            time = crawled_data[1]
            article = crawled_data[2]
            ai_data = openAI.trans_summ_data(crawled_data[2])
            print(f'ticker: {list[0]}, link{list[1]}, t_title{list[2]}, ai_data{ai_data}')
            #해당 관련 정보를 API에 전송해서 article 및 티커 관련정보 저장
        else:
            #meaning crawled_data is none
            print(f'해당 링크는 crawl이 잘 되지 않음 {list[1]}')

if __name__ == "__main__":
    automate_crawler()