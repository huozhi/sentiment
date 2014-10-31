from django.db import models
from mongoengine import *

# Create your models here.

class MoodUser(Document):
    name = StringField(max_length=20)
    pwd = StringField(max_length=20)
    posts = EmbeddedDocumentField(MoodPost)

class MoodPost(EmbeddedDocument):
    text = StringField(max_length=400)
    photo = ImageField()

