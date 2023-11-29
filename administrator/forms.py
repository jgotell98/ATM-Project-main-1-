from django import forms

class AdminLoginForm(forms.Form): 
    username = forms.CharField(
        label = 'username', 
        max_length = 20
    )
    password = forms.CharField(
        label = 'Password', 
        max_length = 20, 
        widget = forms.PasswordInput()
    )



class AdminForm(forms.Form): 
    card_number = forms.CharField(
        label = 'card number',
        max_length = 16
    )
    pin = forms.CharField(
        label = 'PIN', 
        max_length = 4, 
        widget = forms.PasswordInput()
        )

        
class newCardForm(forms.Form): 
    # card_number = forms.CharField(
    #     max_length = 16,
    #     label = "card_number"
    # )
    account_number = forms.CharField(
        max_length = 10,
        label = "account_number"
    )
    pin = forms.CharField(
        max_length = 4,
        label = "pin", 
        widget = forms.PasswordInput()
    )
    name = forms.CharField(
        max_length=35,
        label = "name"
    )
    address = forms.CharField(
        max_length=100,
        label = "address"
    )
    phone_number = forms.CharField(
        max_length=12,
        label = "phone_number"
    )
class ModCardForm(forms.Form): 
    card_number = forms.CharField(
        label = 'Card Number', 
        max_length = 16
    )

class PhoneResetForm(forms.Form): 
    card_number = forms.CharField(
        label = 'Card Number', 
        max_length = 16
    )
    phone_number = forms.CharField(
        label = 'New Phone Number', 
        max_length = 12
    )

class UpdateExpDateForm(forms.Form): 
    card_number = forms.CharField(
        label = 'Card Number',
        max_length = 16
    )