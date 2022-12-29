# board/models.py
from django.db import models
from django.utils import timezone


class Board(models.Model):
    id = models.AutoField(primary_key=True)  # integer(auto-increment)
    title = models.CharField(max_length=255)  # varchar(255)
    content = models.TextField()  # Text
    created_at = models.DateTimeField(auto_now_add=True)  # 추가될 때 default로 현재시간
    updated_at = models.DateTimeField(auto_now=True)  # 추가or업데이트 될 때 default로 현재시간
