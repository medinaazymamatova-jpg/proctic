from django.urls import path
from .views import CategoryViews, ProductViews

urlpatterns = [
    path('category/', CategoryViews.as_view(), name='categories'),
    path('product/', ProductViews.as_view(), name='product_list' )
]