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

```
