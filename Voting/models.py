from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
# Create your models here.


#Create candidate model.
class Candidate(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    phone=models.CharField(max_length=12)
    bio=models.TextField()
    photo=models.ImageField(upload_to='candidate',blank=True)

    #display fullname
    def __str__(self):
        return self.fullname

    # def __str__(self):
    #     return f"ID{self.fullname} - {self.phone} "
    
    # class Meta:
    #     verbose_name_plural = 'AL CANDIDATES'

# Create voting model.
class Votes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    candidate=models.ForeignKey(Candidate,on_delete=models.CASCADE)


