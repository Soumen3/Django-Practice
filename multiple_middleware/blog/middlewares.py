from django.shortcuts import HttpResponse

class FirstMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		print("one time first middleware initialize")

	def __call__(self, request):
		print("This is First Middleware before view")
		response = self.get_response(request)
		print("This is First Middleware after view")
		return response

class SecondMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		print("one time second middleware initialize")

	def __call__(self, request):
		print("This is Second Middleware before view")
		if 1==1:
			response =  HttpResponse("Chup chap patli gali se nikl lo. ") # if this is executed, then the view function will not be executed. and the response will be returned from here.
		else:
			response = self.get_response(request)
		print("This is Second Middleware after view")
		return response
	
class ThirdMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		print("one time Third middleware initialize")

	def __call__(self, request):
		print("This is Third Middleware before view")
		response = self.get_response(request)
		print("This is Third Middleware after view")
		return response