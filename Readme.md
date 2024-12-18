# news

## backend

### How to start

```bash
##가상 환경
가상 환경 생성 : python -m venv venv , 
Window 가상 환경 실행 : venv\Scripts\activate
[Docker 실행을 위한 환경 설정]
Windows : Docker Desktop + wsl2 [바이오스 설정에서 가상환경 관련 설정 필요 ((VT-x or AMD-V) )  ]

# 서버 빌드 및 실행
docker-compose up --build

#OpenAI 및 Crawling 사용법
팀즈에서 env 파일을 다운받은 다음 해당 프로젝트 최상위 폴더에 넣고 .env로 이름 변경
후 가상 환경 실행후 python crawling/automate_crawling.py 작성

# DB 경로
/db.sqlite3

# DB 최초 세팅 <- Django container에서 실행
python manage.py makemigrations trandlator
python manage.py migrate  trandlator

```



