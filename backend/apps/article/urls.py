from django.urls import path
from .views import ListCreateArticleView


urlpatterns = [
    path('', ListCreateArticleView.as_view()),
]
