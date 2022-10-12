from django.db import models


class Widget(models.Model):
    name = models.CharField(max_length=64)
    part_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
