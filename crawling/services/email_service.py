
from dotenv import load_dotenv  # .env 파일에서 환경 변수 불러오기
import smtplib  # 이메일 전송을 위한 라이브러리
from email.mime.text import MIMEText  # 이메일 내용 작성 라이브러리
import os  # 운영체제 관련 라이브러리
import ssl  # 보안 소켓 레이어(SSL) 사용
import socket  # 네트워크 주소 정보 설정 라이브러리

def send_email(receiver_email, subject, content):
    # 로컬 호스트에 대한 네트워크 주소 정보 설정 (특정 문제 해결용)
    socket.getaddrinfo('localhost', 8080)

    # 환경 변수 초기화 후, .env 파일 다시 불러오기 (override 옵션으로 덮어쓰기)
    os.environ.clear()
    load_dotenv(override=True)

    # 발신자 이메일과 비밀번호를 환경 변수에서 불러오기
    sender_email = os.environ.get('EMAIL_ADDRESS')  # 발신자 이메일 주소
    sender_password = os.environ.get('EMAIL_APP_PASSWORD')  # 발신자 이메일 앱 비밀번호

    # 이메일 내용 및 속성 설정
    html_message = MIMEText(content, 'html')  # 이메일 내용을 HTML 형식으로 설정
    html_message['Subject'] = subject  # 이메일 제목 설정
    html_message['From'] = sender_email  # 발신자 이메일 주소 설정
    html_message['To'] = receiver_email  # 수신자 이메일 주소 설정

    # Gmail SMTP 서버 설정
    smtp_server = "smtp.gmail.com"  # Gmail SMTP 서버 주소
    port = 587  # STARTTLS를 위한 포트 번호

    # SSL 보안 컨텍스트 생성
    context = ssl.create_default_context()

    # SMTP 서버에 로그인하고 이메일 전송
    try:
        server = smtplib.SMTP(smtp_server, port)  # SMTP 서버에 연결
        server.ehlo()  # SMTP 서버 확인 (생략 가능)
        server.starttls(context=context)  # STARTTLS로 연결을 보안화
        server.ehlo()  # SMTP 서버 확인 (생략 가능)
        server.login(sender_email, sender_password)  # 발신자 이메일 로그인
        server.sendmail(sender_email, receiver_email, html_message.as_string())  # 이메일 전송
    except Exception as e:
        # 오류 발생 시 오류 메시지 출력
        print(e)


if __name__ == "__main__":
    receiver_email = "gameking0301@gmail.com"
    subject = "TESING NEWS TITLE"
    content = """
            <!DOCTYPE html>
<html>
<head>
    <title>Simple HTML</title>
</head>
<body>
    <header>
        <h1>Header</h1>
    </header>
    <main>
        <section>
            <h2>Section</h2>
            <p>Paragraph</p>
        </section>
        <article>
            <h2>Article</h2>
            <p>Another Paragraph</p>
        </article>
    </main>
    <footer>
        <p>Footer</p>
    </footer>
</body>
</html>"""
    send_email(receiver_email, subject, content)