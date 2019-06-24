from .models import Image, Profile
from django import forms

class UpdateProfile(forms.ModelForm):
    class Meta:
      models = Profile