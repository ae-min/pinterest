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