from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from blog.models import Article, Comment
from blog import views

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^$',  
        ListView.as_view(
            queryset=Article.objects.all(),
            context_object_name='latest_article_list',
            template_name='blog/index.html'),
        name='index'),

    url(r'^(?P<pk>\d+)/comments/$',
        DetailView.as_view(
            model=Article,
            template_name='blog/comments.html'),
        name='comments'),

    url(r'^(?P<article_id>\d+)/comment_submit/$', 'blog.views.comment_submit',name='comment_submit'),
    url(r'^bootstrap/$','blog.views.bootstrap',name='bootstrap'),
    url(r'^bs_flow/$','blog.views.bs_flow',name='bs_flow'),
)
