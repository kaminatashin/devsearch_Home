from multiprocessing import context
import re
from django.shortcuts import render,redirect  
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
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
    projects=Project.objects.all()
   # page="Project"
  #  number=11
  #  context={'page':page,'number':number,'projects':projectsList}
    context={'projects':projects}
   # return HttpResponse("here is our product")
    return render(request,'projects/projects.html',context)
    # return render(request,'main.html',context)

def project(request,pk):
 #   projectObj=None
 #   for i in projectsList:
 #      if i['id'] == pk :
 #          projectObj=i   
    projectObj=Project.objects.get(id=pk)
    tags=projectObj.tags.all()
    #return HttpResponse("Single Project"+" "+ str(pk)+"")
    return render(request,'projects/single-project.html',{'projectObj':projectObj,'tags':tags})

@login_required(login_url="login")    
def createProject(request):
    form=ProjectForm()
    if request.method == 'POST':
        #print(request.POST['title'])
        form=ProjectForm(request.POST,request.FILES) 
        if form.is_valid:
            form.save()  
            return redirect('projects')    
    context={'form':form}
    return render(request,'projects/project_form.html',context)
@login_required(login_url="login")  
def updateProject(request,pk):
    project=Project.objects.get(id=pk)
    form=ProjectForm(instance= project)
    if request.method== 'POST':
        form=ProjectForm(request.POST ,request.FILES ,instance=project)
        if form.is_valid:
            form.save()
            return redirect('projects')
    context={'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url="login")  
def deleteProject(request,pk):
    project=Project.objects.get(id=pk)
    context={'object':project}
    if request.method =='POST':
        project.delete()
        return redirect('projects')

    return render(request,'projects/delete_template.html',context)


# Create your views here.
