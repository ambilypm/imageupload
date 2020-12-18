from django.db import models


class Product(models.Model):
    category = models.CharField(max_length=25)
    picture = models.ImageField(upload_to='pictures')
