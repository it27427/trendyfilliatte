from django.shortcuts import render
from blogs.models import Category, Blogs


def home(request):
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_featured=True)
    post = Blogs.objects.filter(is_featured=False, status='published')
    context = {
        'categories': categories,
        'featured_post': featured_post,
    }
    return render(request, 'home.html', context)


# 404 error page
def error_404(request, exception):
    return render(request, '404.html', status=404)