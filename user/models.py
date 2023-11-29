from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


# Create your models here.

class AccountExtension(models.Model): 
    account_number = models.CharField(
        primary_key=True,
        max_length = 10,
        unique = True
    )
    name = models.CharField(
        max_length = 35
    )
    phone_number = models.CharField(
        max_length = 12
    )
    balance = models.BigIntegerField()



class ATMCard(models.Model): 
    CARD_STATUS_CHOICES = (
        ('active', 'Active'),
        ('deactivated', 'deactivated')
    )
    AUTH_STATUS = (
        ('on', 'On'), 
        ('off', 'Off')
    )
    def newExpDate(): 
        return timezone.now() + timezone.timedelta(days=1095)

    card_number = models.CharField(
        primary_key=True,
        max_length = 16,
        unique=True,
    )
    account_number = models.ForeignKey(
        AccountExtension,
        to_field = 'account_number',
        on_delete=models.DO_NOTHING, 
        verbose_name="account extension", 
        default = None
    )
    pin = models.CharField(
        max_length = 4
    )
    name = models.CharField(
        max_length=35
    )
    date_issued = models.DateField(
        default = timezone.now
    )
    expire_date = models.DateField(
        default = newExpDate
    ) 
    address = models.CharField(
        max_length=100
    )
    two_fact_auth_status = models.CharField(
        max_length = 5,
        choices = AUTH_STATUS, 
        default = 'off'
    )
    phone_number = models.CharField(
        max_length=12
    )
    card_status = models.CharField(
        max_length=15,
        choices=CARD_STATUS_CHOICES, 
        default = 'deactivated'
    )

