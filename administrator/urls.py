from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='admin-home'),
    path('admin-login', views.adminLogin, name = 'admin-login'),
    path('admin-logout', views.adminLogout, name = 'admin-logout'),
    path('add-atm-card', views.addNewATMCard, name = 'add-atm-card'), 
    path('atm-machine-status', views.viewATMachineStatus, name = 'atm-machine-status'), 
    path('update-atm-card', views.updateATMCard, name = 'update-atm-card'), 
    path('block-atm-card', views.blockATMCard, name = 'block-atm-card'), 
    path('activate-atm-card', views.activateATMCard, name = 'activate-atm-card'), 
    path('reset-pin', views.resetPin, name = 'reset-pin'), 
    path('reset-phone-number',views.resetPhoneNumber, name = 'reset-phone-number'), 
    path('view-transaction-history', views.viewTransactionHistory, name = 'view-transaction-history'), 
    path('update-expiration-date', views.updateExpDate, name = 'update-expiration-date')
]