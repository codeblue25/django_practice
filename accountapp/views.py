from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_1ban(request):
    return HttpResponse('Hello 1반!')