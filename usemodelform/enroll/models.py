from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70, blank=True,)
    # email=models.EmailField(max_length=254, verbose_name='enter email')
    email=models.EmailField(max_length=254)
    hobby=models.TextField(max_length=1000,)
    password=models.CharField(max_length=700, help_text='enter password')
