from django.shortcuts import redirect


def cardholderLogout(request): 
    try: 
        del request.session['token']
        return redirect('/')
    except KeyError: 
        pass 
