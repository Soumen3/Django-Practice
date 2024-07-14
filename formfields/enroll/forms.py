from django import forms


class studentRegistration(forms.Form):
    name = forms.CharField(max_length=10, strip=False, label='Enter name', error_messages={
                           'required': 'Enter your name'})
    Roll = forms.IntegerField(label='Enter roll', max_value=10, min_value=5)
    Price = forms.DecimalField(max_value=1000, min_value=50, max_digits=4, decimal_places=1)
    Rate=forms.FloatField(max_value=10, min_value=5, widget=forms.TextInput(attrs={'placeholder':'Enter the rate'}))
    comment=forms.SlugField()
    Email=forms.EmailField(min_length=5, max_length=50)
    website=forms.URLField(min_length=5, max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)
    description=forms.CharField(widget=forms.Textarea)
    notes=forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))
    hidden=forms.CharField(widget=forms.HiddenInput, initial='hidden', required=False)
    agree = forms.BooleanField(label='I agree')
