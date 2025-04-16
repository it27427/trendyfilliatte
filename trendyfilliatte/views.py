from django.shortcuts import render
from blogs.models import Category


def home(request):
    categories = Category.objects.all()
    context = { 'categories': categories }
    return render(request, 'home.html', context)


# 404 error page
def error_404_view(request, exception):
    return render(request, '404.html', status=404)