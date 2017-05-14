from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
# Create your views here.
def require_login(request):
    return render(request, 'user/login.html')

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(username,password)
    rt = models.validate_login(username, password)
    if rt:
        print(rt)
        return HttpResponseRedirect('/user/list_user/')
    else:
        print(rt)
        context = {'error':'用户名或密码错误','username':username,'password':password}
        return render(request,'user/login.html',context)

def list_user(request):
    action = request.POST.get('action','None')
    if action == 'add':
        return add_user(request)
    else:
        context = {'messages':models.get_messages()}
        print(context,type(context))
        print(models.get_messages(),type(models.get_messages()))
        return render(request, 'user/list.html',context)

def delete_user(request):
    name = request.GET.get('name','')
    models.delete_user(name)
    print(request.GET)
    print(name)
    return HttpResponseRedirect('/user/list_user/')

def edit_user(request):
    name = request.GET.get('name','')
    age = models.get_messages().get(name).get('age')
    tel = models.get_messages().get(name).get('tel')
    password = models.get_messages().get(name).get('password')
    print(name,age,tel,password)
    user_info = {"name":name,"age":age,"tel":tel,"password":password}
    return render(request,'user/edit.html',{'user_info':user_info})

def modify_user(request):
    name = request.POST.get('name','')
    age = request.POST.get('age','')
    tel = request.POST.get('tel','')
    password = request.POST.get('password','')
    print(name,age,tel,password)
    models.modify_user(name=name,age=age,tel=tel,password=password,users=models.get_messages())
    return HttpResponseRedirect('/user/list_user/')

def add_user(request):
    name = request.POST.get('name','')
    age = request.POST.get('age','')
    tel = request.POST.get('tel','')
    password = request.POST.get('password','')
    print(name,age,tel,password)
    if name in models.get_messages():
        print('exist')
        info_dict=models.get_messages()
        info_dict['error'] = '此用户已经存在'
        context={'messages':info_dict}
        return render(request,'user/list.html',context)
    else:
        print('not exist')
        models.modify_user(name=name,age=age,tel=tel,password=password,users=models.get_messages())
    return HttpResponseRedirect('/user/list_user/')
