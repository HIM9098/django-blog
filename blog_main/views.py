from urllib import request
from blog_main.forms import UserRegistrationForm 
from django.contrib.auth.forms import AuthenticationForm
from blogs.models import Blog, Category
from django.shortcuts import redirect, render , HttpResponse
from django.contrib import auth

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

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User registered successfully') 
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(username = username , password = password )
            if user is not None : 
                auth.login(request, user)
                return redirect('home')
    else :

        form = AuthenticationForm()
    context = {
        'form': form
    }

    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)    # how this is working without request argument in logout functinon 
    return redirect('home')