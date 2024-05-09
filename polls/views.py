from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("영남대학교<br>3학년은 오늘도 운다")