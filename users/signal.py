from msilib.schema import InstallUISequence
import profile
from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from .models import User,Profiles
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


subject='Welcome to DevSearch'
message='Wae are glad you in heare!'
# @receiver(post_save,Profiles)
def createProfile(sender,instance,created,**kwargs):
    print('Profile signal triggered')
    if created:
        user=instance
        profile= Profiles.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
        send_mail(
            subject, 
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

    # print("profile update.......")
    # print("instance:",instance)
    # print("created:",created)
def updateProfile(sender,instance,created,**kwargs):
    profile = instance
    user=profile.user
    if created == False:
        user.first_user=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()


# @receiver(post_delete,Profiles)    
def deleteUser(sender,instance,**kwarags):
     print('instance:',str(instance) )
     print('user',str(instance.user))
     try:
        user=instance.user
        user.delete()
     except:
        pass

post_save.connect(createProfile,sender=User)
post_save.connect(updateProfile,sender=Profiles)
post_delete.connect(deleteUser,sender= Profiles)
     

