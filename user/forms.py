from django import forms

class UserForm(forms.Form): 
    card_number = forms.CharField(
        label = 'card number',
        max_length = 16
    )
    pin = forms.CharField(
        label = 'PIN', 
        max_length = 4, 
        widget = forms.PasswordInput()
    )

class WithdrawalForm(forms.Form):
    amount = forms.IntegerField(
        label = "amount"
    )

class TransferForm(forms.Form):
    account_num = forms.CharField(
        label = 'Account Number',
        max_length = 10
    )
    amount = forms.IntegerField(
        label = 'Amount'
    )

class PinChangeForm(forms.Form): 
    old_pin = forms.CharField(
        label = 'Old PIN', 
        max_length = 4,
        widget = forms.PasswordInput()
    )
    new_pin = forms.CharField(
        label = 'New PIN', 
        max_length = 4,
        widget = forms.PasswordInput()
    )
    confirm_pin = forms.CharField(
        label = 'Retype New PIN', 
        max_length = 4,
        widget = forms.PasswordInput()
    )

class PhoneNumberChangeForm(forms.Form): 
    old_phone_number = forms.CharField(
        label = 'Old Phone Number ', 
        max_length = 12
    )
    new_phone_number = forms.CharField(
        label = 'New Phone Number ', 
        max_length = 12
    )