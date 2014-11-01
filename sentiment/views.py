from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mood.models import *

import json
import datetime
import time

def index(req):
    name = req.session.get('name',None)
    # print name
    if name is None:
        return render(req, 'index.html')
    return render(req, 'home.html', {'name':name})


def logout(req):
    if req.session.get('name',None):
        del req.session['name']
    return index(req)



def register(req):
    if req.is_ajax():
        print json.loads(req.body)
        ret = { 'state': 0 }
        try:
            u = User.objects.get(name=name)
        except User.DoesNotExist:
            # try:
            reguser = User(name=name, pwd=pwd)
            reguser.save()
            # req.session['name'] = name            
            return HttpResponse(ret)
        return HttpResponse(ret)



def login(req):    
        # name, pwd = parse_query(req)
    if req.method == 'POST':
        uname = req.POST.get('name','')
        
        return render(req, 'home.html', {'name': uname})
    return render(req, 'index.html')


def user_mood(req):
    posts = None
    # posts = Post.objects.all()[0:8]
    return render(req, 'home.html', {'posts':posts})



def post_mood(req):
    if req.method == 'POST':
        f = req.FILES.get['']




def axis(req):
    return render(req, 'axis.html', locals())