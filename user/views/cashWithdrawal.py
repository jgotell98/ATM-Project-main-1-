from ..decorator import user_authenticated
from django.shortcuts import render, redirect
from user.models import ATMCard
from ..forms import WithdrawalForm
from main.models import Transaction
from administrator.models import ATMachine
import time

#GET request to load page with form for withdrawing money 
@user_authenticated
def cashWithdrawal(request): 
    #logic for loading page for money withdrawal 
    if (request.method == 'POST'):
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            try:
                card = ATMCard.objects.get(card_number = request.session['token'])
            except:
                form = WithdrawalForm()
                return render(request, 'user/cash-withdrawal.html', {
                    'form': form,
                    'message': 'User does not exist with that account number.'
                })
            amount = form.cleaned_data['amount']
            if amount <= 0: 
                form = WithdrawalForm()
                return render(request, 'user/cash-withdrawal.html', {
                    'form': form, 
                    'message': 'Not a valid withdrawal amount'
                })
            ## checks our balance 
            if card.account_number.balance < amount:
                ## if there are not enough funds 
                form = WithdrawalForm()
                return render(request, 'user/cash-withdrawal.html', {
                    'form': form,
                    'message': 'Insufficient Funds.'
                })
            else: 
                # there are enough funds   
                #Update Database
                card.account_number.balance -= amount
                card.account_number.save()
                print("Money dispursed. New Balance: ", amount)
                transaction = Transaction(
                    status = 'complete',
                    response_code = '200',
                    transaction_type = 'cash-withdraw'
                )
                transaction.atm_card_number = card
                machine = ATMachine.objects.get(atm_machine_uid = request.session['machine'])
                transaction.atm_machine_uid = machine
                transaction.save()
                form = WithdrawalForm()
                return render(request, 'user/cash-withdrawal.html', {
                    'message': 'Funds Withdrawn Successfully',
                    'form': form
                })
        else: 
            form = WithdrawalForm()
            return render(request, 'user/cash-withdrawal.html', {
            'form': form,
            'message': 'Form is not valid.'
        })
    else:
        form = WithdrawalForm()
        return render(request, 'user/cash-withdrawal.html', {'form': form})