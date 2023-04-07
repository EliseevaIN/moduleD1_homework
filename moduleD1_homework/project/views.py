from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def show_main(request):
    return render(request, 'flatpages/main.html')

# def index(request):
#     return render(request, 'main.html')

# def show_services(request):
#     return render(request, 'flatpages/services.html')

# def show_about(request):
#     return render(request, 'flatpages/about.html')

# def show_contacts(request):
#     return render(request, 'flatpages/contacts.html')

# def show_authorized(request):
#     return render(request, 'flatpages/private.html')
