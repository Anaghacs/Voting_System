from django.shortcuts import render,redirect,get_object_or_404
from .models import Candidate,Votes
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.db.models import Count
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login


# Create your views here.
def index(request):
    return render(request,'base.html')

#The user registration or signup form for the user.
@never_cache
def signup(request):

    #The form submition field daata fetch
    if request.method == "POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password1']
        confirm_password=request.POST['password2']

         #username , firstname ,lastname  validation.
        if username==first_name==last_name==email==password==confirm_password=="" or username==first_name==last_name==email==password==confirm_password==" ":
            messages.info(request,"Username or firstname and last name is not allowed space and blank space and number and numbers and special characters")
            return redirect('signup')

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


#Create login page functions admin login and user login.
# @never_cache
def user_login(request):
    
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password1']
        user=authenticate(username=username,password=pass1)

        # user = request.user
        print("======",user)
        # if user := authenticate(username=username,password=password):
        if user is not None:
            auth_login(request, user)
            
            if user.is_superuser:
            # print("--------------------------------------------")
                request.session['username']=username
                return redirect(admin_home)
            
            else:
                
                if user.is_staff==True:
                    return redirect(user_home)
                else:
                    messages.info(request,"Your account not approved by the admin! Please wait.")
        else:
            messages.info(request,"Invalid username or password ! Please check username or password not alowed blank space.")
    return render(request,"login.html")

@never_cache
@login_required
def signout(request):
    logout(request)
    # if 'username' in request.session:
    #     request.session.flush()
    return redirect('index')


#Create admin home page functions.
@never_cache
@login_required
def admin_home(request):
    if 'username' in request.session:
        return render(request,'admin_home.html')
    return render(request,"login.html")

#Create admin view user details and approve button
@never_cache
@login_required
def view_users(request):
    user=User.objects.filter(is_staff=False)
    return render(request,"view_users.html",{'user':user})


#Create admin approve login request for the users.
@never_cache
@login_required
def approve(request,id):
    user=User.objects.get(id=id)
    user.is_staff=True
    user.save()
    return redirect("verified_users")

#Crete admin approved users details.
@never_cache
@login_required
def verified_users(request):
    user=User.objects.filter(is_staff=True,is_superuser=False)
    return render(request,"verified_users.html",{'user':user})


#Admin create candidate details add.
@never_cache
@login_required
def candidate_form(request):

    if request.method=="POST":
        fullname=request.POST['fullname']
        email=request.POST['email']
        phone=request.POST['phone']
        bio=request.POST['bio']
        photo=request.POST['photo']
        candidates=Candidate.objects.create(fullname=fullname,email=email,phone=phone,bio=bio,photo=photo)
        candidates.save()   
    return render(request,'candidate_form.html')

def update(request,id):
    candidate=Candidate.objects.get(id=id)
    return render(request,'updates.html',{'candidate':candidate})

def updates(request,id):
    fullname=request.POST['fullname']
    email=request.POST['email']
    phone=request.POST['phone']
    bio=request.POST['bio']
    photo=request.POST['photo']
    candidate=Candidate.objects.get(id=id)
    candidate.fullname=fullname
    candidate.email=email
    candidate.phone=phone
    candidate.bio=bio
    candidate.photo=photo
    candidate.save()
    return redirect("/")

#Admin view candidate details
@never_cache
@login_required
def admin_candidate_view(request):
    candidates=Candidate.objects.all()
    return render(request,'admin_candidate_view.html',{'candidates':candidates})

#admin delete candidate details using and create confirmation box.
@never_cache
@login_required
def delete_candidate_invoice(request,id):
    candidate=Candidate.objects.get(id=id)

    #Create confirmation message for deletion page. 
    if request.method == "POST":
        candidate.delete()
        return redirect('admin_candidate_view')
    return render(request,"delete_candidate_invoice.html")

#create voting table access candidate name and user name.
@never_cache
@login_required
def vote(request,id):
    
    print("-------------in function-----------------------------------")
    user = request.user
    print(user.username)
    candidate=Candidate.objects.get(id=id)
    print(candidate.fullname)

    #check user is already voted or not.voted then print the msg. 
    if Votes.objects.filter(user = user).exists():
        messages.info(request,"User is already voted! Only one times voting for users")
        return redirect('user_view_candidate')
    
    #else vote the user for specific candidate 
    if request.method == "POST":
        voting=Votes.objects.create(user=user,candidate=candidate)
        voting.save()
        return render(request,'successfull_msg.html')
    return render(request,"user_voting_invoice.html")

#Voting successfully completed sendby the user successfullmessage
@never_cache
@login_required
def successfull_msg(request):
    return render(request,'successfull_msg.html')

#Crete user_home view
@never_cache
@login_required
def user_home(request):
    user = request.user
    return render(request,"user_home.html",{"user":user})


#view candidate details in user
@never_cache
@login_required
def user_view_candidate(request):
    candidates=Candidate.objects.all()
    return render(request,'user_view_candidate.html',{'candidates':candidates})

#count the highest voting count
@never_cache
@login_required
def win_vote(request):
    
    max_votes_candidate = Candidate.objects.annotate(num_votes=Count('votes')).order_by('-num_votes').first()
    
    context = {'max_votes_candidate': max_votes_candidate}
#     candidates_with_vote_count = Candidate.objects.annotate(vote_count=Count('votes'))
#      for candidate in candidates_with_vote_count:
#         print(f"{candidate.fullname} has {candidate.vote_count} votes.")
#      print(candidates_with_vote_count())
    return render(request,"win_vote.html",context)

    