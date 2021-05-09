from django.db import models

from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=15, null=1)
    description = models.TextField(max_length=200, null=1)
    date = models.DateTimeField(null=1, default=datetime.now())

    def __str__(self):
        return self.title
