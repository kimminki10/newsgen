from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import CursorPagination
from .models import Article
from .serializer import ArticleSerializer

class ArticleCursorPagination(CursorPagination):
    page_size = 10
    ordering = 'created_at'  # 정렬 기준 필드

class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleCursorPagination
    #permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

