from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

from webapp.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description', 'author_name','likes']

