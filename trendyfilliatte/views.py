from django.http import render

def home(request):
    render(request, 'home.html')