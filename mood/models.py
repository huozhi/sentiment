from django.db.models import *

# Create your models here.

# class Comment(Model):
#     author = CharField(max_length=20)
#     img = TextField()

class User(Model):
    name = CharField(max_length=20)
    pwd = CharField(max_length=20)



class Post(Model):
    img = TextField()
    text = CharField(max_length=200)
    # date = DateTimeField()
    tmood = FloatField()
    imood = CharField(max_length=10)
    # public = BooleanField(default=False)
    # comments = (ForeignKey(Comment))
    poster = ForeignKey(User, blank=True,null=True)




