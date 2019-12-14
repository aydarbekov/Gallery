from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

from webapp.models import Photo, Comment


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description', 'author_name','likes']


class PhotoCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
