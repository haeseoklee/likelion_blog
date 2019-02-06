from django import forms
from .models import Blog

class BlogModelForm(forms.ModelForm):

    title = forms.CharField(label='제목')
    body = forms.CharField(label='내용', widget=forms.Textarea())

    class Meta:
        model = Blog
        fields = ['title', 'body']