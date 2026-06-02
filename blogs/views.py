from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from .models import Blog  ,Category
# Create your views here.
def posts_by_category(request, category_id):
    # fetch the post using category 
   
    try :    
        posts = Blog.objects.filter(status='Publish',category = category_id)
        cat_id = get_object_or_404( Category,pk=category_id)
    except :
        return render(request , '404.html')
        
    # categories = Category.objects.all()
    
    context= {
        'posts' : posts, 
        # 'categories':categories,
        'category_id':category_id,
    }
    return render(request , 'posts_by_category.html' ,context )
    # print(posts)
    # return HttpResponse(posts)

def blog_detail(request, slug):
    try : 
        post = Blog.objects.get(slug = slug, status = 'Publish')
    except Blog.DoesNotExist:
        return render(request, '404.html')
    context= {
        'post': post,
    }

    return render(request, 'blog_detail.html', context)

def search_blog(request):
    keyword = request.GET.get('keyword')
    # print(keyword)
    # search for the blogs matching the keyword in title or content
    # and what if the keyword is empty then redirect to home page 
    if keyword:
        post = Blog.objects.filter(status= "Publish").filter(Q(title__icontains= keyword) | Q(author__username__icontains= keyword)| Q(short_description__icontains= keyword)| Q(category__category_name__icontains= keyword))
    else:
        return redirect('home')

    context = {
        'post': post,
        'keyword': keyword,
    }
    
    return render(request, 'search_results.html', context)
