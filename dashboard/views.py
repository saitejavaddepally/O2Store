from django.shortcuts import render
from .models import brand_new

# Create your views here.

def home(request): 

    brand_new_details = brand_new.objects.all()
    return render(request, 'dashboard.html', {'brand_new' : brand_new_details})
