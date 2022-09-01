from lzma import is_check_supported
from django.forms import ModelForm
from django import forms
from  .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','featured_image',
                    'demo_link','source_link','tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }            
       # fields='__all__'
    def __init__(self,*args,**kwargs)   :
        super(ProjectForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items() :
            field.widget.attrs.update({'class':'input',})

        # self.fields['title'].widget.attrs.update(
        #     {'class':'input','placeholder':'Add Title Please'})
        # self.fields['description'].widget.attrs.update(
        #     {'class':'input','placeholder':'Add Description Please'}
        # )    
        # self.fields['demo_link'].widget.attrs.update(
        #     {'class':'input','placeholder':'Add demo link Please'}
        # )
        # self.fields['source_link'].widget.attrs.update(
        #     {'class':'input','placeholder':'Add source link Please'}
        # )
      
        
        


        