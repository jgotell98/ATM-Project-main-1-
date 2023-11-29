from django.shortcuts import render 
from django.http import HttpResponse
from ..decorator import user_authenticated
from user.models import ATMCard

#GET request for loading page to check balance of account
@user_authenticated
def balanceInquiry(request): 
    #logic for loading page goes here 
    #TEST
    #query to retrieve ATMCard object 
    card = ATMCard.objects.get(card_number = request.session['token'])
    
    #since this is a foreign key, card.account_number is the Account Extension Object
    #associated with this ATMCard 
    account = card.account_number
    user_balance = account.balance
    #here we can access the actual account_number and balance
    return render(request, 'user/balance-inquiry.html', {'user_balance': user_balance, 'account':account})