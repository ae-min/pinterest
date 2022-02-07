from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    #on_delete=models.SET_NULL : 회원탈퇴 시, 게시물이 삭제되지 않고 주인없는 알 수 없는 게시물로 남게함
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    #어느 게시판에 해당하는지

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True) #auto_now_add=True : 생성된 시간 자동 저장

    like = models.IntegerField(default=0) #좋아요기능

