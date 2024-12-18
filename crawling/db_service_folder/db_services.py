import os
import sys
import django
import random
from datetime import datetime
# Step 1: Add the project root to the Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(PROJECT_ROOT)

# Step 2: Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trandlator.settings')

# Step 3: Initialize Django
django.setup()

from trandlator.models import User, Article, Ticker
from trandlator.controller.UserSerialize import UserSerializer

def get_articles_by_ticker_and_date(ticker_name: str, start_date:datetime, end_date: datetime):
    ticker = Ticker.objects.get(ticker_name=ticker_name)
    articles = ticker.articles.filter(
        created_at__range=[start_date, end_date]  # 날짜 범위 필터링
    )
    article_list = [
        {
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "tickers": [ticker.ticker_name for ticker in article.tickers.all()],  # Include tickers
            "created_at": article.created_at,
            "updated_at": article.updated_at,
        }
        for article in articles
    ]
    return article_list

def get_all_users():#
    users = User.objects.prefetch_related('tickers').all()
    user_list = [
        {
            "email": user.email,
            "is_active": user.is_active,
            "is_superuser": user.is_superuser,
            "is_email_verified": user.is_email_verified,
            "tickers": [ticker.ticker_name for ticker in user.tickers.all()]
        }
        for user in users
    ]
    #serializer = UserSerializer(users, many=True)
    return user_list

def update_user(email, new_email):
    try:
        user = User.objects.get(email= email)
        user.email = new_email
        user.save()
    except User.DoesNotExist:
        return {"error": ""}

def get_all_articles():
    articles = Article.objects.all()
    article_list = [
        {
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "created_at": article.created_at,
            "updated_at": article.updated_at,
            "views": article.views,
            "origin_url": article.origin_url,
            "tickers": [ticker.ticker_name for ticker in article.tickers.all()]
        }
        for article in articles
    ]
    return article_list

def add_article(title, content, tickers, origin_url=""):
    new_article = Article.objects.create(
        title=title,
        content=content,
        origin_url=origin_url
    )
    # Add tickers to the article
    for ticker_name in tickers:
        ticker, _ = Ticker.objects.get_or_create(ticker_name=ticker_name)  # Create or get ticker
        new_article.tickers.add(ticker)  # Link ticker to article
    new_article.save()
    return {"id": new_article.id, "title": new_article.title, "tickers": [ticker.ticker_name for ticker in new_article.tickers.all()]}

def add_user(email, password, is_active=True, is_superuser=False, is_email_verified=False):
    user = User.objects.create_user(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_email_verified=is_email_verified
    )
    return {"id": user.id, "email": user.email}

# 5. Add Ticker
def add_ticker(ticker_name):
    ticker, created = Ticker.objects.get_or_create(ticker_name=ticker_name)
    return {"id": ticker.id, "ticker_name": ticker.ticker_name, "created": created}

# 6. Link Ticker to an Article
def link_ticker_to_article(ticker_name, article_id):
    try:
        ticker = Ticker.objects.get(ticker_name=ticker_name)
        article = Article.objects.get(id=article_id)
        ticker.articles.add(article)
        return {"message": f"Ticker '{ticker_name}' linked to Article ID {article_id}"}
    except Ticker.DoesNotExist:
        return {"error": f"Ticker '{ticker_name}' does not exist."}
    except Article.DoesNotExist:
        return {"error": f"Article with ID {article_id} does not exist."}

# 7. Link Ticker to a User
def link_ticker_to_user(ticker_name, user_email):
    try:
        ticker = Ticker.objects.get(ticker_name=ticker_name)
        user = User.objects.get(email=user_email)
        user.tickers.add(ticker)
        return {"message": f"Ticker '{ticker_name}' linked to User '{user_email}'"}
    except Ticker.DoesNotExist:
        return {"error": f"Ticker '{ticker_name}' does not exist."}
    except User.DoesNotExist:
        return {"error": f"User with email '{user_email}' does not exist."}

if __name__ == "__main__":
    # print("\n=== Final Articles ===")
    # print(get_all_articles())
    #print(get_articles_by_ticker_and_date("TSLA", datetime(2024, 12, 17), datetime(2024, 12, 18, 6, 0)))

    # print("\n=== Final Users ===")
    print(get_all_users())
    #update_user("user1@example.com", "johnwon2007@gmail.com")
    # print("=== Adding Users ===")
    # users = [
    #     {"email": "user1@example.com", "password": "password123"},
    #     {"email": "user2@example.com", "password": "password123"},
    #     {"email": "user3@example.com", "password": "password123"},
    # ]
    # for user in users:
    #     print(add_user(**user))

    # print("\n=== Adding Tickers ===")
    # tickers = ["AAPL", "TSLA", "AMZN", "GOOGL", "MSFT"]
    # for ticker_name in tickers:
    #     print(add_ticker(ticker_name))

    # print("\n=== Adding Articles ===")
    # articles = [
    #     {"title": "Apple vs Tesla", "content": "Apple stock reaches a record high.", "origin_url": "http://example.com/apple", "tickers": ["AAPL", "TSLA"]},
    #     {"title": "Tesla Supports Dogecoin", "content": "Tesla now accepts Dogecoin for payments.", "origin_url": "http://example.com/tesla", "tickers": ["TSLA"]},
    #     {"title": "Amazon Expands Globally", "content": "Amazon announces global expansion plans.", "origin_url": "http://example.com/amazon", "tickers": ["AMZN"]},
    #     {"title": "Google AI Innovations", "content": "Google introduces new AI features.", "origin_url": "http://example.com/google", "tickers": ["GOOGL"]},
    #     {"title": "Microsoft Cloud Growth", "content": "Microsoft Azure sees unprecedented growth.", "origin_url": "http://example.com/azure", "tickers": ["MSFT"]},
    # ]
    # article_ids = []  # To keep track of added articles
    # for article in articles:
    #     result = add_article(**article)
    #     print(result)
    #     article_ids.append(result["id"])

    # print("\n=== Linking Tickers to Users ===")
    # for i, ticker_name in enumerate(tickers):
    #     user_email = f"user{(i % len(users)) + 1}@example.com"  # Cycle through users
    #     print(link_ticker_to_user(ticker_name, user_email))