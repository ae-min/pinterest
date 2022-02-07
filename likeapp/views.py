from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord
from django.urls import reverse
from django.contrib import messages


@method_decorator(login_required, 'get') #로그인한 사람만 좋아요 가능이 가능하도록 제한
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk':kwargs['pk']})

    def get(self, *args, **kwargs):

        user = self.request.user #셀프해서 리퀘스트를 보내는 사람이 user
        article = get_object_or_404(Article, pk=kwargs['pk']) #article안에서 pk=kwargs['pk'] 값을 받은 article

        # 게시물에 좋아요를 이미 눌렀는지 확인하는 부분
        if LikeRecord.objects.filter(user=user, article=article).exists(): #이미 누른적이 있는 경우, 다시 돌아가기
            messages.add_message(self.request, messages.ERROR, '이미 좋아하는 게시물입니다.')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
        else:
            LikeRecord(user=user, article=article).save() #누른적이 없는 경우, user와article짝을 맞춰서 기록을 남기고 저장

        article.like += 1 #누르면 좋아욕 개수가 1씩 추가되도록
        article.save() #최종 저장

        messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영되었습니다.')

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)
