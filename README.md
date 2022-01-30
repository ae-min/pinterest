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

# 설치된 portainer 확인 방법

1. cmd창에 docker volume create portainer_data

2. docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
---
@ 1,2번 입력 후 나오는 부분

Unable to find image 'portainer/portainer-ce:latest' locally
latest: Pulling from portainer/portainer-ce

=> 가상서버 내에 있는 도커시스템에서 이미지를 찾지 못했기 때문에 도커허브에서 이미지를 가져왔다

---
3. docker container ls => 현재 구동중인 컨테이너 확인

---

http:// 본인의 가상서버주소:9000 접속

=> 내가 설치한 portainer 컨테이너가 정상적으로 구동됨 확인 가능
=> 빌린 가상서버 내부에 있는 도커시스템에서 어떤 일이 벌어지는지를 GUI환경 하에서 모니터링할 수 있는 구축이 완료됨

# course 49 'nginx 컨테이너 추가'
@ container - add container - name 입력 - image : 도커허브에서 가져올 이미지 (nginx) - 포트 선택 - deploy the container

@ Manual network port publishing의 +publish a new network port : 

내가 발린 가상서버 host 포트와 potainer 포트 지정하여 서로 연결

nginx 컨테이너는 테스트용이므로 기본 http프로토콜 포트인 80번으로 지정

# course 50 'django container 추가 순서'
1. github에 나의 소스 업로드
2. 도커파일 만들기 : 이미지를 만드는 설계서. 어떤 식으로 시스템을 만들것인지에 대한 설계서
3. 이미지 빌드 : 실제로 이미지 빌드
4. 컨테이너 구동 : 이미지를 기반으로 장고 컨테이너 구동

# course 50 'requirements.txt 파일 생성'
도커는 나의 장고 프로젝트에서 어떤 라이브러리를 설치 했었는지를 모르기 때문에, 설치된 라이브러리 정보를 requrements.txt문서로 따로 남겨줘야함

입력 : pip freeze > requirements.txt

=> 새로만드는 컨테이너에서도 이 파일 하나로, 같은 가상환경 구축이 가능해진다.

# course 51 'Dockerfile 구문'

@ Dockerfile  

어떻게 이미지를 만들지에 대한 설계서 (이미지 : 어떤os, 어떤 라이브러리, path 등등)

어떻게 환경설정을 했는지 알고서 그 것을 실제 도커파일에 그대로 적어줘야함.

---

@ Dockerfile command 

1. from : 시작이되는 베이스 이미지를 무엇을 쓸지 골라주는 커맨드
2. run : 커맨드 실행 run pip install~ 이런 방식
3. workdir : cd..와 비슷(cd:체인지디렉토리)
4. expose : 장고 컨테이너가 어떤 포트를 사용할것인지
5. cmd : 커맨드를 입력하는 곳 

# course 52 'Dockerfile 생성'

작성방법은 Dockerfile 주석 참고

@ potainer 생성정보

이미지 : django_test_image:1

컨테이너 : django_container

# course 53 'gunicorn'

python manage.py runserver로 배포하는 것은 하면 안되는 방법임.

장고는 웹프레임워크를 만드는 것이지, 웹서버를 만드는 것이 아니기 때문에 

보안이슈 등에 대해 정확한 테스트를 거치지도 않았으므로 배포에 사용하면 안됨

=> 이러한 문제 해결을 위해 장고컨테이너안에 gunicorn이라는 라이브러리를 설치해야함. 설치하면 원래 쓰던 runserver이라는 명령어를 gunicorn 자체의 커맨드로 교체됨

---
@ gunicorn

요청을 먼저 앞단에서 받아주는 nginx라는 웹서버와 내가 만든 장고컨테이너를 연결시켜주는 인터페이스

장고컨테이너안에 구니콘을 설치하고, 설치한 상태로 다시 도커이미지를 새로 만들고, 그 이미지를 컨테이너로 만들면 됨

---
@ gunicorn 설치

pip install gunicorn 

@ gunicorn이 포함되도록 설치된 라이브러리 파일 재작성

pip freeze > requirements.txt

---
@ 특정 파일만 커밋에 올리기

