from django.http import HttpResponseForbidden


def profile_ownership_required(func): #views.py에서 본인인지 인증하는 작업을 데코레이터가 대신하는 부분
    def decorated(request, *args, **kwargs):
        from profileapp.models import Profile
        profile = Profile.objects.get(pk=kwargs['pk']) #profile_urls.py의 update로 pk를 받아서 이 프로파일의 주인을 확인하고
        if not profile.user == request.user: #해당 프로파일의 유저가 리퀘스트를 보내는 유저와 같지 않다면
            return HttpResponseForbidden() #접근불가 페이지 보여주기
        return func(request, *args, **kwargs) #맞으면 원하는 페이지로 보내주기
    return decorated

