from django.shortcuts import render

def home(request):
    return render(request, 'main_app/index.html')

def about(request):
    return render(request, 'main_app/aboutus.html')

def services(request):
    return render(request, 'main_app/services.html')

def contact(request):
    return render(request, 'main_app/contactus.html')
