from django.urls import path
from home.views import home_page, detail_voucher, delete_voucher, delete_all_vouchers

urlpatterns = [
    path('', home_page, name='home'),
    path('detail/<str:code>', detail_voucher, name='detail'),
    path('delete/<str:code>', delete_voucher, name='delete'),
    path('deleteall', delete_all_vouchers, name='delete_all')
]
