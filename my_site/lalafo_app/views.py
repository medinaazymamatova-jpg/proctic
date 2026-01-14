from django.views.generic import ListView
from .models import Category,Product

class CategoryViews(ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'category_list.html'

class ProductViews(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product_list.html'