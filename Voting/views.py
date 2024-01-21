from django.shortcuts import render,redirect
from .models import Candidate,Vote
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout

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


#Create login page functions.
def login(request):
    # if 'username' in request.session:
    #     return redirect(index)
    
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password1']
        user=authenticate(username=username,password=pass1)

        if user is not None:
            request.session['username']=username

            if user.is_superuser:
                return render(request,'admin_home.html')
            
            else:
                if user.is_staff==True:
                    return render(request,'user_home.html')
                else:
                    messages.info(request,"Your account not approved by the admin! Please wait.")
        
        else:
            messages.infor(request,"Invalid login credentials")
    return render(request,"login.html")

def signout(request):
    logout(request)
    # if 'username' in request.session:
    #     request.session.flush()
    return redirect('index')


#Create admin home page functions.
def admin_home(request):
    if 'username' in request.session:
        return render(request,'admin_home.html')
    return render(request,"login.html")

#Create admin view user details and approve button
def view_users(request):
    user=User.objects.filter(is_staff=False)
    return render(request,"view_users.html",{'user':user})


#Create admin approve login request for the users.
def approve(request,id):
    user=User.objects.get(id=id)
    user.is_staff=True
    user.save()
    return redirect("verified_users")

def verified_users(request):
    user=User.objects.filter(is_staff=True,is_superuser=False)
    return render(request,"verified_users.html",{'user':user})

def user_home(request):
    return render(request,"user_home.html")