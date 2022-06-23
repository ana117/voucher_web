from django.urls import path
from .views import redeem_api

urlpatterns = [
    path('redeem', redeem_api, name='redeem_api'),
]
