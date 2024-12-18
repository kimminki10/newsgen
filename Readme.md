# news

## backend

### How to start

```bash
##가상 환경
가상 환경 생성 : python -m venv venv , 
Window 가상 환경 실행 : venv\Scripts\activate

##필요한 라이브러리 설치
pip install -r requirements.txt

#서버 실행
python manage.py runserver

# DB 최초 세팅
python manage.py makemigrations trandlator
python manage.py migrate  trandlator  


# DB 경로
/db.sqlite3

#OpenAI 및 Crawling 사용법
팀즈에서 env 파일을 다운받은 다음 해당 프로젝트 최상위 폴더에 넣고 .env로 이름 변경
후 가상 환경 실행후 python crawling/automate_crawling.py 작성


#Nginx -> admin 페이지 관련 안떠서 프록시 서버둠
#Django -> 서버 사이드 스크립트
#주기적으로 실핸되는 기능 제공 Celery
#Docker 사용

#OpenAI 3분마다 호출 등록 windows 에서 prefork  지원하지 않아 solo로
docker-compose up --build

django 서버 포트 80번 
관리자 계정 
admin 
1234

```



