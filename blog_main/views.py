from urllib import request
from blogs.models import Blog, Category
from django.shortcuts import render , HttpResponse

def home(request):
    # categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured = True, status = "Publish").order_by('-crated_at')[:3]
    not_featured = Blog.objects.filter(is_featured= False).order_by('-crated_at')
    context = {
        # 'categories': categories,
        'featured_post': featured_post,
        'not_featured':not_featured,
    }
    return render(request, 'home.html', context)