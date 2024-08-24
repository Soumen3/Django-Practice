from django.shortcuts import render
from django.views import View
from django. http import HttpResponse

# Create your views here.
class MyView(View):
    name = "Soumen"
    def get(self, request):
        return HttpResponse(f"<h1>Class Based View</h1> {self.name}")

class MyChildView(MyView):
    def get(self, request):
        return HttpResponse(f"<h1>Class Based Child View</h1> {self.name}")