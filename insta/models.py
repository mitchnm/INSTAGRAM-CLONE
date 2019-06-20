from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'instagram/')
    bio = models.CharField(max_length=250)

class Image(models.Model):
    image = models.ImageField(upload_to = 'instagram/')
    image_name = models.CharField(max_length =60)
    caption = models.CharField(max_length =200)
    profile = models.ForeignKey(Profile)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length=500)

    def __str__(self):
        return self.img_name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()