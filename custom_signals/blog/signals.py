from django.dispatch import Signal, receiver

# Creating Signal 
notification = Signal()

# Creating a receiver function
@receiver(notification)
def show_notification(sender, **kwargs):
	print("Sender: ", sender)
	print("Kwargs: ", kwargs)