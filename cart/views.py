from django.shortcuts import render
from .models import user_cart
from dashboard.models import brand_new
from accounts.models import user_login

# Create your views here.

def cart(request):
    cust_prod_id = user_cart.objects.filter(cust_id=7).values_list('prod_id_id',flat=True)
    if(cust_prod_id.exists()):
        print(cust_prod_id)
    # cart_details = brand_new.objects.filter(id = cust_prod_id).first()
    # print(cart_details)
    # print(cart_details)
    # details = {
    #     "cart_details" : cart_details
    # }
    return render(request, 'cart.html')