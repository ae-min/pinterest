from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return HttpResponse('hello world!')
    # pinterest_account -> account_urls -> views_hello_world -> hello world! 출력하는 구조
    # http://127.0.0.1:8000/account/hello_world/ -> hello world! 출력
