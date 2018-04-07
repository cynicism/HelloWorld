#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return HttpResponse(u"test1234")

def views(request):
    return render(request, 'views.html')