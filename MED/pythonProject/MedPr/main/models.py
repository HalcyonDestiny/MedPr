from django.db import models


class Results(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField()


class Questions(models.Model):
    content_text = models.TextField(max_length=200, null=True, blank=True)
    content_image = models.ImageField(null=True, blank=True)
    content_video = models.FileField(null=True, blank=True)
    answer_text = models.CharField(max_length=120)

