from django.shortcuts import render
from user.models import ATMCard
from ..forms import ModCardForm 
from main.services import renderPage, getCardholderByNumber, setContextMessage
from ..decorator import admin_authenticated

#Request to block an ATM card
@admin_authenticated
def blockATMCard(request):
    renderData = {
        'request': request,
        'path': 'administrator/block-atm-card.html',
        'context': { 
            'form': ModCardForm(),
            'message': '',
        } 
    } 
    if request.method == 'POST':
        form = ModCardForm(request.POST)
        if form.is_valid(): 
            card = getCardholderByNumber(form.cleaned_data['card_number'])
            if not card: 
                setContextMessage(renderData['context'], 'Card not found')
                return renderPage(renderData)

            if card.card_status == 'active': 
                card.card_status = 'deactivated'
                card.save()
                setContextMessage(renderData['context'], 'Card deactivated')
                return renderPage(renderData)
            else: 
                setContextMessage(renderData['context'], 'Card already deactivated')
                return renderPage(renderData)
        else: 
            setContextMessage(renderData['context'], 'Form is invalid')
            return renderPage(renderData)
    else: 
        return renderPage(renderData)