from django.contrib.auth.models import User 

from django.db import models

# Creating category model 
class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta : 
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
    

# creating blog model 
STATUS_CHOICES= (
    ("Draft","Draft"),
    ("Publish","Publish"), 
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 150 , unique=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    featured_image = models.ImageField(upload_to = 'uploads/%y/%m/%d/')
    short_description = models.TextField(max_length=300)
    blog_body = models.TextField(max_length = 5000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog , on_delete=models.CASCADE) 
    # if blog is deleted then comment also get deleted 
    comment = models.TextField(max_length=100)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


