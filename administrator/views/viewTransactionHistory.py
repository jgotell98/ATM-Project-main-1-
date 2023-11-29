from main.models import Transaction
from ..forms import ModCardForm
from main.services import renderPage, getCardholderByNumber, setContextMessage, getTransactionsByCard, getTransactionsByMachine, getCardholderByNumber
from user.models import ATMCard
from ..decorator import admin_authenticated

#Request to view transaction history of the ATM, there may be many transactions so a new page for this would work better 
@admin_authenticated
def viewTransactionHistory(request): 
    renderData = {
        'request': request, 
        'path': 'administrator/view-transaction-history.html', 
        'context': {
            'form': ModCardForm(), 
            'message': '', 
            'history': getTransactionsByMachine(request.session['machine'])
        }
    }
    if request.method == 'POST': 
        form = ModCardForm(request.POST)
        if form.is_valid(): 
            card = getCardholderByNumber(form.cleaned_data['card_number'])
            if not card: 
                setContextMessage(renderData['context'], 'Card not found')
                return renderPage(renderData)
            transactions = getTransactionsByCard(form.cleaned_data['card_number'])
            if not transactions: 
                setContextMessage(renderData['context'], 'There are not transactions for this card')
                return renderPage(renderData)
            
            renderData['context']['history'] = transactions
            return renderPage(renderData)
    else: 
        return renderPage(renderData)