from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,AnonymousUser
# Create your models here.





class CrmUser(AbstractUser):
    username = models.CharField(max_length=255)


    REQUIRED_FIELDS = ['username']