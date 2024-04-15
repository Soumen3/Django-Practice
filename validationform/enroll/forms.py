from django import forms
from django.core import validators


# def starts_with_s(value):
#     if value[0]!='s':
#         raise forms.ValidationError('Name should start with "s"')
    


class studentRegistration(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    # name = forms.CharField(validators=[starts_with_s])

    
    name = forms.CharField()
    Email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean_name(self):
    #     valname = self.cleaned_data['name']

    #     if len(valname) < 4:
    #         raise forms.ValidationError('Enter more than or equal 4')
    #     return valname


    