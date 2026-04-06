from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from ..models import Article

class ArticlesListView(ListView):
    queryset = Article.objects.order_by("-pub_date")
    template_name = 'blog/home.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article.html'

