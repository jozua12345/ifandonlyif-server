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

class ClientUsers(models.Model):
    name = models.CharField(max_length=155)
    uid  = models.CharField(max_length=155)

    def __str__(self):
        return self.uid

class BlackLists(models.Model):
    clientuser2= models.ForeignKey(ClientUsers, on_delete=models.CASCADE, related_name='clientuser2')
    clientuser1= models.ForeignKey(ClientUsers, on_delete=models.CASCADE, related_name='clientuser1')
    deal = models.ForeignKey(Deals, on_delete=models.CASCADE)

    def __str__(self):
        return self.id