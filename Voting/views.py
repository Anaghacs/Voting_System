from django.shortcuts import render,redirect
from .models import Candidate,Vote
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'base.html')

def signup(request):
    # if request.method=="POST":
        # username=request.POST['username']
        # first_name=request.POST['first_name']
        # last_name=request.POST['last_name']
        # email_id=request.POST['email']
        # password1=request.POST['password1']
        # password2=request.POST['password2']
        # user=User(username=username,first_name=first_name,last_name=last_name,email_id=email_id,password1=password1,password2=password2)
        # user.save()
        # print(user.objects.all())
        return render(request,'signup.html')
        

#Create admin home page functions.
def admin_home(request):
    return render(request,'admin_home.html')