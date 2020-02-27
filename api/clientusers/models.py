from django.db import models

# Create your models here.
class ClientUsers(models.Model):
    name = models.CharField(max_length=155)
    uid  = models.CharField(max_length=155)

    def __str__(self):
        return self.uid