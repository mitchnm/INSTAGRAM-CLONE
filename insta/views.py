from django.shortcuts import render, redirect
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
  image = Image.objects.all()
  profile = Profile.objects.all()
  return render(request, 'index.html', {"image":image, "profile":profile})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = User.objects.filter(username__icontains=search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message, "profile":searched_profiles})
    else:
        message = "You haven't searched for any term."
        return render(request, 'search.html', {"message":message})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    image = Image.objects.filter(name_of_image_id=id)
    current_user = request.user
    user = User.objects.get(id=id)
    try:
      profile = Profile.objects.filter(name_id=id)
    except ObjectDoesNotExist:
      return redirect(user.id)
    return render(request, 'profile.html', {"image":image, "user":user, "profile":profile})
