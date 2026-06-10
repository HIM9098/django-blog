from django.urls import path

from dashboards import views 

urlpatterns= [
    path('', views.dashboard, name='dashboard'),

    # Category URLS // CRUD operations
    path('category/' , views.category , name = "category"),
    path('category/edit_category/<int:id>/',views.edit_category, name = "edit_category"),
    path('category/delete_category/<int:id>/',views.delete_category, name = "delete_category"),
    path('category/add_category/', views.add_category, name = "add_category"),
    
    # Blog URLS // CRUD operations

    path('blog/', views.blog, name = "blog_posts"),
    path('blog/add_blog/', views.add_blog, name = "add_blog"),
    path('blog/edit_blog/<int:id>/', views.edit_blog, name = "edit_blog"),
    path('blog/delete_blog/<int:id>/', views.delete_blog, name = "delete_blog"),

    path('users/', views.users , name = "users"),
    path('users/add_users/',views.add_users, name = "add_users"),
    path('users/edit_user/<int:pk>/',views.edit_user, name = "edit_user"),
    path('user/delete/<int:pk>/', views.delete_user, name = "delete_user"),
    

]