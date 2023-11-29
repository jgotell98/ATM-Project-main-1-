from ..decorator import user_authenticated
from main.services import renderPage, getCardholderByNumber, setContextMessage, validatePhoneNumber
from user.forms import PhoneNumberChangeForm

#Request to load form for phone number change 
@user_authenticated
def phoneNumberChange(request): 
    #logic for loading page goes here  
    renderData = {
        'request': request, 
        'path': 'user/phone-number-change.html', 
        'context': {
            'form': PhoneNumberChangeForm(), 
            'message': ''
        }
    }
    if request.method == 'POST': 
        form = PhoneNumberChangeForm(request.POST)
        if form.is_valid(): 
            card = getCardholderByNumber(request.session['token'])
            if not card: 
                return redirect('/user/cardholder-login')
            if not validatePhoneNumber(form.cleaned_data['old_phone_number']) or not validatePhoneNumber(form.cleaned_data['new_phone_number']): 
                setContextMessage(renderData['context'], 'There is a problem with the format of your phone number')
                return renderPage(renderData)
            if card.phone_number != form.cleaned_data['old_phone_number']: 
                setContextMessage(renderData['context'], 'The old phone number input does not match your old phone number')
                return renderPage(renderData)

            card.phone_number = form.cleaned_data['new_phone_number']
            card.save()
            setContextMessage(renderData['context'], 'Your new phone number is now ' + card.phone_number)
            return renderPage(renderData)
    
    else: 
        return renderPage(renderData)