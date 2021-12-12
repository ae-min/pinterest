# pinterest
Django, Docker, AWS


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
