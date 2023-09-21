from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 기존에 있는 User 클래스를 사용하기 위해
class User(AbstractUser):
    pass