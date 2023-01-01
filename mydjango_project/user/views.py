from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    print(request.user)
    print(type(request.user))

    print(type(request.session))
    for k, v in request.session.items():
        print(k, v)
    print(dir(request.user))

    return render(request, 'user/profile.html')
