from django.shortcuts import redirect
from ..decorator import user_authenticated
from user.forms import PinChangeForm
from main.services import getCardholderByNumber, renderPage, setContextMessage

#Request for loading pin change form 
@user_authenticated
def pinChange(request): 
    renderData = {
        'request': request, 
        'path': 'user/pin-change.html', 
        'context': {
            'form': PinChangeForm(), 
            'message': ''
        }
    } 
    if request.method == 'POST': 
        form = PinChangeForm(request.POST)
        if form.is_valid(): 
            card = getCardholderByNumber(request.session['token'])
            if not card: 
                setContextMessage(renderData['context'], 'Could not get cardholder')
                return redirect('/user/cardholder-login')
            
            if len(form.cleaned_data['new_pin']) < 4 or len(form.cleaned_data['confirm_pin']) < 4: 
                setContextMessage(renderData['context'], 'PIN must be 4 digits')
                return renderPage(renderData)
            if card.pin != form.cleaned_data['old_pin']: 
                setContextMessage(renderData['context'], 'Old PIN is incorrect')
                return renderPage(renderData)
            if form.cleaned_data['new_pin'] != form.cleaned_data['confirm_pin']: 
                setContextMessage(renderData['context'], 'New PINs do not match')
                return renderPage(renderData)
            
            card.pin = form.cleaned_data['new_pin']
            card.save()
            setContextMessage(renderData['context'], 'PIN changed successfully to ' + card.pin)
            return renderPage(renderData)

    else: 
        return renderPage(renderData)
    return