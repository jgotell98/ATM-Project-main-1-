from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='user-home'),
    path('cardholder-login', views.cardholderLogin, name = 'cardholder-login'),
    path('cardholder-logout', views.cardholderLogout, name = 'cardholder-logout'),
    path('cash-transfer', views.cashTransfer, name = 'cash-transfer'),
    path('cash-withdrawal', views.cashWithdrawal, name = 'cash-withdrawal'),
    path('balance-inquiry', views.balanceInquiry, name='balance-inquiry'),
    path('transaction-history', views.transactionHistory, name='transaction-history'),
    path('pin-change', views.pinChange, name = 'pin-change'),
    path('phone-number-change', views.phoneNumberChange, name = 'phone-number-change'),
]