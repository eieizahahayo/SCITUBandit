from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from . models import meetingTable,report


def index(request):
    years = []
    all_meetingTable = meetingTable.objects.all()
    all_report = report.objects.all()
    return render(request, 'meeting/meeting.html', {'all_meetingTable':all_meetingTable,'all_report':all_report , 'all_years':all_years})
