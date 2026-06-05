from urllib import request

from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

# Create your views here.

# category CURD operations

# lgoin checkup
@login_required(login_url="login")
def dashboard(request):
    category_count = Category.objects.all().count
    blogs_count = Blog.objects.all().count

    context = {"blog_count": blogs_count, "category_count": category_count}

    return render(request, "dashboards/dashboard.html", context)


# @login_required(login_url='login')
def category(request):
    category_name = Category.objects.all()

    context = {
        "category_name": category_name,
    }
    return render(request, "dashboards/category.html", context)


def add_category(request):
    if request.method == "POST" and request.POST["category_name"] != "":

        category_name = request.POST["category_name"]
        category = Category.objects.create(category_name=category_name)
        category.save()
        return redirect("category")
    else:
        return render(request, "dashboards/add_category.html")


def edit_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST" and request.POST["category_name"] != "":
        category_name = request.POST["category_name"]
        category.category_name = category_name
        category.save()
        return redirect("category") 

    context = {"category": category}
    return render(request, "dashboards/edit_category.html", context)


def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect("category")

# blog CURD operations

def blog(request):
    blogs = Blog.objects.all()

    context = {
        "blogs": blogs,
    }
    return render(request, "dashboards/blog_posts.html", context)

def delete_blog(request, id):   
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("blog_posts")   

def add_blog(request):
    category = Category.objects.all()  # to show category in dropdown menu in add blog page
    if request.method == "POST" and request.POST["title"] != "" and request.POST["short_description"] != "" and request.POST["blog_body"] != "" and request.FILES["featured_image"] != "":
        title = request.POST["title"]
        short_description = request.POST["short_description"]
        blog_body = request.POST["blog_body"]
        featured_image = request.FILES["featured_image"]
        category_id = request.POST["category"]

        category = Category.objects.get(id=category_id) # to get the category for assigining it to the blog 

        blog = Blog.objects.create(
            title=title,
            short_description=short_description,
            blog_body=blog_body,
            featured_image=featured_image,
            category=category,
            author=request.user,
            slug = title.replace(" ","-").lower(),
            is_featured = True,
            status = "Publish"

        )
        blog.save()
        return redirect("blog_posts")
    else:
        context = {"category": category}
        return render(request, "dashboards/edit_post.html", context)
    
def edit_blog(request, id):
    category = Category.objects.all() 
    if request.method == "POST" and request.POST["title"] != "" and request.POST["short_description"] != "" and request.POST["blog_body"] != "":
        blog = Blog.objects.get(id=id)
        title = request.POST["title"]
        short_description = request.POST["short_description"]
        blog_body = request.POST["blog_body"]
        category_id = request.POST["category"]

        category = Category.objects.get(id=category_id) # to get the category for assigining it to the blog 

        blog.title = title
        blog.short_description = short_description
        blog.blog_body = blog_body
        # blog.slug = title.replace(" ","-").lower()  or -- 
        blog.slug = slugify(title) + "-" + str(blog.id)  # it is working fine 

        blog.category = category
        if "featured_image" in request.FILES: # checking if user has uploaded files or not 
            featured_image = request.FILES["featured_image"]
            blog.featured_image = featured_image

        blog.save()
        return redirect("blog_posts")
    blog_post = Blog.objects.get(id=id)
    context = {"category": category
               ,"blog": blog_post
               }
    return render(request, "dashboards/edit.html",context)


# now making the tile clickable and on clicking the it opens the psots 