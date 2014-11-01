from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mood.models import *
from snownlp import SnowNLP

import json
import datetime
import time
import sys


reload(sys)
sys.setdefaultencoding('utf8')

def index(req):
    name = req.session.get('name',None)
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
            req.session['username'] = uname
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
        req.session['username'] = uname
        return HttpResponse(0)
    else:
        return render(req, 'index.html', {'name': uname})


def user_mood(req):
    posts = Post.objects.all()
    evalues = [p.tmood for p in posts]
    username = req.session.get('username', 'Hackathon')
    return render(req, 'home.html', locals())



def post_mood(req):
    if req.is_ajax():
        text = req.POST.get('text','')
        imgurl = req.POST.get('img', '')
        imood = req.POST.get('emotion', 'normal')
        print text, len(imgurl)
        try:
            user = User.objects.get(name='a')
        except:
            user = User(name='a')
        tmood = SnowNLP(text).sentiments
        post = Post(img=imgurl,text=text,tmood=tmood,imood=imood,poster=user)
        # print post.img,post.text,post.imood,post.poster
        post.save()
        # return HttpResponse(0)
        posts = list(Post.objects.all())
        print 'posts',len(posts)
        return render(req, 'home.html', posts)
    return HttpResponse(1)




def axis(req):
    posts = Post.objects.all()[0:8]
    username = req.session.get('username', 'Hackathon')
    evalues = [p.tmood for p in posts]
    return render(req, 'axis.html', locals())


def test(req):
    if req.is_ajax():
        text = req.POST.get('text', None)
        print text
        return HttpResponse(text)
    else:
        return render(req, 'mood.html')