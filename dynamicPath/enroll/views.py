from django.shortcuts import render

# Create your views here.
def show_home(request):
    return render(request, 'enroll/home.html')

def show_details(request, my_id):
    context={}
    context['id']=my_id
    return render (request, 'enroll/page.html', context)


def show_details(request, my_id, my_subid):
    context={}
    if my_subid==14:
        context['id']=my_id
        context['sub_id']=my_subid
        context['name']="rohan"
    if my_subid==15:
        context['id']=my_id
        context['sub_id']=my_subid
        context['name']="soman"
    if my_subid==16:
        context['id']=my_id
        context['sub_id']=my_subid
        context['name']="puja"
    if my_subid==17:
        context['id']=my_id
        context['sub_id']=my_subid
        context['name']="janeliya"
    
    return render (request, 'enroll/page.html', context)