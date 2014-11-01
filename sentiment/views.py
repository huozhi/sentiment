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
        # print 'session',q.name
        return render(req, 'home.html', {'name': uname})
    return render(req, 'index.html')
        # req.session['name'] = q.get('name')
        # return HttpResponse('0')
        
        #     print name,pwd
        #     data = { 'state' : 0 }
        #     # try:
        #     user = User.objects.get(name=name, pwd=pwd)
        #     # req.session['name'] = user.name
        #     print data
        #     return HttpResponse(0)
        # else:
        #     return index(req)
        # except User.DoesNotExist:
            # data['state'] = 1
            # return HttpResponse(data)


def user_mood(req):
    # name = req.session.get('name',None)
    # print 'session',name
    # if name is None:
        # return index(req)
    # req.session['name'] = 'q'
    return render(req, 'home.html')
    query = json.loads(req.body)
    seconds = json.loads('date')
    fts = datetime.datetime.fromtimestamp
    curdate = fts(seconds)
    postlist = Post.objects.filter(date__gt=curdate).order_by('date')[0:50]
    return HttpResponse(postlist)


def post_mood(req):
    query = json.loads(query)
    post_imgurl = query.get('img')
    post_text = query.get('text')
    post = Post(img=post_imgurl)