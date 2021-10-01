from django.db.models import query
from rest_framework import generics

from .serializers import ArticleSerializer
from .models import Article


class ListCreateArticleView(generics.ListCreateAPIView):
    queryset = Article.objects.all() 
    serializer_class = ArticleSerializer 
