from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    Phone = models.TextField(blank=True,null=True)
    HasGarden = models.BooleanField(default=False,null=True)
    PastPetExperience = models.IntegerField(default=0)
    Age = models.IntegerField(blank=True,null=True)
    Occupation = models.TextField(blank=True,null=True)


class Post(models.Model):
    created_by = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    animal= models.TextField()
    desc = models.TextField()
    name = models.TextField()
    age = models.DecimalField(decimal_places=1,max_digits=2)
    imageurl = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    State= models.TextField(blank=True,null=True)
    District = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.created_by} : {self.pk}" 

class Message(models.Model):
    sender= models.ForeignKey("User", on_delete=models.CASCADE, related_name="sent")
    receiver=models.ForeignKey("User", on_delete=models.CASCADE, related_name="received")
    message= models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    