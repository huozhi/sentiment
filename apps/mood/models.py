from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class Comment(Model):
#     author = CharField(max_length=20)
#     img = TextField()

class User(AbstractUser):
    def __unicode__(self):
        return self.username


class Post(models.Model):
    text = models.CharField(max_length=200)
    image = models.TextField()
    tmood = models.FloatField()
    imood = models.CharField(max_length=10)
    poster = models.ForeignKey(User, blank=True, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=20)
    related = models.ForeignKey(Post, blank=True, null=True)






