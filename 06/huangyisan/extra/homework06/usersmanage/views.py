from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from . import models
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, 'usersmanage/index.html')
@csrf_exempt
def usersinfo(request):
    info = models.get_messages()
    print(info)
    #user_context = {'messages':models.get_messages()}
    #print(models.get_messages())
    #return render(request,'usersmanage/usersinfo.html',{'messages':info})
    return render(request,'usersmanage/usersinfo.html',{'messages':info})

    #return render(request, 'usersmanage/usersinfo.html')
def home(request):
    return render(request, 'usersmanage/home.html')

def create(request):
    return render(request, 'usersmanage/create.html')

def delete(request):
    return render(request, 'usersmanage/delete.html')

def save_create(request):
    user_name = request.GET.get('name')
    user_age = request.GET.get('age','')
    user_telephone = request.GET.get('telephone','')
    print(user_name,user_age,user_telephone)
    models.save_message(user_name,user_age,user_telephone) 
    return HttpResponseRedirect('/usersmanage/usersinfo.html')

def save_delete(request):
    user_name = request.GET.get('name')
    user_age = request.GET.get('age','')
    user_telephone = request.GET.get('telephone','')
    print(user_name,user_age,user_telephone)
    models.del_message(user_name,user_age,user_telephone) 
    return HttpResponseRedirect('/usersmanage/usersinfo.html')
