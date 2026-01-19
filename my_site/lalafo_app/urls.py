from django.urls import path
from .views import CategoryViews, ProductViews, ProductCreateViews,ProductDetailViews

urlpatterns = [
    path('category/', CategoryViews.as_view(), name='categories'),
    path('', ProductViews.as_view(), name='product_list' ),
    path('create/', ProductCreateViews.as_view(), name='product_create'),
    path('<int:pk>', ProductDetailViews.as_view(), name='product_detail')
]