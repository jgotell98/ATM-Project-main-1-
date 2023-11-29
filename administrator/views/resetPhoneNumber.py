from django.shortcuts import render, redirect
from ..forms import PhoneResetForm
from user.models import ATMCard
from main.services import renderPage, getCardholderByNumber, setContextMessage
from ..decorator import admin_authenticated



#Request to reset phone number
@admin_authenticated
def resetPhoneNumber(request): 
    renderData = {
        'request': request,
        'path': 'administrator/reset-phone-number.html',
        'context': { 
            'form': PhoneResetForm(),
            'message': '',
        } 
    }
    if request.method == 'POST': 
        form = PhoneResetForm(request.POST)
        if form.is_valid():
            card = getCardholderByNumber(form.cleaned_data['card_number'])
            #if card is a string it means we have an error message
            if not card: 
                setContextMessage(renderData['context'], 'Card not found')
                return renderPage(renderData)

            #verify the phone number contains only numbers
            check = form.cleaned_data['phone_number'].replace('-', '')
            if check.isdigit():
                card.phone_number = form.cleaned_data['phone_number']
                card.save()
                setContextMessage(renderData['context'], 'Phone Number changed to ' + card.phone_number)
                return renderPage(renderData)               

            else:
                setContextMessage(renderData['context'], 'Invalid Phone Number')
                return renderPage(renderData)

    else: 
        return renderPage(renderData) 