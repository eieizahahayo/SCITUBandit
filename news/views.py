from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import public,fund



def news_public(request):
    all_public = public.objects.all()
    return render(request, 'news/news_public.html',{'all_public':all_public})






def news_fund(request):
    all_fund = fund.objects.all()
    return render(request, 'news/news_fund.html',{'all_fund':all_fund})
