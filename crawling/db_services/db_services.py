import os
import sys
import django

# # Step 1: Add the project root to the Python path
# PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
# sys.path.append(PROJECT_ROOT)

# # Step 2: Set the Django settings module
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trandlator.settings')

# # Step 3: Initialize Django
# django.setup()

from trandlator.models import User, Article, Ticker

def get_all_users():
    users = User.objects.all()
    user_list = [
        {
            "email": user.email,
            "username": user.username,
            "is_active": user.is_active,
            "is_superuser": user.is_superuser,
            "is_email_verified": user.is_email_verified,
        }
        for user in users
    ]
    return user_list


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
        }
        for article in articles
    ]
    return article_list

def add_article(title, content, origin_url=""):
    new_article = Article.objects.create(
        title=title,
        content=content,
        origin_url=origin_url
    )
    new_article.save()
    return {"id": new_article.id, "title": new_article.title}

def add_user(email, username, password, is_active=True, is_superuser=False, is_email_verified=False):
    user = User.objects.create_user(
        email=email,
        password=password,
        username=username,
        is_active=is_active,
        is_superuser=is_superuser,
        is_email_verified=is_email_verified
    )
    return {"id": user.id, "email": user.email, "username": user.username}

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
    #add_article("테슬라기사", "텍슬라는 도지코인투더문을 지지함함")
    print(get_all_articles())