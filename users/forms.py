from cProfile import label
from dataclasses import fields
from inspect import classify_class_attrs
from pyexpat import model
from tkinter.ttk import LabeledScale
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreattionForm(UserCreationForm):
    class Meta():
        model=User
        fields=['first_name','email','username','password1','password2']
        labels ={
            'first_name':'Name',
        }
