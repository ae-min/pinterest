# course 29 commit

@super 계정 생성
python manage.py createsuperuser 

@장고에서 이미지를 관리할 때 필요한 라이브러리 설치
pip install pillow

# course 30 commit

accountapp의 usercreationForm은 중요한 계정기능이므로 장고에서 기본 제공.
하지만, profileapp에서는 사용 불가하므로, model을 생성했으면 비슷한 형식의 form을 직접 새로 만들어서 사용해야 함.
그런데, 데이터가 수십 개 이상 방대할 경우, 이를 쉽게 만들기 위해 ModelForm 사용

@ ModelForm :
- 기존에 있었던 model을 그대로 form으로 변환해주는 기능
- modelForm을 상속받은 후에, 어떤 모델을 사용할 것인지, 어떤 필드를 입력할 수 있게 만들 것인지 설정해주면, model이 그대로 form으로 변환됨.

ex) 
class ProfileCreationForm(ModelForm):
   class Meta:
      model = Profile
      fields = ['image', 'nickname', 'message']

*model의 user는 서버에서 따로 처리

# course 31 commit

@새로운 app생성
모델을 만들었으면 db에 반영
1) python manage.py makemigrations
2) python manage.py migrate

# course 34 commit 
@Magic-Grid 

주소 : https://github.com/e-oj/Magic-Grid
1) on JSFIDDLE 하이퍼링크 클릭시, 주소이동 (https://jsfiddle.net/eolaojo/4pov0rdf/)  // html,css,자바스크립트 소스
2) dist 폴더 내의 magic-grid.cjs.js  // js소스

---
@랜덤이미지 사용 

주소 : https://picsum.photos/

img태그 src에 "https://picsum.photos/200/300" 주소 입력

# course 36 commit

@pagination

이전페이지, 다음페이지 존재여부 확인하여 1,2,3 등의 페이지 번호들을 보여주며, 해당 페이지로 이동 가능

@infinite scroll 

페이스북, 인스타그램, 핀터레스트와 같은 무한 스크롤

# course 37 commit

@Mixin 다중상속

detailView의 content영역에 게시물 내용이 나오고 
하단에 commentForm 영역이 나와야 하는데 
현재 detailView는 폼이 없고 오브젝트만 있으므로
이 문제를 해결하기 위해 mixin 사용


# course 38 commit

@모바일에서 확인하는 방법

(PC는 python manage.py runserver 127.0.0.1:8000)

모바일은 python manage.py runserver 0.0.0.0:8000 으로 서버를 열고, 

'0.0.0.0 자리에 내 ip주소 :8000' 입력하여 확인 가능

setting.py의 ALLOWED_HOST => '*' : 모든 호스트의 접근 허용

---
@media screen and (max-width:500px) {
    html {
        font-size : 13px;
    }
}

=> 지정한 너비인 500px 이하로 떨어지면 해당 설정을 적용하여 반응형 사이트 구현

# course 40 commit

@새로운 앱 생성

python manage.py startapp projectapp

---
@ a:hover 

a태그에 마우스를 올렸을 때

@ text-decoration : none;

a태그의 언더바 제거

---
<a href="{% url 'articleapp:list' %}?page={{ page_obj.next_page_number }}"
       class="btn btn-secondary rounded-pill">
        {{ page_obj.next_page_number }}
</a>

=> {% url 'articleapp:list' %} 이부분을 제거하면, 

articleapp에서만 사용 가능한게 아니라 어디서든 사용 가능해짐.

---
@ 보여지는 글자수 제한

truncatechars : 글자수

제한한 글자수 까지만 보여진 후, 뒷 부분은 ... 표시됨

# course 43 commit

@ Field Lookup

조금 더 복잡한 DB쿼리를 사용자가 구현할 수록 있도록 하는 기능

articles.objects.filter(pk=xxx, user=xxx)

=> articles.objects.filter(project__in=projects)

** project__in 이 부분은

SQL문의 select...where peoject in(...);와 같음

# course 44 commit

@ Medium Editor 사용을 통한 WYSIWYS 구현

WYSIWYS : what you see is what you get '보는대로 글이 써진다'

글을 쓸때 볼드체, 기울임, 언더라인, 글씨크기 조정 등의 기능 제공

https://github.com/yabwe/medium-editor

1. For a custom one:

2. You can now instantiate a new MediumEditor object:

두 부분의 소스코드 사용함

# course 45 commit

@ material-design-icons 구글 무료제공 아이콘

https://fonts.google.com/icons?selected=Material+Icons

@ 사용법

https://github.com/google/material-design-icons

---
# account/views.py - hello_world 코드 제거

    @login_required #데코레이터
    def hello_world(request):
        if request.user.is_authenticated:
        if request.method == "POST":
    
            temp = request.POST.get('hello_world_input')
    
            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()
    
            # hello_world_list = HelloWorld.objects.all()
            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        else: return HttpResponseRedirect(reverse('accountapp:login')) ->데코레이터가 대신함

