from django import forms 
from .models import User
from django.core import validators

class Formdata(forms.ModelForm):
    def start_with_s(value):
        if value[0]!='s'.upper():
            raise forms.ValidationError('Name should start with s')
    name=forms.CharField(validators=[start_with_s])

    class Meta:
        model=User
        fields=['name', 'email','hobby','password']
        labels={'name':'Enter name', 'email':'Enter Email','hobby':'Enter hobbies','password':"Enter password"}
        help_texts={'name':'Enter your full name',}
        error_messages={'email':{'required':'Enter your email'}}
        widgets={'password':forms.PasswordInput}
