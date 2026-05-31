from django.contrib import admin

from blogs.models import Category
from blogs.models import Blog


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}   
    list_display = ('title','author','status','is_featured','crated_at')
    # list_filter = ('status','is_featured','author') 
    search_fields = ('title','author__username','Category__category_name')
    list_editable= ('status','is_featured')


# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)