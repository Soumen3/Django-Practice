from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.cache import cache

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
	
	ip = request.META['REMOTE_ADDR'] 
	print("IP Address:",ip)
	request.session['ip'] = ip

	#---------login count-----------
	cache.get_or_set('count',0, version=user.pk)
	new_count = cache.incr('count', 1, version=user.pk)
	cache.set('count',new_count, version=user.pk)