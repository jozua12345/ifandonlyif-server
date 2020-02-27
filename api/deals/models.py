from django.db import models

# Create your models here.
class Deals(models.Model):
    name = models.CharField(max_length=155)
    start = models.CharField(max_length=25)
    end = models.CharField(max_length=25)
    image = models.CharField(max_length=110)
    vendors = models.CharField(max_length=41)
    terms = models.CharField(max_length=4315)
    category = models.CharField(max_length=126)

    def __str__(self):
        return self.name