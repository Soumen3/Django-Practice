from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def mymodel_post_save_handler(sender, instance, created, **kwargs):
    if created:
        print(f"A new instance of MyModel was created: {instance.name}")
    else:
        print(f"An instance of MyModel was updated: {instance.name}")
