from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
    #여기의 form은 forms.py의 class ProfileCreationForm(ModelForm):의 전체 데이터
    #models.py의 Profile에는 user, image, ninkname, message가 있지만, forms.py에는 user를 제외한 3가지 데이터만 있는 상태
        temp_profile = form.save(commit=False)
        #실제 데이터베이스에 저장하지 않고, 임시 대기 중인 데이터이므로 커밋하지 않게 지정
        #forms.py에 있는 3가지 정보는 있지만, 거기 정의되지 않은 user 데이터는 아직 없는 상태
        temp_profile.user = self.request.user
        #temp_profile의 user라는 데이터를,  self해서 리퀘스트를 보낸 그 당사자 유저로 정해줌
        temp_profile.save() #그 후, 최종 저장
        return super().form_valid(form) #나머지는 조상인 class ProfileCreateView(CreateView):의 결과를 리턴

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'