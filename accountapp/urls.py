from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"
'''
"127.0.0.1:8000/account/hello_world"라고 쓰기에 길어서 불편하므로, 
나중에는 함수를 활용해 accountapp:hello_world 방식으로 접근하기 위해 app_name을 만들어줌
'''

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    #accountapp-views의 hello_world라는 주소에 접근하면, 해당 hello_world뷰를 되돌려주는 구조 (접근경로, 보여쥴뷰, 이름)
    path('create/', AccountCreateView.as_view(), name='create'),
    #함수형이 아닌, 클래스형일 경우에는 : 클래스명.as_view() 형식으로 작성.
]