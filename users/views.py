from multiprocessing import context
from unicodedata import decomposition
from django.shortcuts import render
from .models import Profiles


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