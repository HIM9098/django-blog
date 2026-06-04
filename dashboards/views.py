from urllib import request

from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required

# Create your views here.


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
