from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func): #views.py에서 본인인지 인증하는 작업을 데코레이터가 대신하는 부분
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk']) #요청을 받으면서 기본키(PK)로 받은 값을 가지고 있는 article을 찾아서
        if not article.writer == request.user: #현재 user가 article 작성자가 아니면
            return HttpResponseForbidden() #접근불가 페이지 보여주기
        return func(request, *args, **kwargs) #맞으면 원하는 페이지로 보내주기
    return decorated

