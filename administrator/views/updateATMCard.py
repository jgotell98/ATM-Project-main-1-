from django.shortcuts import render 
from ..decorator import admin_authenticated

#Request to load page for update ATM card options
@admin_authenticated
def updateATMCard(request): 
    #logic for loading page with update options for ATM card goes here 
    
    return render(request, 'administrator/update-atm-card.html')
