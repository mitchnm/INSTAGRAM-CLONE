from .models import Image, Profile, Comment
from django import forms
from django.forms import ModelForm,Textarea,IntegerField

class ImageForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ['likes','comments', 'user', 'profile']

class ProfileForm(forms.ModelForm):
   class Meta:
       model = Profile
       exclude = ['name']
class CommentForm(forms.ModelForm):
   class Meta:
       model = Comment
       exclude = ['user','image']