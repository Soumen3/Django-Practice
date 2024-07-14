from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, post_save, pre_delete, post_delete, post_init, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
	print("-----------------")
	print("Logged in Signal.....  Run Intro.....")
	print("Sender: ", sender)
	print("Request: ", request)
	print("User: ", user)
	print("Kwargs: ", kwargs)

# user_logged_in.connect(login_success, sender=User)   # This is another way to connect signal

@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
	print("-----------------")
	print("Logged out Signal.....  ")
	print("Sender: ", sender)
	print("Request: ", request)
	print("User: ", user)
	print("Kwargs: ", kwargs)

# user_logged_out.connect(logout_success, sender=User)  # This is another way to connect signal

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
	print("-----------------")
	print("Login Failed Signal.....  ")
	print("Sender: ", sender)
	print("Credentials: ", credentials)
	print("Request: ", request)
	print("Kwargs: ", kwargs)

# user_login_failed.connect(login_failed)  # This is another way to connect signal



@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
	print("-----------------")
	print("Pre Save Signal.....")
	print("Sender: ", sender)
	print("Instance: ", instance)
	print("Kwargs: ", kwargs)

# pre_save.connect(at_beginning_save, sender=User)  # This is another way to connect signal

@receiver(post_save, sender=User)
def at_end_save(sender, instance, created, **kwargs):
	if created:
		print("-----------------")
		print("New User Created.....")
		print("Post Save Signal.....")
		print("Sender: ", sender)
		print("Instance: ", instance)
		print("Created: ", created)
		print("Kwargs: ", kwargs)
	else:
		print("-----------------")
		print("User Updated.....")
		print("Post Save Signal.....")
		print("Sender: ", sender)
		print("Instance: ", instance)
		print("Created: ", created)
		print("Kwargs: ", kwargs)

# post_save.connect(at_end_save, sender=User)  # This is another way to connect signal

@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
	print("-----------------")
	print("Pre Delete Signal.....")
	print("Sender: ", sender)
	print("Instance: ", instance)
	print("Kwargs: ", kwargs)

# pre_delete.connect(at_beginning_delete, sender=User)  # This is another way to connect signal

@receiver(post_delete, sender=User)
def at_end_delete(sender, instance, **kwargs):
	print("-----------------")
	print("Post Delete Signal.....")
	print("Sender: ", sender)
	print("Instance: ", instance)
	print("Kwargs: ", kwargs)

# post_delete.connect(at_end_delete, sender=User)  # This is another way to connect signal

@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
	print("-----------------")
	print("Pre Init Signal.....")
	print("Sender: ", sender)
	print("Args: ", args)
	print("Kwargs: ", kwargs)

# pre_init.connect(at_beginning_init, sender=User)  # This is another way to connect signal

@receiver(post_init, sender=User)
def at_end_init(sender, instance, *args, **kwargs):
	print("-----------------")
	print("Post Init Signal.....")
	print("Sender: ", sender)
	print("Instance: ", instance)
	print("Args: ", args)
	print("Kwargs: ", kwargs)

# post_init.connect(at_end_init, sender=User)  # This is another way to connect signal

@receiver(pre_migrate)
def at_beginning_migrate(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
	print("-----------------")
	print("Pre Migrate Signal.....")
	print("Sender: ", sender)
	print("App Config: ", app_config)
	print("Verbosity: ", verbosity)
	print("Interactive: ", interactive)
	print("Using: ", using)
	print("Plan: ", plan)
	print("Apps: ", apps)
	print("Kwargs: ", kwargs)

# pre_migrate.connect(at_beginning_migrate)  # This is another way to connect signal

@receiver(post_migrate)
def at_end_migrate(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
	print("-----------------")
	print("Post Migrate Signal.....")
	print("Sender: ", sender)
	print("App Config: ", app_config)
	print("Verbosity: ", verbosity)
	print("Interactive: ", interactive)
	print("Using: ", using)
	print("Plan: ", plan)
	print("Apps: ", apps)
	print("Kwargs: ", kwargs)

# post_migrate.connect(at_end_migrate)  # This is another way to connect signal

@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
	print("-----------------")
	print("Request Started Signal.....")
	print("Sender: ", sender)
	print("Environ: ", environ)
	print("Kwargs: ", kwargs)

# request_started.connect(at_beginning_request)  # This is another way to connect signal

@receiver(request_finished)
def at_end_request(sender, **kwargs):
	print("-----------------")
	print("Request Finished Signal.....")
	print("Sender: ", sender)
	print("Kwargs: ", kwargs)

# request_finished.connect(at_end_request)  # This is another way to connect signal

@receiver(got_request_exception)
def at_exception_request(sender, request, **kwargs):
	print("-----------------")
	print("Got Request Exception Signal.....")
	print("Sender: ", sender)
	print("Request: ", request)
	print("Kwargs: ", kwargs)

# got_request_exception.connect(at_exception_request)  # This is another way to connect signal

@receiver(connection_created)
def at_db_connection_created(sender, connection, **kwargs):
	print("-----------------")
	print("Connection Created Signal.....")
	print("Sender: ", sender)
	print("Connection: ", connection)
	print("Kwargs: ", kwargs)

# connection_created.connect(at_db_connection_created)  # This is another way to connect signal