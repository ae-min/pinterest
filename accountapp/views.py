from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):

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