from django.contrib import admin
from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'detail']

admin.site.register(Article, ArticleAdmin)
