from django.shortcuts import render, redirect

from models.models import Voucher
from generator.views import create_qr_svg


def home_page(request):
    vouchers = Voucher.objects.all()
    return render(request, 'homepage.html', {"vouchers": vouchers})


def detail_voucher(request, code):
    voucher = Voucher.objects.get(code=code)
    svg = create_qr_svg(code)
    return render(request, 'detail.html', {'voucher': voucher, 'qr': svg})


def delete_voucher(request, code):
    voucher = Voucher.objects.get(code=code)
    voucher.delete()
    return redirect('home')


def delete_all_vouchers(request):
    vouchers = Voucher.objects.all()
    vouchers.delete()
    return redirect('home')
