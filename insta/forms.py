from .models import Image, Profile, Comment
from django import forms

class NewPostForm(forms.ModelForm):
   class Meta:
       model = Image
       exclude = ['likes','comments', 'name_of_image', 'profile']
class NewProfileForm(forms.ModelForm):
   class Meta:
       model = Profile
       exclude = ['']
class CommentForm(forms.ModelForm):
   class Meta:
       model = Comment
       exclude = ['']