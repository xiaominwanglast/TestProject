# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Book(models.Model):
    name=models.CharField(max_length=50)
    pub_date=models.DateField()

    def __unicode__(self):
        return self.name
# Create your models here.
