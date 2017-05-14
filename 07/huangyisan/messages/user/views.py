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
    #add功能再list页面展现，所以需要知道当时具体是什么行为，action=add为add功能按钮所致
    if action == 'add':
        #直接递交给add_user(request)函数，并且返回，让add_user(request)函数判断后进行传递其HttpResponse
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
    age = int(age)
    tel = request.POST.get('tel','')
    password = request.POST.get('password','')
    if name in models.get_messages():
        print('exist')
        info_dict=models.get_messages()
        #当添加一个已经存在的用户的时候，添加一个error的key和对应的'此用户已经存在'的值给原字典，一起传递给list.html进行渲染。
        #因为单纯的渲染error不够，所以和数据需要一起传递。
        info_dict['error'] = '此用户已经存在'
        context={'messages':info_dict}
        #因为add行为在list.html。所以这里直接request了list.html。如果独立出一个界面再重定向回list.html会有问题。当出现error的时候，会因为重定向导致渲染丢失。
        #总之这里我是强行要把add和list写同个界面了。。应该有更好的处理方法,来解决重定向后渲染丢失问题。
        return render(request,'user/list.html',context)
    if age < 0 or age > 150:
        return handle_error(request,'这年龄很诡异，添加信息失败')
    if len(tel) != 11:
        return handle_error(request,'这手机号码很诡异，添加信息失败')
    if len(password) < 6:
        return handle_error(request,'密码设置过于简单，请重新设置')
    else:
        models.modify_user(name=name,age=age,tel=tel,password=password,users=models.get_messages())
    return HttpResponseRedirect('/user/list_user/')

def handle_error(request,error_message):
    info_dict=models.get_messages()
    info_dict['error'] = error_message
    context={'messages':info_dict}
    return render(request,'user/list.html',context)
