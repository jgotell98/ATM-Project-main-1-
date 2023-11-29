from ..decorator import user_authenticated
from django.shortcuts import render, redirect
from ..forms import TransferForm
from user.models import ATMCard, AccountExtension
from main.models import Transaction
from administrator.models import ATMachine
import time
#GET request to load page with form for cash transfer
@user_authenticated
def cashTransfer(request): 
    #logic for loading cash transfer page
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            ## Account from form
            accNum = form.cleaned_data['account_num']
            amount = form.cleaned_data['amount']
            if (amount < 0): 
                form = TransferForm()
                return render(request, 'user/cash-transfer.html', {'form': form, 'message': 'Not a valid transfer amount'})
            try:
                ## tries to get the account
                rec_account = AccountExtension.objects.get(account_number = accNum)
            except:
                form = TransferForm()
                return render(request, 'user/cash-transfer.html', {
                    'form': form,
                    'message': 'User does not exist with that account number.'
                })
            
            ## checks our balance 
            card = ATMCard.objects.get(card_number = request.session['token'])
            if card.account_number.balance < amount:
                ## if there are not enough funds 
                form = TransferForm()
                return render(request, 'user/cash-transfer.html', {
                    'form': form,
                    'message': 'Insufficient Funds.'
                })
            else: 
                # there are enough funds 
                card.account_number.balance -= amount
                rec_account.balance += amount
                card.account_number.save()
                rec_account.save()
                transaction = Transaction(
                    status = 'complete',
                    response_code = '200',
                    transaction_type = 'cash-transfer'
                )
                transaction.atm_card_number = card
                machine = ATMachine.objects.get(atm_machine_uid = request.session['machine'])
                transaction.atm_machine_uid = machine
                transaction.save()
                form = TransferForm()
                return render(request, 'user/cash-transfer.html', {
                    'message': 'Funds Transfered Successful',
                    'form': form
                })
                
                
        else: 
            form = TransferForm()
            return render(request, 'user/cash-transfer.html', {
            'form': form,
            'message': 'Form is not valid.'
        })
    else:
        print(AccountExtension.objects.all())
        form = TransferForm()
        return render(request, 'user/cash-transfer.html', {
            'form': form
        })