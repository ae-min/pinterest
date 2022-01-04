from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView
from django.urls import reverse

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})
        #project_pk를 get방식으로 받아서, 이 pk를 가지고 있는 detail페이지로 이동

    def get(self, request, *args, **kwargs):

        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        # project_pk를 가지고 있는 Project를 찾는데, 만약 찾는게 없다면, 페이지를 찾을 수 없다는 404를 돌려줌
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, project=project)
        # 바로 윗 줄의 프로젝트와 유저 정보를 바탕으로 subscription을 찾음.
        # 유저가 위에서 찾은 유저이고, 프로젝트가 위에서 찾은 프로젝트인 subscription정보를 찾음

        if subscription.exists():   # 이미 구독한 정보가 존재한다면.
            subscription.delete()   # 중복구독 불가이므로, 앞서 찾은 정보는 없애버림.
        else: # 해당 구독 정보가 없다면
            Subscription(user=user, project=project).save() # 앞서 찾은 유저와 프로젝트 쌍에 대한 정보로 구독 생성.

        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    # 단순히 article을 전부 가져오는게 아니라, article 중에 특정 조건을 가진 게시물들만 가져와야 하므로, 쿼리셋 관련함수를 새로 작성
    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        # 유저가 구독 중인 프로젝트 찾기. Subscription내에서 유저의 모든 구독 정보를 가져오며, project 값들을 리스트화(values_list)
        # projects에는 구독한 모든 project 리스트가 담김

        article_list = Article.objects.filter(project__in=projects)
        # field lookups을 사용해 article_list를 만듬. 위에서 찾은 projects가 담김
        
        return article_list