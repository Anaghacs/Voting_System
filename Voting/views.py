from django.shortcuts import render,redirect
from .models import Candidate,Vote
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'base.html')

#The user registration or signup form for the user.
def signup(request):
    #The form submition field daata fetch
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password1']
        confirm_password=request.POST['password2']

        #if condition checking username already exist then display the error message.
        if User.objects.filter(username=username).exists():
            messages.info(request,"Uersname is already exist! Please try some other username ")
            return redirect('signup')
        

        #if condition checking email id already exist then display the error message.
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email address already exist! Please try some other email address.")
            return redirect('signup')
        
        
        #if condition checking username already exist then display the error message.
        if password !=confirm_password:
            messages.info(request,"Password and confirm password didn't match !")
            return redirect('signup')

        else:

            #create the 'User' objects
            my_user=User.objects.create_user(username,email,password)

            my_user.first_name=first_name
            my_user.last_name=last_name
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')


#Create admin home page functions.
def admin_home(request):
    return render(request,'admin_home.html')
