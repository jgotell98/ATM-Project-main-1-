from django.shortcuts import redirect


def adminLogout(request): 
    try: 
        del request.session['admin-token']
        return redirect('/')
    except KeyError: 
        pass 