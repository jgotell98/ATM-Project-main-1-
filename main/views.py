

from django.http import HttpResponse
from administrator.models import ATMachine
from django.shortcuts import render 



#Request that loads the ATM main home page 
def index(request):
    try: 
        machine = ATMachine.objects.get(atm_machine_uid = '1111222233334444')
    except: 
        return HttpResponse('Machine Error')

    if 'machine' not in request.session: 
        request.session['machine'] = machine.atm_machine_uid
    
    return render(request, 'main/home.html')
