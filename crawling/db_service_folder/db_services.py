
import os
import django
import random
from datetime import datetime
from django.db import transaction
# Step 1: Add the project root to the Python path
# export PYTHONPATH=$PYTHONPATH:/Users/johnwon/Desktop/Projects/project2/project2_github/newsgen
# Step 2: Set the Django settings module
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trandlator.settings')

# # Step 3: Initialize Django
# django.setup()

from trandlator.models import User, Article, Ticker
from trandlator.controller.TickerSerialize import TickerNoArticleSerializer, TickerNameSerializer
from trandlator.controller.ArticleSerializer import ArticleSerializer

# 로그 레벨을 WARNING으로 설정하여 디버그 로그 비활성화
# yfinance의 로거 비활성화



##################################################################################################################################
#Used in daily_email.py
##################################################################################################################################
def get_articles_by_ticker_and_date(ticker_name: str, start_date:datetime, end_date: datetime):
    ticker = Ticker.objects.get(ticker_name=ticker_name)
    articles = ticker.articles.prefetch_related('tickers').filter(
        created_at__range=[start_date, end_date]  # 날짜 범위 필터링
    )
    serializer = ArticleSerializer(articles, many=True)
    return serializer.data

##################################################################################################################################
#Used in auto crawling
##################################################################################################################################
def add_article(title: str, content: str, tickers: list, summary: str = 'empty summary',
                origin_url: str = '', tts_content: str = 'empty tts content', tts_url: str = ''):
    # Create the Article instance
    article = Article.objects.create(
        title=title,
        content=content,
        summary=summary,
        origin_url=origin_url,
        tts_content=tts_content,
        tts_url=tts_url
    )
    for ticker_name in tickers:
        ticker, created = Ticker.objects.get_or_create(ticker_name=ticker_name)
        article.tickers.add(ticker)
    return article

def update_article_tts(tts_url: str, article_id: int):
    print("update tts article_id: ", article_id)
    article = Article.objects.get(id=article_id)
    article.tts_url = tts_url
    article.save()

#Used in auto crawling
def check_article_exists_by_url(url: str) -> bool:
    return Article.objects.filter(origin_url=url).exists()

##################################################################################################################################
#Used in daily_stock_prices
##################################################################################################################################
def get_all_ticker_names():
    tickers = Ticker.objects.all()
    serializer = TickerNameSerializer(tickers, many=True)
    return [item['ticker_name'] for item in serializer.data]

def get_all_ticker():
    tickers = Ticker.objects.all()
    serializer = TickerNoArticleSerializer(tickers, many=True)
    return serializer.data

def update_ticker_prices(price_data: dict):
    """
    Updates ticker prices in the database based on the provided price data.

    :param price_data: Dictionary with ticker_name as keys and price info as values
    """
    # Fetch all tickers from the database
    tickers = Ticker.objects.filter(ticker_name__in=price_data.keys())

    tickers_to_update = []

    for ticker in tickers:
        ticker_name = ticker.ticker_name
        if ticker_name in price_data:
            data = price_data[ticker_name]
            # Update the ticker object
            ticker.before_last_price = data["before_last_price"]
            ticker.last_price = data["last_price"]
            ticker.price_diff = data["price_difference"]
            ticker.percentage_diff = data["percentage_difference"]
            ticker.last_price_date = data["last_price_date"]
            ticker.before_last_date = data["before_last_price_date"]
            tickers_to_update.append(ticker)
    # Bulk update the database
    if tickers_to_update:
        Ticker.objects.bulk_update(
            tickers_to_update,
            ["last_price", "before_last_price", "price_diff",
             "percentage_diff", "last_price_date", "before_last_date"]
        )
        print(f"Updated {len(tickers_to_update)} tickers successfully.")
    else:
        print("No tickers were updated.")

def get_all_articles():
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return serializer.data

def add_tickers_to_db(price_data):
    """
    Adds tickers to the database with detailed price information.

    :param price_data: Dictionary with ticker_name as keys and price details as values.
    :return: Summary dictionary with counts of added tickers.
    """
    # Extract ticker names from the price_data keys

    try:
        ticker_names = price_data.keys()

        # Prepare Ticker objects for bulk creation
        ticker_objects = []
        for name, data in price_data.items():
            ticker = Ticker.objects.get_or_create(ticker_name=name)[0]
            ticker.last_price = data["last_price"]
            ticker.before_last_price = data["before_last_price"]
            ticker.price_diff = data["price_difference"]
            ticker.percentage_diff = data["percentage_difference"]
            ticker.last_price_date = data["last_price_date"]
            ticker.before_last_date = data["before_last_price_date"]
            ticker.save()
            ticker_objects.append(ticker)

        # Bulk insert the new tickers into the database
        # batch_size = 10
        # for i in range(0, len(ticker_objects), batch_size):
        #     with transaction.atomic():
        #         Ticker.objects.bulk_create(ticker_objects[i:i + batch_size])

        # Return a summary
        return {
            "added": len(ticker_objects)
        }
    except Exception as e:
        return {
            "error": str(e)
        }
#ORM VERSION
# def get_articles_by_ticker_and_date(ticker_name: str, start_date:datetime, end_date: datetime):
#     ticker = Ticker.objects.get(ticker_name=ticker_name)
#     articles = ticker.articles.filter(
#         created_at__range=[start_date, end_date]  # 날짜 범위 필터링
#     )
#     article_list = [
#         {
#             "id": article.id,
#             "title": article.title,
#             "content": article.content,
#             "tickers": [ticker.ticker_name for ticker in article.tickers.all()],  # Include tickers
#             "created_at": article.created_at,
#             "updated_at": article.updated_at,
#         }
#         for article in articles
#     ]
#     return article_list

def get_all_users():
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

# def get_all_articles():
#     articles = Article.objects.all()
#     article_list = [
#         {
#             "id": article.id,
#             "title": article.title,
#             "content": article.content,
#             "created_at": article.created_at,
#             "updated_at": article.updated_at,
#             "views": article.views,
#             "origin_url": article.origin_url,
#             "tickers": [ticker.ticker_name for ticker in article.tickers.all()]
#         }
#         for article in articles
#     ]
#     return article_list

def add_article(title, short_content, long_content, tts_content, tickers, origin_url=""):
    new_article = Article.objects.create(
        title=title,
        summary=short_content,
        content=long_content,
        tts_content=tts_content,
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
    #print(get_all_articles())
    print(len(get_all_ticker()))
    #print(add_tickers_to_db(['NVDA']))
    #print(get_all_ticker_names())
    #print(get_all_ticker())
    # print(get_articles_by_ticker_and_date("TSLA", datetime(2024, 12, 17), datetime(2024, 12, 18, 6, 0)))
    # print(get_articles_by_ticker_and_date("TSLA", datetime(2024, 12, 17), datetime(2024, 12, 20, 6, 0)))
    # print("\n=== Final Users ===")
    # print(get_all_users())
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