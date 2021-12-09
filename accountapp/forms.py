from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True # mypage_changeinfo에서 아이디 또한 보여지고, 변경이 가능한 것을 방지하기 위함.
        # username(==ID)을 disabled=True 비활성화 하겠다. 그러면 아이디는 보여지지만 비활설화되어 수정불가한 회색으로 보여짐
        # views.py에서 form_class = AccountUpdateView를 form_class = AccountUpdateForm으로 변경함
