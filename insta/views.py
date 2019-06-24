from django.shortcuts import render, redirect
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewPostForm, NewProfileForm, CommentForm

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
        profile = Profile.objects.all()
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message, "profile":searched_profiles, "profile":profile})
    else:
        message = "You haven't searched for any term."
        return render(request, 'search.html', {"message":message})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    image = Image.objects.filter(name_of_image_id=id)
    current_user = request.user
    user = User.objects.get(id=id)
    profile = Profile.objects.all()
    try:
      profile1 = Profile.objects.filter(name_id=id)
    except ObjectDoesNotExist:
      return redirect(user.id)
    return render(request, 'profile.html', {"image":image, "user":user, "profile":profile1, "profile":profile})

# @login_required(login_url='/accounts/login/')
# def new_post(request, id):
#    current_user = request.user
#    profile = Profile.objects.get(name_id=id)
#    if request.method == 'POST':
#        form = NewPostForm(request.POST, request.FILES)
#        if form.is_valid():
#            image = form.save(commit=False)
#            image.name_of_image=current_user
#            image.save_image()
#        return redirect('welcome')

#    else:
#        form = NewPostForm()
#    return render(request, 'post.html', {"form": form, "profile12":profile})

@login_required(login_url='/accounts/login/')
def new_post(request):
  current_user = request.user
  if request.method == 'POST':
      form = NewPostForm(request.POST, request.FILES)
      if form.is_valid():
          image = form.save(commit=False)
          image.user = current_user
          image.save()
      return redirect(home)

  else:
      form = NewPostForm()
  return render(request,'post.html',{'user':current_user,'form':form,})

@login_required(login_url='/accounts/login/')
def update_profile(request,id):
   current_user = request.user
   if request.method == 'POST':
       form = NewProfileForm(request.POST, request.FILES)
       if form.is_valid():
           profile = form.save(commit=False)
           profile.username = current_user
           profile.name_id=current_user.id
           profile.save()
       return redirect('profile')
   else:
       form = NewProfileForm()
   return render(request, 'update_profile.html', {"form":form, "user":current_user})

@login_required(login_url='/accounts/login/')
def comment(request,id):
   image =Image.objects.get(id=id)
   form = CommentForm()
   try:
       comments = Comment.objects.filter(id=id)
   except:
       form = CommentForm()
   return render(request,'comment.html',{'image':image,'comments':comments,'form':form})

def form(request):
    form = NewPostForm()
    return render(request, 'post.html', {"form":form})

