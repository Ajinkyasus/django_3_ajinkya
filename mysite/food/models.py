from django.db import models

# Create your models here.

class Item(models.Model):
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(
    max_length=200,
    default='xyz'
    )
    item_name = models.CharField(max_length=500)
    item_desc = models.CharField(
        max_length=500,
        default="Conubia sem netus ad convallis proin. Nam lobortis ad justo inceptos vehicula sapien rhoncus rhoncus? Vel pellentesque ut taciti gravida hac sociis hendrerit semper platea penatibus fusce sociis. Quis eros dapibus phasellus vulputate."
        )
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://assets.materialup.com/uploads/b03b23aa-aa69-4657-aa5e-fa5fef2c76e8/preview.png"
        )
    #create superuser on  monday
    
    def __str__(self):
        return self.item_name
    
