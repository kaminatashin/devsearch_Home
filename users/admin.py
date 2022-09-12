import profile
from django.contrib import admin
from .models import Profiles, Skill,Message

# Register your models here.
admin.site.register(Profiles)
admin.site.register(Skill)
admin.site.register(Message)
