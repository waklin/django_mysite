# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext

def index(request):    
    return render_to_response('login/index.html', context_instance=RequestContext(request))
