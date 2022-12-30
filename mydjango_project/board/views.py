# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Board, Comment


def index(request):
    board_list = Board.objects.all()
    return render(request, 'board/index.html', {'board_list': board_list})
