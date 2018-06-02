# -*- coding: utf8 -*-
from django.db import models

class Topic(models.Model):
    # 主旨
    subject = models.CharField(max_length=255, verbose_name='討論主題')
    # 內容
    content = models.TextField(verbose_name='討論內容')
    # 發起人
    poster = models.CharField(max_length=20, verbose_name='發起人')
    # 發表日期
    publication_date = models.DateTimeField(auto_now_add=True)
    # 回覆日期
    reply_date = models.DateTimeField(null=True, blank=True)
    # 計數器
    hit =  models.IntegerField(default=0)    
    
class Reply(models.Model):
    # 回覆主題
    topic_id = models.IntegerField(default=0)
    # 回覆內容
    content = models.TextField(verbose_name= '回覆內容')
    # 發表者
    poster = models.CharField(max_length=20, verbose_name='發起人')
    # 發表日期
    publication_date = models.DateTimeField(auto_now_add=True)