from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$',views.welcome,name='welcome'),
  url(r'^search/',views.search_results,name='search'),
  url(r'^profile/(\d+)',views.profile,name='profile'),
  url(r'^update_profile/(\d+)', views.update_profile,name='update_profile'),
  url(r'^new_post/(\d+) ', views.new_post,name='post'),
  url(r'^new_post/', views.form,name='post1'),
  url(r'^comment/(\d+)$',views.comment,name='comment'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)