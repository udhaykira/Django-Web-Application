from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #each user will have a specific profile
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #on_delete=models.CASCADE -> If you delete the user automatially the profile will get deleted
    image = models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    #pip install pillow
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

