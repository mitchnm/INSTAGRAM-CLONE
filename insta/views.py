from django.shortcuts import render, redirect
from .models import Image, Profile, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ImageForm, ProfileForm, CommentForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    image = Image.objects.all()
    profile1 = Profile.objects.all()
    return render(request, 'index.html', {"image": image, "profile1": profile1})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = User.objects.filter(username__icontains=search_term)
        profile = Profile.objects.all()
        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "profile": searched_profiles, "profile": profile})
    else:
        message = "You haven't searched for any term."
        return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def profile(request, id):
    image = Image.objects.filter(user_id=id)
    current_user = request.user
    user = User.objects.get(id=id)
    try:
        profile1 = Profile.objects.get(name=id)
    except ObjectDoesNotExist:
        return render(request,'profile.html')
    return render(request, 'profile.html', {"image": image, "user": user, "profile1": profile1})


@login_required(login_url='/accounts/login/')
def new_post(request,id):
    current_user = request.user
    image = Image.objects.get(user_id=id)
    if request.method == 'POST':
        print('noo')
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('welcome')

    else:
        form = ImageForm()
        print('xyz')
    return render(request, 'post.html', {"form": form, "image":image})


@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.name_id = current_user.id
            profile.save()
        return redirect('welcome')

    else:
        form = ProfileForm()
    return render(request, 'update_profile.html', {"form": form, "user": current_user})


@login_required(login_url='/accounts/login/')
def comment(request, id):
    current_user = request.user
    comments = Comment.objects.filter(image_id=id)
    profile = Profile.objects.all()
    image = Image.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.username = current_user
            comment.name_id = current_user.id
            comment.save()
        return redirect('welcome')

    else:
        form = CommentForm()
    return render(request, 'comment.html', {'image': image, 'comments': comments, 'form': form, "user":current_user, "profile":profile})
