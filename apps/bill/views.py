#-*- coding: utf-8 -*-
# Create your views here.

from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect('/admin/')
