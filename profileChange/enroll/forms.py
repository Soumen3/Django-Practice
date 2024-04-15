from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class signUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}


class profileUpdateForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email', 'date_joined','last_login']
        labels={'email':'Email'}