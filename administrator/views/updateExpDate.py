from ..decorator import admin_authenticated
from administrator.forms import UpdateExpDateForm
from main.services import renderPage, setContextMessage, getCardholderByNumber, newExpDate
from user.models import ATMCard
from django.utils import timezone
from datetime import datetime, date

#Request to update expiration date of ATM card 
@admin_authenticated
def updateExpDate(request): 
    renderData = {
        'path': 'administrator/update-expiration-date.html', 
        'request': request, 
        'context': {
            'form': UpdateExpDateForm(), 
            'message': ''
        }
    }
    if request.method == 'POST': 
        form = UpdateExpDateForm(request.POST)
        if form.is_valid(): 
            card = getCardholderByNumber(form.cleaned_data['card_number'])

            if not card: 
                setContextMessage(renderData['context'], 'Card not found')
                return renderPage(renderData)
            
            if card.expire_date > date.today(): 
                setContextMessage(renderData['context'], 'Card is not expired yet')
                return renderPage(renderData)
        
            # card.expire_date = date.today() + timezone.timedelta(days=1095)
            card.expire_date = newExpDate()
            card.save()
            setContextMessage(renderData['context'], 'Expire date updated to ' + str(card.expire_date)[0:10])
            return renderPage(renderData)
    
    else: 
        return renderPage(renderData)
    