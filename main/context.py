from .models import Category

def get_categories(request):
    categorys=Category.objects.filter(parent__isnull=True)
    return {'categorys':categorys}