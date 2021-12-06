from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):

    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text':'POST METHOD!!!'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})

    '''
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

