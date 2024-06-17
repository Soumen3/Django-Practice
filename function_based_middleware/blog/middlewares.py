
def my_middleware(get_response):
	print("one time initialoze")

	def my_function(request):
		print("This is before view")
		# print(request)
		response = get_response(request)
		# print(response)
		print("This is after view")
		return response
	return my_function