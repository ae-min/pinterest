from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"
'''
"127.0.0.1:8000/account/hello_world"라고 쓰기에 길어서 불편하므로, 
나중에는 함수를 활용해 accountapp:hello_world 방식으로 접근하기 위해 app_name을 만들어줌
'''

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    #accountapp-views의 hello_world라는 주소에 접근하면, 해당 hello_world뷰를 되돌려주는 구조 (접근경로, 보여쥴뷰, 이름)

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    #함수형이 아닌, 클래스형일 경우에는 : 클래스명.as_view() 형식으로 작성.
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    #특정 회원의 정보만을 보여주는 것이기 때문에 회원에 대한 기본키가 필요함. 몇번 유저에 대해 접근할 것인지 지정하기 위해 <int:pk> 작성
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]