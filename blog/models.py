from django.db import models
import datetime

class Article(models.Model):
    title = models.CharField(max_length=50)
    detail = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article)
    detail = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.article
