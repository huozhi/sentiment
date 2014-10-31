from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mood.models import User, Post, Comment

import json
import datetime
import time

def index(req):
    name = req.session.get('name',None)
    if name is None:
        return render(req, 'index.html')
    return render(req, 'home.html', {'name':name})


def logout(req):
    if req.session.get('name',None):
        del req.session['name']
    return index(req)


def jsonf(data):
    return json.dumps(data)


def parse_query(req):
    query = json.loads(req.body)
    name = query.get('name')
    pwd = query.get('pwd')
    if name and pwd:
        return name,pwd
    return None


@csrf_exempt
def register(req):
    name, pwd = parse_query(req)
    if User.objects.get(name=name) is not None:
        return HttpResponse(jsonf(1))
    reguser = User(name=name, pwd=pwd)
    try:
        reguser.save()
        req.session['name'] = name
        return HttpResponse(jsonf(0))
    except Exception:
        return HttpResponse(jsonf(1))


@csrf_exempt
def login(req):
    if req.method == 'GET':
        return index(req)
    name, pwd = parse_query(req)
    try:
        user = User.objects.get(name=name, pwd=pwd)
        req.session['name'] = name
        return HttpResponse(jsonf(0))
    except User.DoesNotExist:
        return HttpResponse(jsonf(1))


def user_mood(req):
    name = req.session.get('name','')
    if name is None:
        return index(req)
    query = json.loads(req.body)
    seconds = json.loads('date')
    fts = datetime.datetime.fromtimestamp
    curdate = fts(seconds)
    postlist = Post.objects.filter(date__gt=curdate).order_by('date')[0:50]
    return HttpResponse(jsonf(postlist))        


def post_mood(req):
    query = json.loads(query)
    post_imgurl = query.get('img')
    post_text = query.get('text')
    post = Post(img=post_imgurl)