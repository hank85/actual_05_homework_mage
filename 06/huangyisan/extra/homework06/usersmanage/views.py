from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, 'usersmanage/index.html')
'''
def usersinfo(request):
    user_context = {'messages':models.get_messages()}
    print(models.get_messages())
    return render(request,'usersmanage/usersinfo.html',user_context)
    '''
@csrf_exempt
def usersinfo(request):
    info = models.get_messages()
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
