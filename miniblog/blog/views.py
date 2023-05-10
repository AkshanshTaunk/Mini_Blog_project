from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .forms import signupform, loginform
from django.contrib.auth import authenticate,login,logout
from .models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def dashboard(request):
    return render(request,'blog/dashboard.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect ('/')

def user_signup(request):
    if request.method =="POST":
        fm = signupform(request.POST)
        if fm.is_valid():
            messages.success(request,'Congratulation!! You have become an Author')
            fm.save()
    else:
        fm = signupform()
    return render(request,'blog/signup.html',{'form':fm})

def user_login(request):
    if request.method == 'POST':
        fm=loginform(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upassword = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upassword)
            if user is not None:
                login(request, user)
                messages.success(request,'Logged in successfully')
                return HttpResponseRedirect('/dashboard/')
    else:
        fm = loginform()
    return render(request,'blog/login.html',{'form':fm})
    