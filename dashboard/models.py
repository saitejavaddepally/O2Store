from django.db import models

# Create your models here.

class brand_new(models.Model):
    item_number = models.IntegerField()
    item_name = models.TextField()
    item_img = models.ImageField(upload_to= 'pics')
    item_price = models.IntegerField()
    item_size = models.IntegerField()

# class rental: 
#     item_number : int
#     item_name : str
#     item_img : str
#     item_price : int
#     item_size : int

# class second_hand:
#     item_number : int
#     item_name : str
#     item_img : str
#     item_price : int
#     item_size : int