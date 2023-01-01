from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.utils import timezone

from .forms import RegisterForm


def index(request):
    response = render(request, 'user/profile.html', )
    response.set_cookie('cookie_test', 'test_value')
    return response


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)  # 로그인
            return redirect(reverse('user:index'))
    return render(request, 'user/register.html', {'form': form})
