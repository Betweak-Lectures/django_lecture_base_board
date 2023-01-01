# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Board, Comment
from .forms import BoardForm, CommentForm


def index(request):
    board_list = Board.active_list().all()
    return render(request, 'board/index.html', {'board_list': board_list})


def board_detail(request, board_id):
    try:
        board = Board.active_list().prefetch_related('comment_set').get(id=board_id)
        comment_form = CommentForm(initial={'board': board})
    except Board.DoesNotExist:
        raise Http404("게시글이 없습니다.")
    return render(request, 'board/detail.html', {'board': board, 'comment_form': comment_form})


def board_create(request):
    form = BoardForm()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            return redirect(reverse('board:index', ))
    return render(request, 'board/create.html', {'form': form})


def board_edit(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if not board.is_active():
        raise Http404("게시물이 없습니다.")

    form = BoardForm({'title': board.title, 'content': board.content})

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            board.title = data['title']
            board.content = data['content']
            board.save()
            return redirect(reverse('board:detail', kwargs={'board_id': board.id}))
    return render(request, 'board/edit.html', {'form': form, 'board': board})


def board_delete(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if not board.is_active():
        raise Http404("게시물이 없습니다.")

    board = board.delete()
    return redirect(reverse('board:index', ))


def board_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            board = form.cleaned_data['board']

    return redirect(reverse('board:detail', kwargs=({'board_id': board.id})))

# def board_delete(request, board_id):
#     board = get_object_or_404(Board, id=board_id)
#     board.
