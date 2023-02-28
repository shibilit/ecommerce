from django.shortcuts import render, redirect


def auth_customer(func):
    def wrapper(request, *args, **kwargs):
        if 'Costomer' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('common:home')
    return wrapper
