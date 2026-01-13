from django.urls import path
from product.views import (
    categories_detail_api_view,
    categories_list_api_view, 
    products_detail_api_view, 
    products_list_api_view,
    reviews_detail_api_view,
    reviews_list_api_view
    )

urlpatterns = [
    path('', products_list_api_view),
    path('<int:product_id>/', products_detail_api_view),
    path('<int:product_id>/reviews/', reviews_list_api_view),
    path('categories/', categories_list_api_view),
    path('categories/<int:category_id>/', categories_detail_api_view),
    path('reviews/', reviews_list_api_view),
    path('reviews/<int:review_id>/', reviews_detail_api_view)
]