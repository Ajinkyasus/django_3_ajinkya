from django.db import models

# Create your models here.

class item(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=50)
    item_price = models.IntegerField()
    #create superuser on  monday
    
