from blogs import models 

def get_categories(request):
    categories = models.Category.objects.all()
    return {'categories': categories}   
