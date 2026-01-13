from django.urls import path
from users.views import autherization_api_view, register_api_view, user_confirm_api_view

urlpatterns = [
    path('register/', register_api_view),
    path('autherization/', autherization_api_view),
    path('confirm/', user_confirm_api_view)
]
