from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from blog.models import Article, Comment
from blog import views

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),

    url(r'^(?P<article_id>\d+)/$', 'blog.views.detail', name='detail'),

    url(r'^(?P<pk>\d+)/comments/$',
        DetailView.as_view(
            model=Article,
            template_name='blog/comments.html'),
        name='comments'),

    url(r'^(?P<article_id>\d+)/comment_submit/$', 'blog.views.comment_submit', name='comment_submit'),
    url(r'^ajax/(?P<article_id>\d+)/$', 'blog.views.ajax', name='ajax'),
    
    #url(r'^bootstrap/$','blog.views.bootstrap',name='bootstrap'),
    #url(r'^bs_flow/$','blog.views.bs_flow',name='bs_flow'),
)
