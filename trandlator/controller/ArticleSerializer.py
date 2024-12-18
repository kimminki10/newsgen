from rest_framework import serializers
from trandlator.model.ArticleModel import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'