---

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
---
    
    return render(request, 'accountapp/hello_world.html', context={'text': POST METHOD!!!'})
    요청을 받은 객체 안에서 찾은 메소드가 POST 메소드일 경우, 기존의 render 방식을 사용하는데, 
    추가적으로 context라는 데이터 꾸러미 안에 텍스트라는 이름을 가졌고 내용은 POST METHOD!!!인 문장을 넣어서 리턴
    -> hello_world.html의 {{ text }} 가 호출되면, context의 text를 찾고 POST METHOD!!! 출력
---
    return render(request, 'base.html')
    #템플릿을 가지고와서 내용을 채워넣는 형식. 요청이 들어오면 base.html 템플릿페이지 반환
    #pinterest_settings_template DIR부분에 'DIRS': [os.path.join(BASE_DIR, 'templates')], 추가함
---
    return HttpResponse('hello world!')
    pinterest_account -> account_urls -> views_hello_world -> hello world! 출력하는 구조
    http://127.0.0.1:8000/account/hello_world/ -> hello world! 출력

---
# google font

https://fonts.google.com/?subset=korean

select this style 선택

link : head.html

css : static/base.css

# Docker

1. 도커란
- 가상화 기반 : 기존의 방식은 OS 위에 가상머신(VM)을 나눠서 만드는 방식이었다면, 도커는 OS위에 컨테이너를 만드는 방식으로,
                      언제 어느 곳에서 어떤 OS를 쓰던간에 규격화되고 표준화된 같은 환경의 컨테이너를 사용 가능함

- 일반 OS를 사용하는 것과 비슷한 빠른 속도로 사용가능. VM에 비해 도커는 성능하락이 거의 없음
- 개발 배포 빌드 유지보수 모두 다 빠름
---
2. 도커의 장점

- 도커가 없이 배포할 경우 : 개발환경과 OS환경의 호환성, 개발 시 사용한 것과 의존된 프로그램 설치, 파이썬 설치, 관련 라이브러리 설치, 환경변수 설정, 테스트가 어떻게 되는지 확인 등 해야할 것이 많고 번거로움.

- 도커를 사용한다면 : 최초 한번은 (호환성, 관련 설치, 테스트 등)을 해야하지만, 한 번 만들어 뒀으면 추후에 발생되는 추가적인 일들은 없음. 

- 최초 한번 만들어둔 것을 이미지 형태로 저장을 해둔 뒤, 이 이미지를 원할때마다 실제 서버에 구축하는 형태 (컨테이너를 사용하여 구축)
---
3. 도커의 필요성

* 만약 서버를 한번 빌려 배포 후, 어떠한 유지보수도 이루어지지 않는 경우라면 도커를 안써도 되겠지만,
실제로 배포를 하다보면 서버다운, 서버이동, 유지보수 등의 여러 애로사항이 발생하기때문에 도커가 유용함. 이미지를 계속 복제해서 컨테이너 형식으로 구축하면 되므로 매우 편리해짐.

* [이미지 = 클래스] , [컨테이너 = 인스턴스]의 관계라고 이해 가능 => 이미지를 상속받아 새로운 이미지를 만들 수 있고, 이미지를 상속받아 새로운 객체를 만들 수도 있고

# vultr의 vps 대여

@ vps

virtual private server : 가상 사설 서버 = 가상의 독자적인 서비스를 빌려준다.

물리적인 서버 하나에서, 물리적 서버의 일정 자원을 분배시켜놓은 가상 서버 하나를 우리가 빌리는게 vps

물리적 서버 통째로 빌리는 것은 비싸므로, 이렇게 분배된 가상서버를 저렴하게 대여

# vps대여 후, docker를 사용하기 위한 접속

https://www.vultr.com/

@ ssh : 원격 서버 접속 가능

1. cmd 창에서 ssh root@대여받은 ip주소 입력
2. 비밀번호는 복사한 뒤. cmd에서 마우스 우클릭 후 엔터 -> 가상서버 접속 완료

* root@vultr:~# docker => 도커 설치여부 확인 가능

* docker container ls => 도커 컨테이너가 뭐가 돌고 있는지 확인 가능

# dockerhub 'potainer'

https://hub.docker.com/r/portainer/portainer-ce

이미지를 이용해 컨테이너를 구성하는 방식인데, 현재는 이미지가 없으므로, 도커허브에서 이미지를 받아서 실제 컨테이너를 만드는데 사용할 것.

---
@ portainer.io

https://hub.docker.com/r/portainer/portainer-ce

도커시스템을 GUI형태로 볼 수 있도록 바꿔주는 소프트웨어

cmd로 관리 시, 도커에 대한 이해가 어려우므로 GUI화 해서 이해가 쉽게 하기 위해 portainer 설치

도커허브에서 portainer라는 컨테이너를 공식이미지를 찾은다음, 

그 이미지를 가져와서 우리의 도커시스템. 우리의 가상서버에 컨테이너를 실제로 만들 작업을 할 것임.
