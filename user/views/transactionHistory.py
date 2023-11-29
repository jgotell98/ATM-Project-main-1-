from django.shortcuts import redirect
from ..decorator import user_authenticated
from main.services import renderPage, setContextMessage, getTransactionsByCard, getCardholderByNumber
#Request for viewing transaction history 
@user_authenticated
def transactionHistory(request): 
    #logic for getting transaction history goes here
    renderData = {
        'request': request, 
        'path': 'user/transaction-history.html', 
        'context': {
            'message': '', 
            'history': [] 
        }
    }
    card = getCardholderByNumber(request.session['token'])
    #issue getting the cardholder that's logged in, redirect them to login screen
    if not card: 
        setContextMessage(renderData['context'], 'Issue getting cardholder')
        return redirect('/user/cardholder-login')
    transactions = getTransactionsByCard(card.card_number)
    #will have false value if there are not transactions 
    if not transactions: 
        setContextMessage(renderData['context'], 'You have no transactions')
        return renderPage(renderData)
    
    #return all the transactions of the logged in cardholder 
    renderData['context']['history'] = transactions
    return renderPage(renderData)