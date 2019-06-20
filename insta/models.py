from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length =60)
    profile_pic = models.ImageField(upload_to = 'instagram/')
    bio = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'instagram/')
    image_name = models.CharField(max_length =60)
    caption = models.CharField(max_length =200)
    profile = models.ForeignKey(Profile)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length=500)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()