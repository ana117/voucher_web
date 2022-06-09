from django.urls import path
from generator.views import generator_page, save_voucher, success_page

urlpatterns = [
    path('', generator_page, name='generator'),
    path('save/', save_voucher, name='save'),
    path('success/', success_page, name='success'),
]
