# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Board, Comment


def index(request):
    board_list = Board.objects.all()
    return render(request, 'board/index.html', {'board_list': board_list})


def board_detail(request, board_id):
    try:
        board = Board.objects.prefetch_related('comment_set').get(id=board_id)
    except Board.DoesNotExist:
        raise Http404("게시글이 없습니다.")
    return render(request, 'board/detail.html', {'board': board})


def board_create(request):
    return render(request, 'board/create.html')
