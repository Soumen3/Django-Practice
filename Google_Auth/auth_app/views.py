from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def logout_user(request):
	logout(request.user)
	return render(request,'index.html') # redirect to index.html template