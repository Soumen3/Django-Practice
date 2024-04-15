from django import forms 


class Registration(forms.Form):

    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    re_password=forms.CharField(label='Re-Enter Password',widget=forms.PasswordInput)


    def clean(self):
        self.cleaned_data=super().clean()
        valpwd=self.cleaned_data['password']
        rvalpwd=self.cleaned_data['re_password']
        
        if valpwd!=rvalpwd:
            raise forms.ValidationError('Password does not match')
