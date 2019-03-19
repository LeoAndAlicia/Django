# -*- coding:utf-8 -*-

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)

    def __unicode__(self):  # 返回title
        return self.title
