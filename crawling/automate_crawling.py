from . import finviz, news_crawler, openAI
from .chrome_driver import get_driver
from .db_service_folder.db_services import add_article, check_article_exists_by_url
from trandlator.automation.jobs_status import is_job_registered,job_id

driver = None

def automate_crawler():
        global job_id
        # finviz에서 리스트 긁어오기
        driver = get_driver()
        print("------- 크롤링 시작 -------")
        
        
        lists = finviz.crawl(driver, "https://finviz.com/news.ashx?v=3")
        crawlings = []

        if is_job_registered(job_id) == False:
                    print("Job already registered. Skipping registration.")
                    return
        

        print("------- 개별 기사 크롤링 시작 -------")
        for list in lists[:3]:  # 테스트를 위해 3개만, 다하면 리소스 많이 써서 혼남
            try:
               
                # (ticker, link, title)
                ticker = list[0]
                url_link = list[1]
                e_title = list[2]
                # if link or title in db, do not crawl or send it to openAI  나중에 추가하기 일단 되는거 확인하자!
                if is_job_registered(job_id) == False:
                    print("Job already registered. Skipping registration.")
                    return
                
                crawled_data = news_crawler.crawler(driver, list[1])

               
                # title, time, article
                # crawl이 잘 됬으면,
                print("===================================================================================================")
             
                if crawled_data is not None:
                    # OpenAI에 요약 부탁하기
                    title = crawled_data[0]
                    time = crawled_data[1]
                    article = crawled_data[2]
                    crawlings.append((ticker,title,article,url_link))
                    # ai_data = openAI.trans_summ_data(crawled_data[2])
                    # print(f'ticker: {list[0]}, link{list[1]}, t_title{list[2]}')
                    # print(f'ticker: {list[0]}, link{list[1]}, t_title{list[2]}, ai_data{ai_data}')
                    print("Success")
                    # 해당 관련 정보를 API에 전송해서 article 및 티커 관련정보 저장
                else:
                    # meaning crawled_data is none
                    print(f'해당 링크는 crawl이 잘 되지 않음 {list[1]}')
            except Exception as e:
                print(f'Exception: {e}')
        print("------- 크롤링 완료 -------")
        driver.quit()

        if is_job_registered(job_id) == False:
                    print("Job already registered. Skipping registration.")
                    return
        
        for (ticker,title,ori_content,url_link) in crawlings:
          
            
            isSuccess,ai_data = openAI.trans_summ_data(ori_content)
            if isSuccess == False:
                 continue
            
            if is_job_registered(job_id) == False:
                print("Job already registered. Skipping registration.")
                return
            if check_article_exists_by_url(url_link) == True:
                print(f"--- Ai Exist ---")
                continue

            print(f"--- Ai Success --- {ticker}")    
    
            add_article(title=ai_data['k_title'],content=ai_data['k_article'],tickers=ticker,origin_url=url_link)
            #ai_data['k_summary']
            
        print("------- AI 완료 -------")
       
            
