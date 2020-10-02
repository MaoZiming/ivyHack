from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    # many to one with Order

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    # many to one with Deal
    def __str__(self):
        return self.name

class Deal(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='deals', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    original_price = models.FloatField()
    new_price = models.FloatField()
    img_url = models.CharField(max_length=100)
    # Many to one with Order

    def __str__(self): 
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    deal = models.ForeignKey(Deal, related_name='orders', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)



