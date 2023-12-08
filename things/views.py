from django.shortcuts import render

def home(request):
    return render(request, 'things/templates/home.html')
