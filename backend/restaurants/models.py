from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    # deal = models.ForeignKey(Deal, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Deal(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)

    def __str__(self): 
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    deals = models.ManyToManyField(Deal)

    def __str__(self):
        return self.name

