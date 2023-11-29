from django.shortcuts import render
from ..decorator import admin_authenticated

@admin_authenticated
def home(request): 
    return render(request, 'administrator/home.html')