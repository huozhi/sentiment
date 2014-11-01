from django.db.models import *

# Create your models here.

# class Comment(Model):
#     author = CharField(max_length=20)
#     img = TextField()



class Post(Model):
    img = TextField()
    text = CharField(max_length=200)
    # date = DateTimeField()
    tmood = FloatField()
    imood = CharField(max_length=10)
    # public = BooleanField(default=False)
    # comments = (ForeignKey(Comment))



class User(Model):
    name = CharField(max_length=20)
    pwd = CharField(max_length=20)
    posts = ForeignKey(Post, blank=True,null=True)


