
from datetime import datetime, timedelta
import pytz
from crawling.services.email_service import send_email as se
from crawling.db_service_folder import db_services as ds
# 티커 위로 좀더 작게
# 구도해지 링크 달아주기
# 기사마다 아티클 뉴스
def daily_email():
    daily_news = []
    daily_news_html = ""
    #user다 가져와서
    users = ds.get_all_users()
    kst = pytz.timezone('Asia/Seoul')
    # Get current time in KST
    today = datetime.now(kst)
    yesterday = today - timedelta(days=1)
    print(today, yesterday)
    #TODO: remove [:1] later
    for user in users[:1]:#1 플고
        #유저마다 ticker 가져오고
            user_email = user['email']
            #티커 없을 때 처리도 해야함
            tickers = user['tickers']
            #해당 티커들 마다 오늘 기사 있는지 찾아보고 있으면 잘 약식정리
            tickers_articles = []
            for ticker in tickers:
                # 날짜는 이야기해보고 하자
                #오늘날짜랑 어제날짜 구해서 집어넣기 지금은 더미값
                #원하는 날짜의 해당 티커의 기사들만 가져옴
                ticker_articles = ds.get_articles_by_ticker_and_date(ticker, yesterday, today)
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
            print(f'EMAIL Sent to: {user_email} \n subject: {subject} \n content: {content}')
            se(user_email, subject, content)
            

def format_articles_html(articles):
    content_html = ""
    # Loop through each article and construct HTML
    for article in articles:
        tickers = ", ".join(article['tickers'])  # Convert tickers list to a string
        title = article['title']
        content = article['summary']
        
        # <div style="margin-top: 10px;">
        #                 {" ".join([f'<a href="https://finance.example.com/{ticker}" style="text-decoration: none; border: 1px solid #1b4d3e; color: #1b4d3e; padding: 5px 10px; border-radius: 5px; font-size: 12px; margin-right: 5px; display: inline-block;">{ticker}</a>' for ticker in article['tickers']])}
        #     </div>
        content_html += f"""
        <tr>
                        <td>
                        <div style="margin: 5px;">
                            {" ".join([f'<a href="https://finance.example.com/{ticker}" style="text-decoration: none; border: 2px solid #1b4d3e; color: #1a412c; padding: 4px 10px; border-radius: 5px; font-size: 11px; margin-right: 5px; display: inline-block;">{ticker}</a>' for ticker in article['tickers']])}
                        </div>
                        <h2 style="font-size: 18px; color: #f6f3f5; padding: 15px; background-color: #6f7074; text-align: center; margin-top: 0;">{title}​</h2>
                        <p style="font-size: 14px; color: #333; padding: 0 20px;">{content}​</p>
                        </td>
                    </tr>
                    <tr>
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
            style="width: 100%; margin: auto; padding: 20px;"
            >
            <tr >
                <td>
                <table
                    role="presentation"
                    cellpadding="0"
                    cellspacing="0"
                    style="
                    width: 100%;
                    max-width: 800px;
                    margin: 0 auto;
                    background-color: #f6f3ec;
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
                    <tr>
                        <!-- 주요지수 관련 지표 -->
                        <td style="text-align: center;">
                            <div style="border: 3px solid #1b4d3e; color: #1a412c; padding: 5px 20px; border-radius: 5px; font-size: 14px; margin: 10px; display: inline-block; font-weight: bold;">
                                주요 지수🐂
                            </div>
                        </td>
                    </tr>

                    <!-- 뉴스 콘텐츠 -->
                    {content_html}

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
                        메일을 더이상 원치 않으시면 마이페이지에서 구독 해지를 눌러 해지해 주세요.
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