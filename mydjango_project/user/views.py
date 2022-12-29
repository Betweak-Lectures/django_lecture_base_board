from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    my_profile = {
        "이름": "신윤수",
        "별명": "ys",
    }
    value = ""
    for k, v in my_profile.items():
        value += f"{k}: {value}<br/>"
    return HttpResponse(value)