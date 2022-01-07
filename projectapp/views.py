from django.views.generic import CreateView, DetailView, ListView

from django.urls import reverse
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
            # 유저가 인증이 되었으면, (유저와 프로젝트)구독정보를 찾음
        else:
            # 인증되어있지 않으면
            subscription = None

        object_list = Article.objects.filter(project=self.get_object())
        #현재의 project의 오브젝트와 같은 프로젝트를 가진 article을 필터링
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription, **kwargs)
        # subscription에 위에서 찾은 subscription 정보를 넣어줌
        # 필터링된 게시글들을 오브젝트 리스트에 넣어서 되돌려줌

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25