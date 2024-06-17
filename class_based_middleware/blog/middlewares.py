
# def my_middleware(get_response):
# 	print("one time initialize")

# 	def my_function(request):
# 		print("This is before view")
# 		# print(request)
# 		response = get_response(request)
# 		# print(response)
# 		print("This is after view")
# 		return response
# 	return my_function


class MyMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		print("one time initialize")

	def __call__(self, request):
		print("This is before view")
		response = self.get_response(request)
		print("This is after view")
		return response