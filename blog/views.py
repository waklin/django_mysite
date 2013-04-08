from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
from django.core.urlresolvers import reverse
from blog.models import Article, Comment

def comment_submit(request, article_id):
    #return HttpResponse("you are looking at comment_submit")
    art = get_object_or_404(Article, pk=article_id);
    comment = art.comment_set.create()
    comment.detail = request.POST['detail']
    comment.save()
    return HttpResponseRedirect(reverse('blog:comments', kwargs={'pk':article_id}))
