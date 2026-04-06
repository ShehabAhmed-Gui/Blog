from django.contrib import admin
from blog_app.models import Article


class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)