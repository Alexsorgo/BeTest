from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import JSONField
from django import forms
from django.forms import ModelForm
from rest_framework import serializers


# Create your models here.
class req(models.Model):
    class Meta:
        db_table = "req"
    url = models.CharField(max_length=200)
    method = models.CharField(max_length=10)
    header = JSONField()
    body = models.TextField()
    tag = models.CharField(max_length=50, primary_key=True)


class res(models.Model):
    class Meta:
        db_table = "res"
    tag = models.ForeignKey(req, related_name="restag")
    status = models.CharField(max_length=50)
    body = JSONField()
    date = models.DateField()

