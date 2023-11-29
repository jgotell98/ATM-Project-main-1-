from django.shortcuts import render, redirect
from ..forms import AdminLoginForm
from django.http import HttpResponse
from administrator.models import Admin
from main.services import getAdmin, setContextMessage, renderPage 


def adminLogin(request):
    renderData = {
        'request': request,
        'path': 'administrator/admin-login.html',
        'context': { 
            'form': AdminLoginForm(),
            'message': '',
        } 
    } 
    if request.method == 'POST': 
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            admin = getAdmin(form.cleaned_data['username'])
            if not admin: 
                setContextMessage(renderData['context'], 'Not a valid administrator')
                return renderPage(renderData)
            
            if admin.password != form.cleaned_data['password']: 
                setContextMessage(renderData['context'], 'Incorrect password')
                return renderPage(renderData)
            
            request.session['admin-token'] = admin.username
            return redirect('/administrator')
        else: 
            setContextMessage(renderData['context'], 'Form not valid')
            return renderPage(renderData)
    else:
        admin = Admin(
            username = 'gotell', 
            password = 'gotell'
        )
        admin.save()
        return renderPage(renderData); 