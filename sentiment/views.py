from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mood.models import *

import json
import datetime
import time

def index(req):
# <<<<<<< HEAD
#    name = req.session.get('name',None)
#    if name is None:
#        return render(req, 'index.html')
    # return render(req, 'home.html')#, {'name':name})
# =======
    name = req.session.get('name',None)
    # print name
    if name is None:
        return render(req, 'index.html')
    return render(req, 'home.html', {'name':name})
# >>>>>>> 36a0105203a77594f7064d483c1024fb2013a2b5


def logout(req):
    if req.session.get('name',None):
        del req.session['name']
    return index(req)



def register(req):
    if req.is_ajax():
        print json.loads(req.body)
        try:
            u = User.objects.get(name=name)
        except User.DoesNotExist:
            # try:
            reguser = User(name=name, pwd=pwd)
            reguser.save()
            # req.session['name'] = name            
            return HttpResponse(0)
        return HttpResponse(1)



def login(req):    
    if req.is_ajax():
        uname = req.POST.get('name','')
        upwd = req.POST.get('pwd','')
        try:
            user = User.objects.get(name=uname,pwd=upwd)
        except User.DoesNotExist:
            return render(req, 'index.html')        
    return render(req, 'home.html', {'name': uname})


def user_mood(req):
    # pass
    # posts = None
    # posts = Post.objects.all()[0:8]
    return render(req, 'home.html')



def post_mood(req):
    if req.is_ajax():
        text = req.POST.get('text','')
        imgurl = req.POST.get('img', '')
        print text, len(imgurl)
        post = Post()
        return HttpResponse(0)
    return HttpResponse(1)




def axis(req):
    return render(req, 'axis.html', locals())


def test(req):
    if req.is_ajax():
        text = req.POST.get('text', None)
        print text
        return HttpResponse(text)
    else:
        return render(req, 'mood.html')