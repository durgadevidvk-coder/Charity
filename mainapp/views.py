from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def causes(request):
    return render(request, 'causes.html')

def donate(request):
    return render(request, 'donate.html')

def contact(request):
    return render(request, 'contact.html')

def volunteer(request):
    return render(request, 'volunteer.html')

def thankyou(request):
    return render(request, 'thankyou.html')