from django.shortcuts import render
from .models import Image
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
  image = Image.objects.all()
  return render(request, 'index.html', {"image":image})

def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message, "profile":searched_profiles})
    else:
        message = "You haven't searched for any term."
        return render(request, 'search.html', {"message":message})
