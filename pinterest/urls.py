"""pinterest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from articleapp.views import ArticleListView

urlpatterns = [
    
    path('', ArticleListView.as_view(), name='home'),
    # 기본 127.0.0.1:8000 접속시 보여줄 페이지
    
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),
    path('likes/', include('likeapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=> 이미지파일을 보여주기 위해 pinterest_settings.py에 있는
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
이 내용들을 불러옴
'''
