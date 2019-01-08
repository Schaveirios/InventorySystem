from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    photos = models.ImageField(upload_to='photos',blank=True)
    
    def __str__(self):
        return self.user.username


class UserActivity(models.Model):
    username = models.CharField(max_length=200)
    activity = models.CharField(max_length=200)
    date = models.DateTimeField("Entry Date")
    # use .strftime("%Y-%m-%d %H:%M")
    def __str__(self):
        return self.username