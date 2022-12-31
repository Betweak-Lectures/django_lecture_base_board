# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Board, Comment


def index(request):
    board_list = Board.objects.all()
    return render(request, 'board/index.html', {'board_list': board_list})


def board_detail(request, board_id):
    board = Board.objects.prefetch_related('comment_set').get(id=board_id)
    return render(request, 'board/detail.html', {'board': board})


def board_create(request):
    return render(request, 'board/create.html')
