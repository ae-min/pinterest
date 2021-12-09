from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


def hello_world(request):

    if request.user.is_authenticated: #사용자가 로그인하지 않은 경우 로그인창으로 이동시킴

        if request.method == "POST":

            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            hello_world_list = HelloWorld.objects.all()
            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

    '''
    return render(request, 'accountapp/hello_world.html', context={'text': POST METHOD!!!'})
    요청을 받은 객체 안에서 찾은 메소드가 POST 메소드일 경우, 기존의 render 방식을 사용하는데, 
    추가적으로 context라는 데이터 꾸러미 안에 텍스트라는 이름을 가졌고 내용은 POST METHOD!!!인 문장을 넣어서 리턴
    -> hello_world.html의 {{ text }} 가 호출되면, context의 text를 찾고 POST METHOD!!! 출력
    '''

    '''
    return render(request, 'base.html')
    #템플릿을 가지고와서 내용을 채워넣는 형식. 요청이 들어오면 base.html 템플릿페이지 반환
    #pinterest_settings_template DIR부분에 'DIRS': [os.path.join(BASE_DIR, 'templates')], 추가함
    '''

    '''
    return HttpResponse('hello world!')
    pinterest_account -> account_urls -> views_hello_world -> hello world! 출력하는 구조
    http://127.0.0.1:8000/account/hello_world/ -> hello world! 출력
    '''

class AccountCreateView(CreateView): #CRUD 중 C create
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #reverse : 함수형 뷰, reverse_lazy : 클래스형 뷰
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    #CRUD 중에 Read부분. 단, Read가 아닌 detail로 사용. 조회이기 때문에 어떤 모델사용, 정보를 어떻게 시각화할 것인지에 대한 정보만 필요
    model = User
    context_object_name = 'target_user'
    '''
    user는 로그인한 사람 정보인데, 예를들어 인스타그램의 다른 사람 계정을 조회하려는 경우에는 내 정보가 아닌 해당 계정주의 정보를 
    보여줘야하므로, detail페이지에 {{ target_user.username }} 처럼 내정보가 아닌 타겟 유저의 정보를 조회하도록 지정함
    '''
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView): #CRUD 중 U update
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world') #reverse : 함수형 뷰, reverse_lazy : 클래스형 뷰
    template_name = 'accountapp/update.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            #self.request.user.is_authenticated and : 현재 request.user 로그인이 되어있고
            #self.get_object() : self는 updateview를 가리키며, .get_object()는 이 안에서 현재 사용되고 있는 user object의 pk값을 가져옴.
            #그 후에 == self.request.user : 현재 리퀘스트를 보낸 유저와 같은지를 확인함.
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

        # return HttpResponseRedirect(reverse('accountapp:login'))
        # 로그인이 되어있으면 기존의 방식으로 하되, 안되어있을 경우 로그인창으로 이동 시킴

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden() 
        # 로그인이 되어있으면 기존의 방식으로 하되, 자신의 pk와 다른 pk에 접근 시, 금지된 곳에 접근했다는 페이지를 보여줌

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()
