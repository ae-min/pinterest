from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_record')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_record')

    class Meta:
        unique_together = ('user', 'article') #좋아요가 중복해서 찍히지 않도록, 한명당 한번의 좋아요만 가능하도록 제한 설정
