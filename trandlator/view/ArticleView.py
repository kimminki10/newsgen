from rest_framework.generics import ListCreateAPIView
from trandlator.controller.ArticleSerializer import ArticleSerializer
from rest_framework.permissions import IsAuthenticated
from trandlator.models import Article

class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능
