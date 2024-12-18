
from datetime import datetime
from email_service import send_email as se
import os, sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(PROJECT_ROOT)
from db_service_folder import db_services as ds

def daily_email():
    daily_news = []
    daily_news_html = ""
    #user다 가져와서
    users = ds.get_all_users()
    #TODO: remove [:1] later
    for user in users[:1]:
        #유저마다 ticker 가져오고
            user_email = user['email']
            #티커 없을 때 처리도 해야함
            tickers = user['tickers']
            #해당 티커들 마다 오늘 기사 있는지 찾아보고 있으면 잘 약식정리
            tickers_articles = []
            for ticker in tickers:
                #오늘날짜랑 어제날짜 구해서 집어넣기 지금은 더미값
                #원하는 날짜의 해당 티커의 기사들만 가져옴
                ticker_articles = ds.get_articles_by_ticker_and_date(ticker, datetime(2024, 12, 18), datetime(2024, 12, 19))
                #기사 전체에 추가
                tickers_articles.extend(ticker_articles)
            
            #보낼 기사가 하나라도 있으면,
            subject = "오늘의 뉴스!!!"
            if tickers_articles:
                 content = format_articles_html(tickers_articles)
            #ticker가 없거나, 해당 티커의 기사가 없으면 유용한 제일 최근 기사 걍 보내버리기
            #이미 만들어 놓은 오늘의 기사가 있으면,
            elif daily_news:
                content = daily_news_html
            #오늘의 기사가 없으면
            else:
                # 가장 최근 저장된 기사 5개 보내버리기~
                articles = ds.get_all_articles()
                daily_news_html = format_articles_html(articles[:5])
                content = daily_news_html
            # 이메일 보내는 기능
            print(f'Sent to: {user_email} \n subject: {subject} \n content: {content}')
            #se(user_email, subject, content)
            
                
                     
            

def format_articles_html(articles):
    html_output = ""
    # Loop through each article and construct HTML
    for article in articles:
        tickers = ", ".join(article['tickers'])  # Convert tickers list to a string
        title = article['title']
        content = article['content']
        
        # Add HTML for this article
        html_output += f"""
        <div>
            <h3>Tickers: {tickers}</h3>
            <h2>{title}</h2>
            <p>{content}</p>
        </div>
        """
    # Print the HTML output
    return html_output

if __name__ == "__main__":
     daily_email()