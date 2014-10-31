from django.db import models
from mongoengine import *

# Create your models here.


class Comment(EmbeddedDocument):
    author = StringField(max_length=20)
    img = StringField()



class Post(EmbeddedDocument):
    img = StringField()
    text = StringField(max_length=200)
    date = DateTimeField()
    tmood = IntField()
    imood = StringField(max_length=10)
    public = BooleanField(default=False)
    comments = ListField(EmbeddedDocumentField(Comment))



class User(Document):
    name = StringField(max_length=20,required=True)
    pwd = StringField(max_length=20,required=True)
    posts = ListField(EmbeddedDocumentField(Post), default=None)


