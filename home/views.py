from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from news.models import public,fund


def index(request):
    all_public = public.objects.all()
    all_fund = fund.objects.all()
    return render(request, 'home/home.html',{'all_fund': all_fund, 'all_public':all_public})
