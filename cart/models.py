from django.db import models
from dashboard.models import brand_new
from accounts.models import user_login


# Create your models here.

class user_cart(models.Model):
    cust_id = models.ForeignKey(user_login, on_delete= models.CASCADE)
    prod_id = models.ForeignKey(brand_new, on_delete = models.CASCADE)