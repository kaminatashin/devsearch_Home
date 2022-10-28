from urllib import response
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from project.models import Project,Tag,Review
from users.models import Profiles

from api import serializers

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRoutes(request):
    print('USER:',request.user)
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
    project=Project.objects.get(id=pk)
    user=request.user.profiles
    data=request.data
    review,created=Review.objects.get_or_create(
        owner=user,
        project=project,
    )
    review.value=data['value']
    review.save()
    project.getVoteCount
    print('data:',data)
    serializer=ProjectSerializer(project,many=False)
    return Response(serializer.data)