from email import message
from multiprocessing import context
from ssl import _create_unverified_context
from unicodedata import decomposition
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profiles
from .forms  import CustomUserCreattionForm



def loginUser(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request,'UserName Does Not Exist...!')   
        user= authenticate(request,username=username,password=password)     
        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,"username Or password is incorrect")
          
    return render(request,'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request,"User was logged out!")
    return redirect('login')

def registerUser(request):
    page='register'
    form= CustomUserCreattionForm()
    if request.method =='POST':
        form=CustomUserCreattionForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            messages.success(request,"user account  was created!")
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,"An error has occurred during to registration")    


    context= {'page':page,'form':form}
    return render(request,'users/login_register.html',context)
    



def profiles(request):
    profiles= Profiles.objects.all()
    context={'profiles':profiles,}
    return render(request,'users/profiles.html', context)

def userProfile(request,pk):
    profile=Profiles.objects.get(id=pk)
    topskill= profile.skill_set.exclude(description__exact="")
    otherskills=profile.skill_set.filter(description="")
    context={'profile':profile,'topskill':topskill,'otherskills':otherskills}
    return render(request ,'users/user-profile.html',context)