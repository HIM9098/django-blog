
from .import views
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static 
from django.conf import settings 
from blogs import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', include('blogs.urls')),
    path('blog/<slug:slug>/', blog_views.blog_detail, name='blog_detail'),
    path('search/blog/', blog_views.search_blog, name='search_blog'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
