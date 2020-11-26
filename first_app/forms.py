from django import forms
from .models import Program,Entity,UserProfileInfo


class ProgramForm(forms.ModelForm):

    class Meta:
        model = Program 
        fields = ('programe_name','no_of_people','place','description')
        Widgets = {
            'program_name':forms.TextInput(attrs={'class':'form-control'}),
            'no_of_people':forms.TextInput(attrs={'class':'form-control'}),
            'place'       :forms.TextInput(attrs={'class':'form-control'}),
            'description' :forms.TextInput(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
       
class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():   
        model = UserProfileInfo
        fields = ('name','email','password')

