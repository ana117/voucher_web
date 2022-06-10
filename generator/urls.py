from django.urls import path
from generator.views import generator_page, save_voucher, download_voucher

urlpatterns = [
    path('', generator_page, name='generator'),
    path('save/', save_voucher, name='save'),
    path('download/<str:code>', download_voucher, name='download'),
]
