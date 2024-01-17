from django.db import models

# Create your models here.

#Create customized Users model.
class Users(models.Model):
    user_name=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email_id=models.EmailField(max_length=40)
    password1=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)


#Create candidate model.
class Candidate(models.model):
    fullname=models.CharField(max_length=20)
    email_id=models.EmailField(max_length=20)
    phone_no=models.CharField(max_length=12)
    bio=models.TextField()
    photo=models.ImageField(upload_to="candidates")

# Create voting model.
class Vote(models.model):
    user_name=models.ForeignKey(Users,on_delete=models.CASCADE)
    candidate_name=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    vote_no=models.PositiveIntegerField()

