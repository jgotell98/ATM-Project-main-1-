#Request to view status of ATM Machine
from django.shortcuts import render, redirect
from administrator.models import ATMachine
from ..forms import AdminForm
from user.models import ATMCard
from ..decorator import admin_authenticated

@admin_authenticated
def viewATMachineStatus(request): 
    machine = ATMachine.objects.get(atm_machine_uid = request.session['machine'])
    #logic for viewing ATM machine status goes here 
    status = machine.status
    machID = machine.atm_machine_uid
    balance = machine.current_balance
    minBal = machine.minimum_balance
    location = machine.location
    refill = machine.last_refill_date
    maintenance = machine.next_maint_date


    return render(request, 'administrator/atm-machine-status.html', {'status':status,'machID':machID, 'balance':balance, 'minBal':minBal, 'location': location, 'refill':refill, 'maintenance':maintenance})