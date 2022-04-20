from django.urls import path
from .views import *

urlpatterns = [
    path('article/all/', ArticleListView.as_view()),
    path('article/privat/', ArticlePrivatListView.as_view()),
    path('article/create/', ArticleCreateView.as_view()),
    path('article/detail/<int:pk>/', ArticleDetailView.as_view()),
    path('auth/registr/', RegisterUserView.as_view()),
]