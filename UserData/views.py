# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random
# Create your views here.
#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail
from django import forms
from models import User
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login

#表单
class UserForm(forms.Form):
    Email = forms.EmailField(label='Email',max_length=255)
    ID = forms.IntegerField(label='ID')


#注册
def register(req):
    return render_to_response('pages/register.html')


def register_update(req):
    if req.method == 'POST':
            #获得表单数据
            email = req.POST.get('Email')
            uid = random.randint(1,100)
            while User.objects.filter(email=email,UID=uid).exists():
                uid = random.randint(1, 100)
            #添加到数据库
            User.objects.create(email=email, UID=uid,FPList='')
            send_mail("Hi there",'Your ID number is:  '+str(uid), "xzthemeofsss@gmail.com", [email])
            j = {'email':email,'UID':uid}
            req.session['email'] = email
            req.session['id'] = uid
            req.session['isLogin'] = True
            return HttpResponse(json.dumps(j))
#登陆
def login(req):
    if 'email' in req.session.keys():
        return HttpResponseRedirect('/fingerprint')
    else:
        return HttpResponseRedirect('/register')

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response