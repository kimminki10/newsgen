# news

## backend

### How to start

```bash
##가상 환경
가상 환경 생성 : python -m venv venv
Window 가상 환경 실행 : venv\Scripts\activate
리눅스 가상환경 실행 : source venv/bin/activate

##필요한 라이브러리 설치
pip install -r requirements.txt

## 테스트 디비 설정
python manage.py makemigrations
python manage.py migrate

#서버 실행
python manage.py runserver

# DB 경로
/db.sqlite3

#OpenAI 및 Crawling 사용법
팀즈에서 env 파일을 다운받은 다음 해당 프로젝트 최상위 폴더에 넣고 .env로 이름 변경
후 가상 환경 실행후 python crawling/automate_crawling.py 작성

```