git add requirements.txt

---
@ gunicorn container (호스트 8080 - 컨테이너 8000)

구니콘 컨테이너의 경우 css와 같은 정적파일을 불러오지 못함. 

이걸 nginx라는 서버를 앞단에 연결시킴으로써 해결 가능

(구니콘은 nginx와 장고 컨테이너를 연결시켜주는 인터페이스이므로 nginx를 연결해줘야함
nginx-gunicorn-django)

# course 54 'Docker Network'

유저가 요청을 줄 때는 vps의 ip와 port번호를 참고해 서버에 접속하면되는데,

nginx 컨테이너에서 장고 컨테이너로 요청을 보낼 때는, ip adress로 보내야할지 도메인으로 보내야할지 모름

이러한 어디로 보낼지 모르는 문제를 해결해주는 도구가 'docker network'

** 네트워크 : 컨테이너를 여러개 만드는데, 그 컨테이너들을 하나의 네트워크로 묶어주는 것

---
네트워크 안에 컨테이너마다 이름이 정해져있는데 (ex. nginx / django_container_gunicorn)

이 컨테이너 이름을 기반으로 서로 요청을 주고 받을 수 있게 할 수 있음
 
docker network 안에서는 컨테이너 이름 자체가 도메인처럼 쓰임. 

www.naver.com 쓰는 것처럼 컨테이너 이름이 도메인처럼 쓰임.

=> nginx컨테이너에서 http://django_container_gunicorn:8000이라는 주소를 넣어서 요청을 보내게되면,
실제로 장고컨테이너로 요청을 보낼 수 있음

---
@ 1. portainer에서 새로운 'nginx-django' 네트워크 생성

이름만 기재하고 create the network

---
@ 2. portainer에서 새로운 'django_container_gunicorn' 컨테이너 생성

장고컨테이너들의 경우 원래는 8000번 포트 등으로 해서 외부와 연결시켜줬는데,

유저에서 보내는 요청을 앞단인 nginx에서 먼저 받은 다음, 

장고로 넘겨주기 때문에, 장고에서 외부 포트를 연결시켜줄 필요가 없으므로 포트 지정안해도됨

** 네트워크 nginx-django지정

---
@ 3. 새로운 nginx 컨테이너 생성을 위한 'nginx.conf' 파일 생성

nginx를 만들기 전에 nginx 설정 파일을 만들어야함 (파이참 nginx.conf 파일 생성)

https://gunicorn.org/#deployment

nginx.conf 파일에 기본 틀을 복붙한 뒤 수정

    server {
    listen 80;
    server_name example.org;
    access_log  /var/log/nginx/example.log;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    }

proxy_pass http://django_container_gunicorn:8000;

=> 앞서 네트워크 설명에서 말했듯이 같은 네트워크 안에서는 컨테이너 이름으로 도메인 접속 가능

---
@ 4. '파일질라'를 이용해 nginx 설정파일을 가상서버에 올리기

https://filezilla-project.org/ (클라이언트설치)

vps에서 부여받은 호스트주소-사용자명-pw 입력 / 포트번호는 22로하여 빠른연결

가상서버에 /home/django_course 만들고 거기에 nginx.conf 파일 옮김

---
@ 5. portainer에서 새로운 'nginx' 컨테이너 생성

컨테이너이름 nginx 

이미지 nginx:latest

네트워크 nginx-django

볼륨 bind로 하고, 컨테이너에 /etc/nginx/nginx.conf 

호스트에 /home/django_course/nginx.conf 입력한 뒤 생성

# git에 잘못올린 파일 삭제 (내 pc에는 존재, git에서는 삭제)

git rm --cached 파일명

git commit -m "Fixed untracked files"

git push -u origin master

# 특정 파일만 git에 올리기

git add 파일명

ex) git add requirements.txt
 
# course 57 Docker Volume

nginx 내부의 static 파일들과 django의 static 파일들을 동기화 시키기 위해서 docker volume을 사용 

Docker Volume : 다른 컨테이너 내에 있는 데이터를 공유할 수 있는 기능

1. bind volume
- host server(vps서버)와 nginx 컨테이너간의 각 파일들을 연동, 동기화 시킴

