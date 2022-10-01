from urllib import response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from project.models import Project,Tag
from users.models import Profiles

from api import serializers

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {'GET':'/api/projects'},
        {'GET':'api/projects/id'},
        {'POST':'/api/projects/id/vote'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},

    ]
    # return JsonResponse(routes,safe=False)
    return Response(routes)

@api_view(['GET'])
def getProjects(resquest):
    projects=Project.objects.all()
    serializer=ProjectSerializer(projects,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request,pk):
    project=Project.objects.get(id=pk)
    serializer=ProjectSerializer(project,many=False)
    return Response(serializer.data)