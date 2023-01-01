from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    my_profile = {
        "이름": "신윤수",
        "별명": "ys",
    }

    value = """<h1>나의 프로필</h1>"""
    value += "<ul>"
    for k, v in my_profile.items():
        value += f"<li>{k}: {v}</li>"
    value += "</ul>"
    return HttpResponse(value)
