from django.db import models

# Create your models here.


class User(models.Model):
    text = models.CharField(max_length=255, null=False)
