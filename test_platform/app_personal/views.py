from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_form(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        print('--->',username,password)
        if username=='' or password=='':
            return render(request,'login.html',{'info':'用户名或者密码为空'})
        if user:
            auth.login(request,user)
            return HttpResponseRedirect('/manage/')
        else:
            return HttpResponse('用户名或者密码错误')
    else:
        return render(request, 'login.html', {'info': '登录页面'})


@login_required
def manage(request):
    return render(request,'manage.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login_form')