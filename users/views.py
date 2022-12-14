from email import message
from encodings import search_function
from http.client import HTTPResponse
from multiprocessing import context
from ssl import _create_unverified_context
from tkinter.messagebox import NO
from unicodedata import decomposition
from unittest import skip
from wsgiref.util import request_uri
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profiles ,Message
from .forms  import CustomUserCreattionForm, profileForm,SkillForm,MessageForm
from .utils import  searchProfiles,paginatProfiles



def loginUser(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method =='POST':
        username=request.POST['username'].lower()
        password=request.POST['password']
        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request,'UserName Does Not Exist...!')   
        user= authenticate(request,username=username,password=password)     
        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
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
            return redirect('edit-account')
        else:
            messages.error(request,"An error has occurred during to registration")    


    context= {'page':page,'form':form}
    return render(request,'users/login_register.html',context)
    



def profiles(request):
    profiles,search_query=searchProfiles(request)
    custom_range,profiles=paginatProfiles(request,profiles,3)

    context={'profiles':profiles,'search_query':search_query,'custom_range':custom_range}
    return render(request,'users/profiles.html', context)

def userProfile(request,pk):
    profile=Profiles.objects.get(id=pk)
    topskill= profile.skill_set.exclude(description__exact="")
    otherskills=profile.skill_set.filter(description="")
    context={'profile':profile,'topskill':topskill,'otherskills':otherskills}
    return render(request ,'users/user-profile.html',context)

@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profiles
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request,'users/account.html',context)

@login_required(login_url='login')
def editAccount(request):
    profile=request.user.profiles
    form=profileForm(instance=profile)
    if request.method =='POST':
        form=profileForm(request.POST, request.FILES ,instance=profile)
        if form.is_valid:
            form.save()
            return redirect('account')
    context={'form':form}
    return render(request,'users/profile_form.html',context)

@login_required(login_url='login')
def createSkill(request):
    #owner detect
    profile=request.user.profiles
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully!')
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)

@login_required(login_url='login')
def updateSkill(request,pk):
    profile=request.user.profiles
    skill= profile.skill_set.get(id=pk)
    form=SkillForm(instance=skill)
    if request.method=='POST':
        form=SkillForm(request.POST,instance=skill)
        if form.is_valid:
            form.save()
            messages.success(request,"skill was updated successfully!")
            return redirect('account')
    context={'form':form}
    return render(request,'users/skill_form.html',context)

def deleteSkill(request,pk):
    profile=request.user.profiles
    skill=profile.skill_set.get(id=pk)
    if request.method== 'POST':
        skill.delete()
        messages.success(request,"skill  was deleted successfully!")
        return redirect('account')

    context={'object':skill}
    return render(request,'delete_template.html',context)

@login_required(login_url='login')
def inbox(request):
    profile=request.user.profiles
    messageRequest=profile.messages.all()
    un_readCount=messageRequest.filter(is_read=False).count()
    context={'messageRequest':messageRequest,'un_readCount':un_readCount}
    return render(request,'users/inbox.html',context)
@login_required(login_url='login')
def viewMessage(request,pk):
    profile=request.user.profiles
    message=profile.messages.get(id=pk)    
    if message.is_read==False:
        message.is_read=True
        message.save()
    context={'message':message}
    return render(request,'users/message.html',context)

def createMessage(request,pk):
    recipient=Profiles.objects.get(id=pk) 
    form=MessageForm()
    try:
        sender=request.user.profile
    except:
        sender=None
    if request.method=='POST' :
        form=MessageForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.sender=sender
            message.recipient=recipient
            if sender:
                message.name=sender.name
                message.email=sender.email
            message.save()    
            messages.success(request,'Your message was successfully send!')
            return redirect('user-profile',pk=recipient.id)


    context={'recipient':recipient,'form':form}
    return render(request,'users/message_form.html',context)
