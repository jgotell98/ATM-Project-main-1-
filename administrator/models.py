from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Admin(models.Model): 
    username = models.CharField(
        primary_key = True, 
        max_length = 20, 
        unique = True
    )
    password = models.CharField(
        max_length = 20
    )


class ATMachine(models.Model): 
    STATUS_CHOICES = (
        ("active", "Active"),
        ("deactivated", "Deactivated")
    )
    atm_machine_uid = models.CharField(
        primary_key = True, 
        max_length = 16,
        unique = True
    )
    current_balance = models.BigIntegerField()
    location = models.CharField(
        max_length = 100
    )
    minimum_balance = models.BigIntegerField()
    status = models.CharField(
        max_length = 15,
        choices = STATUS_CHOICES, 
        default = 'active'
    )
    last_refill_date = models.DateField(
        null = True
    )
    next_maint_date = models.DateField(
        null = True
    )



class ATMachineRefill(models.Model): 
    refill_id = models.CharField(
        primary_key = True,
        max_length = 10,
        unique = True
    )
    atm_machine_uid = models.ForeignKey(
        ATMachine, 
        to_field = 'atm_machine_uid',
        on_delete = models.DO_NOTHING,
        verbose_name = "ATM Machine UID"
    )
    amount = models.BigIntegerField()
    atm_branch = models.CharField(
        max_length = 30
    )
    refill_date = models.DateField()
    previous_balance = models.BigIntegerField()