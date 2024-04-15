from django import forms 

class UserDetails(forms.Form):
    name=forms.CharField(max_length=30, min_length=2)
    email=forms.EmailField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)