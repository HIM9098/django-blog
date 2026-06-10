from .forms import EditUserForm
from urllib import request
from django.contrib.auth.models import User 
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .forms import AddUserForm

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
# now manageing the manager dashboard 6

#  users 
# @login_required(login_url="login") 
def users(request):
    users = User.objects.all()

    
    context = {
        'users' : users
            }
    return render(request , "dashboards/users.html",context)

def add_users (request):
    if request.method == "POST":

        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']

        isactive = 'is_active' in request.POST
        issuperuser = 'is_superuser' in request.POST

        user = User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email=email,
            password=password,
        )

        user.is_active = isactive
        user.is_superuser = issuperuser

        # Needed for Django admin access
        if issuperuser:
            user.is_staff = True

        user.save()

        return redirect("users")
    else : 
        form = AddUserForm()
        context = {
        'form':form
            }
        return render(request , 'dashboards/add_user.html',context)
    

def edit_user(request, pk):

    user = User.objects.get(pk=pk)

    if request.method == "POST":

        form = EditUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('users')

    else:
        form = EditUserForm(instance=user)

    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'dashboards/edit_user.html', context)

    
def delete_user (request, pk):
    user = User.objects.get(pk = pk )
    user.delete()
    return redirect('users')