from django.shortcuts import render


class underConstructionMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		if request.path == '/about/':
			return render (request, 'mysite/siteuc.html')
		return response