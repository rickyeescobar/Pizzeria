from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = model.CharField(max_length=200)

    def __str__(self):
        return self.name