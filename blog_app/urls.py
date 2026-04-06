from django.urls import path
from .views import views

urlpatterns = [
    path('home/', views.ArticlesListView.as_view(), name='home'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article')
]