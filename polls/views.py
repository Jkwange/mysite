from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("지금 시각 03:23<br>컴퓨터공학과 3학년은 오늘도 운다")
