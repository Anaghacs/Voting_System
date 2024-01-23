from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Create customized Users model.
# class Users(models.Model):
#     user_name=models.CharField(max_length=20)
#     first_name=models.CharField(max_length=20)
#     last_name=models.CharField(max_length=20)
#     email_id=models.EmailField(max_length=40)
#     password1=models.CharField(max_length=20)
#     confirm_password=models.CharField(max_length=20)
#     is_active=models.BooleanField(default=True)
#     is_staff=models.BooleanField(default=False)

#Create candidate model.
class Candidate(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    phone=models.CharField(max_length=12)
    bio=models.TextField()
    # photo=models.ImageField(upload_to="candidates")

# Create voting model.
class Votes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    candidate=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    # vote=models.PositiveIntegerField(default=0)


