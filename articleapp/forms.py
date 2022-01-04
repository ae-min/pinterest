from django.forms import ModelForm
from django import forms
from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # WYSIWYG 사용을 위한 커스터마이징
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start', 'style': 'height:auto;'}))
    # <!-- WYSIWYG --> <script>var editor = new MediumEditor('.editable');</script>
    # bootstrap5에서는 text-left가 text-start로 변경됨.

    # article 작성 시, project를 필수 선택하지 않아도 등록 가능하도록 하는 부분 (required=False) -> 이 내용이 있어야 필수선택 안해도됨
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    # ModelChoiceField : 외래키 사용과 관련된 필드

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
