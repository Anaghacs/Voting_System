from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'base.html')

#Create admin home page functions.
def admin_home(request):
    return render(request,'admin_home.html')