from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')
    #어떤 user와 어떤 project. 그 쌍이 가지는 구독정보가 딱 하나가 되도록

    class Meta:
        unique_together = ('user', 'project')
        # 같은 프로젝트를 한 유저가 중복으로 구독할 수 없어야 맞는 것이므로, 유저-프로젝트가 한쌍만 나올 수 있도록 함
