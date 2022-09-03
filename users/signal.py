import profile
from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from .models import User,Profiles
from django.dispatch import receiver

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
    # print("profile update.......")
    # print("instance:",instance)
    # print("created:",created)
# @receiver(post_delete,Profiles)    
def deleteUser(sender,instance,**kwarags):
     print('instance:',str(instance) )
     print('user',str(instance.user))
     user=instance.user
     user.delete()

post_save.connect(createProfile,sender=User)
post_delete.connect(deleteUser,sender= Profiles)
     

