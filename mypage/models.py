from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class Remail(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    remail1 = models.EmailField(max_length=255, unique=True, null = True, default="")
    remail2 = models.EmailField(max_length=255, unique=True, null = True, default="")
    remail3 = models.EmailField(max_length=255, unique=True, null = True, default="")
    remail4 = models.EmailField(max_length=255, unique=True, null = True, default="")
    remail5 = models.EmailField(max_length=255, unique=True, null = True, default="")
    category1 = models.CharField(max_length=10, null = True, default="")
    category2 = models.CharField(max_length=10, null = True, default="")
    category3 = models.CharField(max_length=10, null = True, default="")
    category4 = models.CharField(max_length=10, null = True, default="")
    category5 = models.CharField(max_length=10, null = True, default="")
    

    def __str__(self):
        return self.user.username
    
