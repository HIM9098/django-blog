from django.urls import path

from dashboards import views 

urlpatterns= [
    path('', views.dashboard, name='dashboard'),
    path('category/' , views.category , name = "category"),
    path('category/edit_category/<int:id>/',views.edit_category, name = "edit_category"),
    path('category/delete_category/<int:id>/',views.delete_category, name = "delete_category"),
    path('category/add_category/', views.add_category, name = "add_category"),

]