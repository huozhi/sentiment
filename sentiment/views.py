from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required

from apps.mood.models import *
from snownlp import SnowNLP

import json
import datetime
import time
import sys


reload(sys)
sys.setdefaultencoding('utf8')



@require_GET
# @login_required(redirect_field_name='/axis/')
def home(request):
    username = request.session.get('username', 'hehe')
    return render(request, 'home.html', { 'username': username })


def register(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        print 'reg', username, password
        try:
            reguser = User.objects.get(username=username)
        except User.DoesNotExist:
            reguser = User(username=username, password=password)
            reguser.save()
            request.session['username'] = username
            return HttpResponse(0)
        return HttpResponse(1)
    return render(request, 'index.html')


def login(requset):
    if requset.is_ajax():
        username = requset.POST.get('username')
        password = requset.POST.get('password')
        if username is None or password is None:
            return render(requset, 'index.html')
        print username, password
        try:
            user = User.objects.get(username=username,password=password)
        except User.DoesNotExist:
            return render(requset, 'index.html')
        requset.session['username'] = uname
        return HttpResponse(0)
    else:
        return render(requset, 'index.html', {'name': uname})


def user_mood(request):
    posts = list(Post.objects.all())
    # username = request.session.get('username', 'Hackathon')
    username = 'hehe'
    return render(request, 'home.html', locals())



@require_POST
def post_mood(request):
    if request.is_ajax():
        text = request.POST.get('text', None)
        imgurl = request.POST.get('img', None)
        imood = request.POST.get('emotion', 'normal')
        print text, len(imgurl)
        name = request.session.get('username')
        user = User.objects.get(username=name)
        
        tmood = SnowNLP(text).sentiments
        post = Post(img=imgurl, text=text, tmood=tmood, imood=imood, poster=user)
        # print post.img,post.text,post.imood,post.poster
        post.save()
        # return HttpResponse(0)
        posts = list(Post.objects.all())
        print 'posts',len(posts)
        return render(request, 'home.html', posts)
    return HttpResponse(1)




def axis(request):
    posts = Post.objects.all()
    username = request.session.get('username', 'Hackathon')
    evalues = [p.tmood for p in posts]
    return render(request, 'axis.html', locals())


def test(request):
    if request.is_ajax():
        text = request.POST.get('text', None)
        print text
        return HttpResponse(text)
    else:
        return render(request, 'mood.html')