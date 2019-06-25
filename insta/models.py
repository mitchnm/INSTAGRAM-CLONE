from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    profile_pic = models.ImageField(upload_to = 'instagram/')
    bio = models.CharField(max_length=250)
    
    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()


    # @classmethod
    # def search_by_name(cls,search_term):
    #     prof_name = cls.objects.filter(username__icontains=search_term)
    #     return prof_name
    
class Comment(models.Model):
    user = models.ForeignKey(User)
    image = models.ForeignKey('Image')
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.comment

class Image(models.Model):
    image = models.ImageField(upload_to = 'instagram/')
    image_name = models.CharField(max_length =60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length =200, blank=True)
    profile = models.ForeignKey(Profile, null=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.image_name

    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

