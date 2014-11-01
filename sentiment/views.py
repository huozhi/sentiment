from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mood.models import *
from snownlp import SnowNLP

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
        uname = req.POST.get('name','')
        upwd = req.POST.get('pwd','')
        print 'reg',uname,upwd
        try:
            reguser = User.objects.get(name=uname)
        except User.DoesNotExist:
            reguser = User(name=uname, pwd=upwd)
            reguser.save()
            return HttpResponse(0)
        return HttpResponse(1)
    return render(req, 'index.html')


def login(req):    
    if req.is_ajax():
        uname = req.POST.get('name',None)
        upwd = req.POST.get('pwd',None)
        if uname is None or upwd is None:
            return render(req, 'index.html')
        print uname, upwd
        try:
            user = User.objects.get(name=uname,pwd=upwd)
        except User.DoesNotExist:
            return render(req, 'index.html')
        return HttpResponse(0)
    else:
        return render(req, 'index.html', {'name': uname})


def user_mood(req):
    # pass
    # posts = None
    # posts = Post.objects.all()[0:8]
    return render(req, 'home.html')



def post_mood(req):
    if req.is_ajax():
        text = req.POST.get('text','')
        imgurl = req.POST.get('img', '')
        imood = req.POST.get('emotion', 'normal')
        print text, len(imgurl)
        # user = None
        try:
            user = User.objects.get(name='a')
            print 'get', user
        except:
            user = User(name='a')
            # user.save()
            print user
            # return HttpResponse(1)
        print user.name,user.pwd
        # user.save()
        post = Post(img=imgurl,text=text,imood=imood,poster=user)
        # print post.img,post.text,post.imood,post.poster
        post.save()
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