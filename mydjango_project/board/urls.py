from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:board_id>', views.board_detail, name='detail'),
    path('write', views.board_create, name='write'),
    path('comment', views.board_comment, name='comment'),
]
