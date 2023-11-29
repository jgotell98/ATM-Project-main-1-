from django.shortcuts import render
from user.models import ATMCard
from main.models import Transaction
from administrator.models import Admin
from django.utils import timezone


# from datetime import datetime, date
import datetime
from random import randint



#METHOD: to retrieve a cardholder by the ATM card number
#@Params: (cardNumber) card number to search for 
#@Returns: If ATMCard found, returns that objects, if not returns string message

def getCardholderByNumber(cardNumber): 
    try: 
        card = ATMCard.objects.get(card_number = cardNumber)
    except: 
        return False
    return card



#METHOD: to render any pages
#works with the assumption that the path has been set properly
#works with the asuumption that the object has "REQUEST", "PATH", and "CONTEXT OBJECT""

def renderPage(renderData): 
    if not renderData['request']: 
        return 'No request provided'
    if not renderData['path']:
        return 'No template path provided'
    if not renderData['context']: 
        return render(renderData['request'], renderData['path'])
    return render(renderData['request'], renderData['path'], renderData['context'])


#METHOD: to get Transaction from cardholder number
#@Params: (cardNumber) card number associated with transactions
#@Returns: if transactions exist returns all transactions, if no transactions returns string message no transactions

def getTransactionsByCard(cardNumber): 
    try: 
        transactions = Transaction.objects.all().filter(atm_card_number = cardNumber)
    except: 
        return False 
    if len(transactions) == 0: 
        return False
    return transactions


    #transactions

def getTransactionsByMachine(machine_id): 
    try: 
        transactions = Transaction.objects.all().filter(atm_machine_uid = machine_id)
    except: 
        return False 
    if len(transactions) == 0: 
        return False
    return transactions

#METHOD: set message of context object

#ASSUMES: the object already has a message property
#@Params: (data) the context object containing the message, (message) string message to be added to message property

def setContextMessage(data, message): 
    data['message'] = message
    return




def getAdmin(user): 
    try:
        admin = Admin.objects.get(username = user)
    except: 
        return false
    return admin

    #add new date

def newExpDate(): 
    return timezone.now() + timezone.timedelta(days=1095)


    #phone number validator

def validatePhoneNumber(phone_number): 
    countCheck = phone_number.count('-')
    if countCheck != 2: 
        return False 
    numberCheck = phone_number.replace('-', '')
    if not numberCheck.isdigit(): 
        return False 
    
    return True


    #generateCardNumber via random numbers
def generateCardNumber(): 
    a = randint(11111111,99999999)
    b = randint(11111111,99999999)
    cardNum = str(a) + str(b)
    try: 
        card = ATMCard.objects.get(card_number = cardNum)
    except: 
        return cardNum
    generateCardNumber()
    

