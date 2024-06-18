from django.shortcuts import HttpResponse


class MyProcessMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		# One-time configuration and initialization.

	def __call__(self, request):
		response = self.get_response(request)
		return response
	
	def process_view(request, *agrs, **kwargs):
		print("This is Process View - Before View")
		# return None
		return HttpResponse("This is before Process View")

class MyExceptionMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		# One-time configuration and initialization.

	def __call__(self, request):
		response = self.get_response(request)
		return response
	
	def process_exception(self, request, exception):
		exception_name = exception.__class__.__name__
		print(f"Exception Type: {exception_name}")
		msg = f"Exception Occured: {exception}"
		return HttpResponse(msg)



class MyTemplateResponseMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		# One-time configuration and initialization.

	def __call__(self, request):
		response = self.get_response(request)
		return response
	
	def process_template_response(self, request, response):
		response.context_data['name'] = 'Modified Soumen'
		print("This is Process Template Response from Middleware")
		return response
