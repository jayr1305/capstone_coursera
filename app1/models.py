from django.db import models

class TableBook(models.Model):
    name = models.CharField(max_length=100)
    guestNumber = models.IntegerField()
    date = models.DateField()

class Menu(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()
    
