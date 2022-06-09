from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

from models.forms import VoucherForm
from models.models import Voucher


def code_generator():
    code_length = 12
    new_code = get_random_string(code_length)
    while Voucher.objects.only("code").filter(code=new_code).exists():
        new_code = get_random_string(code_length)
    return new_code


def generator_page(request):
    code = code_generator()
    return render(request, "generator-page.html", {"code": code})


def save_voucher(request):
    form = VoucherForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('success')

    return redirect('generator')


def success_page(request):
    return render(request, "success.html")
