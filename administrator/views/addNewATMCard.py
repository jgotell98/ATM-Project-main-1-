from django.shortcuts import render, redirect
from administrator.models import ATMachine
from ..forms import AdminForm, newCardForm
from user.models import ATMCard, AccountExtension
from ..decorator import admin_authenticated
from main.services import generateCardNumber

#Request to load page with form to add new ATM Card
@admin_authenticated
def addNewATMCard(request): 

    if request.method == 'POST': 
        form = newCardForm(request.POST)
        if form.is_valid():
                #generate card number for new card 
                newNum = generateCardNumber()
                try:
                    account = AccountExtension.objects.get(account_number = form.cleaned_data['account_number'])
                    #account = AccountExtension.objects.get(account_number = '1111111111')
                except:
                    form = newCardForm()
                    return render(request, 'administrator/add-atm-card.html', {'form': form, 'message': 'Not a valid account number'})
                #if card.card_number == form.cleaned_data['card_number']: 
                newATMCard = ATMCard(
                    card_number = newNum,
                    pin = form.cleaned_data['pin'],
                    name = form.cleaned_data['name'], 
                    address = form.cleaned_data['address'], 
                    phone_number = form.cleaned_data['phone_number']
                )
                print('card number: ', newATMCard.card_number)
                print('pin: ', newATMCard.pin)
                newATMCard.account_number = account
                newATMCard.save()
                form = newCardForm()
                return render(request, 'administrator/add-atm-card.html', {'form': form, 'message': 'Card created succesfully!'})
            #else: 
                #request.session['token'] = card.card_number
                #return redirect('/administrator')
        else: 
            return render(request, 'administrator/add-atm-card.html', {'form': form, 'message': 'Form not valid'})
    else:
        print(AccountExtension.objects.all())
        form = newCardForm()
        return render(request, 'administrator/add-atm-card.html', {'form': form})