2. named volume
- 도커 안에서 이름이 있는 새로운 볼륨을 만들고, 이 새로운 볼륨을 django컨테이너나 nginx같은 컨테이너들과 붙여서 동기화 가능
- 네임드볼륨은 도커가 알아서 관리
- 만약 네임드볼륨과 연결된 컨테이너들이 사라지더라도, 네임드 볼륨은 사라지지 않고 데이터를 유지시킴

# course 58 Docker Volume create

1. volume 생성 : static, media 볼륨 생성

2. container 생성 : django_container_gunicorn 

- (network : nginx, staticfiles폴더와 static볼륨 연결, midea와 media볼륨 연결), nginx생성(포트 80-80, 네트워크 nginx, 볼륨 : (컨테이너)/data/static과 static볼륨연결, /data/media와 media볼륨 연결), bind: /etc/nginx/nginx.conf - /home/django_course/nginx.conf)

---
3. nginx.conf : 앞단인 nginx컨테이너에서 static파일을  먼저 처리하도록 해당 코드 작성
    

    include mime.types;

    location /static/{
        alias /data/static/;
    }

     location /media/{
        alias /data/media/;
    }

# course 59,60 mariaDB 컨테이너를 이용한 DB분리 (개발/배포 분리)

현재 내 컴퓨터인 local의 DB는 : sqllite  / docker : mariaDB

mariaDB 컨테이너 생성 : https://hub.docker.com/_/mariadb 사이트에서 공식이미지 다운

# course 61 mariaDB 컨테이너 설정 및 django 연동

1. volume 생성 : volume 이름 'database'
2. container 생성 : 

이름 : mariadb, 이미지 :  mariadb, 네트워크 : nginx-django, 볼륨 : (컨테이너)/var/lib/mysql-(볼륨)database, 
env(환경변수) : name 4개 : MYSQL_ROOT_PASSWORD, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, value에 deploy.py의 database란에 적은 값 입력


3. Dockerfile 수정 후 -> 이미지 새로 빌드 -> 새로운 이미지로 다시 django_container_gunicorn 컨테이너 생성, 네트워크 nginx-django 설정

# course 62 "Docker Stack"

단순히 컨테이너만을 가지고 배포 시 발생 가능한 문제 :
1. 배포시마다, 컨테이너마다의 설정을 반복해야하는 문제
- 사소한 변화가 있을 때에도 전체적인 설정을 다시 해야하는 비효율성
- Docker Stack으로 해결 가능

@ Docker Stack :

컨테이너별로 들어가는 모든 세팅들을 하나의 total 파일로 만들어서 관리,

totla stack settings는 YML파일에 작성


2. 모종의 문제로 컨테이너가 종료될 때의 문제
- 사람이 계속 지켜보면서 종료된 컨테이너를 재실행 시키기 어려움
- nginx, django container, mariaDB를 각각의 서비스로 관리.
- 서비스가 하는일 : 컨테이너 셧다운 시 자동으로 재부팅 시켜줌. 서비스내에서는 필요에따라 컨테이너를 복제할수도, 줄일 수도 있음.

# course 63 "Docker Swarm"

현재 nginx container, django container, mariadb가 도커 시스템 위에서 돌아가고 있는데, 이 도커시스템을 포함하고 있는 가상서버 하나를 '노드'라고 부름

@Docker Swarm :
여러개의 노드가 있을 때, 여러 서버(노드) 를 하나의 서버인것처럼 이용할 수 있게 해주는 것이 docker swarm

노드가 한개가 아니라 여러개가 되었을 경우, 여러개의 노드를 이용해서 클러스터링 가능

각각의 컨테이너들을 서비스로 관리 중이라면, 노드 안에서 컨테이너당 서비스가 돌아가고 잇으며, 새로운 노드를 추가해서 서비스 복제 하는 방식으로 쉽게 관리 가능

Docker Swarm은 Kubernetes, Apache Mesos 같은 컨테이너 오케스트레이션 툴에 비해서 쉬움. 

핵심적인 부분만 쉽게 만들 수 있도록 구성이 되어있음


