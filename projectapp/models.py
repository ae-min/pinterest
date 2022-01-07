from django.db import models

class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now=True)

    #article create 시 어떤 프로젝트인지 이름을 보여주기 위한 부분
    def __str__(self):
        return f'{self.pk} : {self.title}'
        # [게시판번호 : 게시판이름]으로 출력되는 구조