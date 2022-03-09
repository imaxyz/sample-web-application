from django.db import models


class TestModel(models.Model):
    """TestModel model classes"""
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    content = models.TextField()
