from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, DetailView,
                                  UpdateView, DeleteView)
from .models import Category,Product
from .forms import ProductForm

class CategoryViews(ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'category_list.html'

class ProductViews(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product_list.html'

class ProductCreateViews(CreateView):
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')

class ProductDetailViews(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'product'
    template_name = 'product_detail.html'


class ProductUpdateViews(UpdateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    template_name = 'product_update.html'

class ProductDeleteViews(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')


