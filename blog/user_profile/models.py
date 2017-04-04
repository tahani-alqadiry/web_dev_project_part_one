from django.db import models
from django.contrib.auth.models import AbstractBaseUser



class User(AbstractBaseUser):
    username = models.CharField('username', max_length=10, unique=True, db_index=True)
    email = models.EmailField('email address', unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    following = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    birth_date = models.DateField()
    blog_name = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Blog(models.Model):
    blog_name = models.CharField(max_length=20, unique=True)
    admin_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_name



