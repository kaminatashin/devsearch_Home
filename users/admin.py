import profile
from django.contrib import admin
from .models import Profiles, Skill

# Register your models here.
admin.site.register(Profiles)
admin.site.register(Skill)
