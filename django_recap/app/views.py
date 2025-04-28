from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from icecream import ic
from .models import MyModel, RelatedModel
from .forms import MyModelForm

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Default Name')
        password = request.POST.get('password', 'Default Password')
        return render(request, 'Home.html', {'name': name, 'password': password})
    return render(request, 'Home.html')

def create_or_update_model(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Default Name')
        obj, created = MyModel.objects.update_or_create(name=name)
        message = f"Instance {'created' if created else 'updated'}: {obj.name}"
        return HttpResponse(message)
    return HttpResponse("Send a POST request to create or update a model instance.")

def mymodel_form_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return HttpResponse(f"Form submitted successfully! Created instance: {instance.name}")
    else:
        form = MyModelForm()
    return render(request, 'mymodel_form.html', {'form': form})

def select_related_example(request):
    # Fetch MyModel instances with related RelatedModel using select_related
    queryset = MyModel.objects.select_related('related_model').all()
    data = [
        f"MyModel: {obj.name}, RelatedModel: {obj.related_model.name}"
        for obj in queryset
    ]
    return HttpResponse("<br>".join(data))

def prefetch_related_example(request):
    # Fetch MyModel instances with related RelatedModel using prefetch_related
    queryset = MyModel.objects.prefetch_related('related_model_set').all()
    data = [
        f"MyModel: {obj.name}, RelatedModels: {[related.name for related in obj.related_model_set.all()]}"
        for obj in queryset
    ]
    return HttpResponse("<br>".join(data))