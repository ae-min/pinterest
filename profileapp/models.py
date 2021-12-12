from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # OneToOneField : Profile과 user를 1:1로 연결
    # on_delete=models.CASCADE : user가 사라지면 그 유저와 연결된 Profile역시 연쇄삭제됨
    # related_name='profile' : request.user 접근 시, 따로 프로필 객체를 찾지 않더라도 request.user.profile 해당 유저의 프로필에 바로 접근할 수 있도록 이름을 정해주는 것
    image = models.ImageField(upload_to='profile/', null=True)
    # upload_to= : 이미지를 받아서 서버 내부에 저장할 것임. 그 이미지가 어디에 저장될 것인지 경로를 정해주는 것. media 밑에 profile 이라는 경로에 이미지가 저장됨
    # null=True : 꼭 이미지가 없어도 괜찮다
    nickname = models.CharField(max_length=20, unique=True, null=True) #unique=True : 유일한 닉네임을 가져라
    message = models.CharField(max_length=100, null=True)
