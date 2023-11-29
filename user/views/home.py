from django.shortcuts import render 
from user.models import AccountExtension
from ..decorator import user_authenticated
from main.models import Transaction
#GET request loads page with options for ATM cardholder 
@user_authenticated
def home(request): 
    print(Transaction.objects.all())
    return render(request, 'user/home.html')


    #HARDCODED EXAMPLE OF MODEL CREATION
    # acc = AccountExtension(
    #     account_number = 2222222222,
    #     name = 'brandon corn', 
    #     phone_number = '569-1624', 
    #     balance = 9999999
    # )  
    # acc.save()
    # accounts = AccountExtension.objects.all()
    # AccountExtension.objects.all().delete()
    # for account in accounts: 
    #     print("account num: ",account.account_number)
    #     print("name: ", account.name)


    #SAVING FOREIGN KEYS
    #card.account_number = AccountExtension.objects.get(account_number = '1111111111')