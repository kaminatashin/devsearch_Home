from multiprocessing import context
import re
from unittest import result
from django.shortcuts import render,redirect  
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from project.utils import searchProject
from .models import Project,Tag
from .forms import ProjectForm ,ReviewForm
from django.contrib import messages
from .utils  import searchProject,paginatProject
from django.contrib.auth.decorators import login_required


# projectsList = [
#     {
#         'id': '1',
#         'title': 'Ecommerce Website',
#         'description': 'Fully functional ecommerce website'
#     },
#     {
#         'id': '2',
#         'title': 'Portfolio Website',
#         'description': 'A personal website to write articles and display work'
#     },
#     {
#         'id': '3',
#         'title': 'Social Network',
#         'description': 'An open source project built by the community'
#     }
# ]

def projects(request):
    projects,search_query=searchProject(request)
    # page="Project"
  #  number=11
  #  context={'page':page,'number':number,'projects':projectsList}
    custom_range,projects=paginatProject(request,projects,6)
    context={'projects':projects,'search_query':search_query,'custom_range':custom_range}
   # return HttpResponse("here is our product")
    return render(request,'projects/projects.html',context)
    # return render(request,'main.html',context)

def project(request,pk):
 #   projectObj=None
 #   for i in projectsList:
 #      if i['id'] == pk :
 #          projectObj=i   
    projectObj=Project.objects.get(id=pk)
    form=ReviewForm()
    if request.method == 'POST':
        form=ReviewForm(request.POST)
        review=form.save(commit=False)
        review.project=projectObj
        review.owner=request.user.profiles
        review.save()
        projectObj.getVoteCount
        messages.success(request,'tank you ,your review was successfully submitted ')
        return redirect('project',pk=projectObj.id)
       
    tags=projectObj.tags.all()
    #return HttpResponse("Single Project"+" "+ str(pk)+"")
    return render(request,'projects/single-project.html',{'projectObj':projectObj,
                    'tags':tags,'form':form}
                )


@login_required(login_url="login")    
def createProject(request):
    profile=request.user.profiles
    form=ProjectForm()
    if request.method == 'POST':
        newTags=request.POST.get('newTags').replace(',',  " ").split()

        #print(request.POST['title'])
        form=ProjectForm(request.POST,request.FILES) 
        if form.is_valid:
            project=form.save(commit=False) 
            project.owner=profile
            project.save()
            for tag in newTags:
               tag,created= Tag.objects.get_or_create(name=tag)
               project.tags.add(tag)
            return redirect('projects')    
    context={'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url="login")  
def updateProject(request,pk):
    profile=request.user.profiles
    project=profile.project_set.get(id=pk)
    form=ProjectForm(instance= project)
    if request.method== 'POST':
        newTags=request.POST.get('newTags').replace(',',  " ").split()
        form=ProjectForm(request.POST ,request.FILES ,instance=project)
        if form.is_valid:
            project=form.save()
            for tag in newTags:
                tag,created= Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            # return redirect('projects')
            return redirect('account')
    context={'form':form, 'project':project}
    return render(request,'projects/project_form.html',context)

@login_required(login_url="login")  
def deleteProject(request,pk):
    profile=request.user.profiles
    project=profile.project_set.get(id=pk)
    context={'object':project}
    if request.method =='POST':
        project.delete()
        return redirect('projects')

    return render(request,'delete_template.html',context)


# Create your views here.
