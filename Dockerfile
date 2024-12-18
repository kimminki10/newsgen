# 베이스 이미지
FROM python:3.11.5-slim

# 작업 디렉토리 설정
WORKDIR /app

# pip 업데이트 및 의존성 설치
RUN apt-get update && apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip setuptools wheel

# requirements.txt 복사 및 설치
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사
COPY . .


# 마이그레이션 및 슈퍼유저 생성
# ...기존 코드...
# 직접 도커에 작성해야한다 Django 데이터 베이스 준비전에 호출해서 작동안되더라
# 이걸 하고 나서 슈퍼계정도 만들어야함
#RUN python manage.py makemigrations 
#RUN python manage.py migrate 


# 정적 파일 수집
RUN python manage.py collectstatic --noinput

# 기본 실행 명령
CMD ["gunicorn", "trandlator.wsgi:application", "--bind", "0.0.0.0:8000"]
