from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
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