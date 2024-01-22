from django.shortcuts import render,redirect,get_object_or_404
from .models import Candidate,Votes
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
    if request.method == "POST":
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
        
        #username , firstname ,lastname  validation.
        if username==first_name==last_name== "" or username==first_name==last_name==" ":
            messages.info(request,"Username or firstname and last name is not allowed space and blank space and number and numbers and special characters")
            return redirect('signup')

        #if condition checking username already exist then display the error message.
        if password !=confirm_password:
            messages.info(request,"Please enter same Password and confirm password didn't match !")
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

        # if user := authenticate(username=username,password=password):
        if user is not None:
            request.session['username']=username

            if user.is_superuser:
                # print("--------------------------------------------")
                return redirect(admin_home)
            
            else:
                if user.is_staff==True:
                    return redirect(user_home)
                else:
                    messages.info(request,"Your account not approved by the admin! Please wait.")
        
        else:
            messages.info(request,"Invalid username or password ! Please check username or password")
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

def candidate_form(request):

    if request.method=="POST":
        fullname=request.POST['fullname']
        email=request.POST['email']
        phone=request.POST['phone']
        bio=request.POST['bio']
        candidates=Candidate.objects.create(fullname=fullname,email=email,phone=phone,bio=bio)
        candidates.save()   
    return render(request,'candidate_form.html')


def admin_candidate_view(request):
    candidates=Candidate.objects.all()
    return render(request,'admin_candidate_view.html',{'candidates':candidates})

def delete_candidate_invoice(request,id):
    candidate=Candidate.objects.get(id=id)

    #Create confirmation message for deletion page. 
    if request.method == "POST":
        candidate.delete()
        return redirect('admin_candidate_view')
    return render(request,"delete_candidate_invoice.html")


def user_home(request):
    return render(request,"user_home.html")

def user_view_candidate(request):
    candidates=Candidate.objects.all()
    return render(request,'user_view_candidate.html',{'candidates':candidates})


# def vote(request,candidate_id):
#     candidate=get_object_or_404(Candidate,pk=candidate_id)
#     if Votes.objects.filter(user=request.User,candidate=candidate).exists():
#         return render(request,'already voted')
#     vote=Votes(user=request.User,candidate=candidate)
#     vote.save()
#     return render(request,'voting_success')

def vote(request,candidate_id):
    if request.user.is_authenticated:
        cart=Votes.objects.filter(user=request.user)
        count=0
        for i in cart:
            