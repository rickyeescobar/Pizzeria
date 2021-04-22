from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200)

    date_added = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name

#class Topping(models.Model):
    #pizza = Topping