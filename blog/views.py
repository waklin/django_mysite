from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.utils import timezone

from blog.models import Article, Comment

def index(request):
    article_list = Article.objects.all().order_by('-pub_date')
    paginator = Paginator(article_list, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        article_list= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        article_list= paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        article_list= paginator.page(paginator.num_pages)

    x = 1
    pagenum_list=[]
    while x <= paginator.num_pages:
        pagenum_list.append(x)
        x += 1

    return render_to_response('blog/index.html', {"article_list": article_list, "pagenum_list": pagenum_list})

def detail(request, article_id):
    art = get_object_or_404(Article, pk=article_id)
    comment_list = art.comment_set.all().order_by('-pub_date')
    return render_to_response('blog/detail.html', {'article':art, 'comment_list':comment_list},
                                context_instance=RequestContext(request))

    

def comment_submit(request, article_id):
    art = get_object_or_404(Article, pk=article_id)
    comment = art.comment_set.create()
    comment.detail = request.POST['detail']
    comment.pub_date = timezone.now()
    comment.save()
    return HttpResponseRedirect(reverse('blog:detail', kwargs={'article_id': article_id}))

def bootstrap(request):
    return render(request, 'blog/bootstrap.html')

def bs_flow(request):
    return render(request, 'blog/bs_flow.html')
