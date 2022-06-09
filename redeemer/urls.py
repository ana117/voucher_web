from django.urls import path
from .views import redeem_page

urlpatterns = [
    path('', redeem_page, name='redeemer'),
]
