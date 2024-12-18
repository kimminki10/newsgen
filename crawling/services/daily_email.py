
from datetime import datetime
from email_service import send_email as se

from crawling.db_service_folder import db_services as ds

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
                ticker_articles = ds.get_articles_by_ticker_and_date(ticker, datetime(2024, 12, 17), datetime(2024, 12, 20))
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
            #print(f'Sent to: {user_email} \n subject: {subject} \n content: {content}')
            se(user_email, subject, content)
            

def format_articles_html(articles):
    html_output = ""
    # Loop through each article and construct HTML
    for article in articles:
        tickers = ", ".join(article['tickers'])  # Convert tickers list to a string
        title = article['title']
        content = article['summary']
        
        # Add HTML for this article
        # html_output += f"""
        # <div>
        #     <h3>Tickers: {tickers}</h3>
        #     <h2>{title}</h2>
        #     <p>{content}</p>
        # </div>
        # """
        
        html_output += f"""
        <tr>
            <td style="padding: 20px;">
            <div style="padding: 0;">
            <h2 style="font-size: 18px; color: #1b4d3e;">{title}</h2>
            <p style="font-size: 14px; color: #333;">{content}</p>
            <div style="margin-top: 10px;">
                        {" ".join([f'<a href="https://finance.example.com/{ticker}" style="text-decoration: none; border: 1px solid #1b4d3e; color: #1b4d3e; padding: 5px 10px; border-radius: 5px; font-size: 12px; margin-right: 5px; display: inline-block;">{ticker}</a>' for ticker in article['tickers']])}
            </div>
            </div>
            </td>
        </tr>
        """
    basic_html_template  = f"""<!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>핀트렌드 뉴스레터</title>
        </head>
        <body
            style="
            margin: 0;
            padding: 0;
            background-color: #f6f6f6;
            font-family: Arial, sans-serif;
            "
        >
            <table
            role="presentation"
            cellpadding="0"
            cellspacing="0"
            style="width: 100%; margin: auto; padding: 20px"
            >
            <tr>
                <td>
                <table
                    role="presentation"
                    cellpadding="0"
                    cellspacing="0"
                    style="
                    width: 100%;
                    max-width: 800px;
                    margin: 0 auto;
                    background: white;
                    "
                >
                    <!-- 헤더 -->
                    <tr>
                    <td
                        style="
                        background-color: #1b4d3e;
                        padding: 20px;
                        text-align: center;
                        "
                    >
                        <h1 style="color: white; margin: 0; font-size: 24px">
                        🔥 핀트렌드 뉴스레터 🔥
                        </h1>
                        <p style="color: white; margin: 10px 0 0 0">
                        새로운 미국 주식시장 소식을 전달해 드릴께요! 📰
                        </p>
                    </td>
                    </tr>

                    <!-- 뉴스 콘텐츠 -->
                    <!-- <tr>
                    <td style="padding: 20px">{{newsContent}}</td>
                    </tr> -->
                    {html_output}

                    <!-- 푸터 -->
                    <tr>
                    <td
                        style="
                        background-color: #333;
                        color: white;
                        padding: 20px;
                        text-align: center;
                        "
                    >
                        <p style="margin: 0; font-size: 14px">
                        본 메일은 핀트렌드 메일 수신을 신청하신 분들에게만 발송
                        되었습니다.<br />
                        메일을 더이상 원치 않으시면 사이트에서 구독 해지를 눌러 해지해 주세요.
                        <!-- <a href="{{unsubscribeLink}}" style="color: white"
                            >구독 해지</a
                        >를 눌러 해지해 주세요. -->
                        </p>
                        <p style="margin: 10px 0 0 0; font-size: 12px">
                        Fintrend.com<br />
                        COPYRIGHT © 2024 Fintrend. ALL RIGHTS RESERVED
                        </p>
                    </td>
                    </tr>
                </table>
                </td>
            </tr>
            </table>
        </body>
        </html>
        """
    # Print the HTML output
    return basic_html_template

if __name__ == "__main__":
     daily_email()