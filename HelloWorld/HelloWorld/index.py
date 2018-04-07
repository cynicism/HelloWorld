#encoding:utf-8

from django.shorcuts import render

def index(request):
    return render('index.html')