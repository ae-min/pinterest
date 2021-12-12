from django.forms import ModelForm

from profileapp.models import Profile

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']

    '''
    @user는 폼에 보여지지 않고 서버에서 만든 이유
    클라이언트에서 이미지, 닉네임, 메시지의 주인이 누구인지 user를 통해 보여주게 되면, 
    그 정보들을 활용해서 다른 사람의 프로필을 만들 수도 있으므로, 악용 방지를 위해 user는 서버내에서 구현하기로 함.(views.py)
    '''