from io import BytesIO
import magic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import pyqrcode

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
        voucher = form.save()
        svg = create_qr_svg(voucher.code)
        return render(request, "success.html", {"qr": svg, "qrcode": voucher.code})

    return redirect('generator')


def create_qr_svg(code):
    qr = pyqrcode.create(code)

    stream = BytesIO()
    qr.svg(stream, scale=5)
    svg = stream.getvalue().decode()

    return svg


def download_voucher(request, code):
    qr = pyqrcode.create(code)

    stream = BytesIO()
    qr.png(stream, scale=5)
    png = stream.getvalue()

    content_type = magic.from_buffer(png, mime=True)
    response = HttpResponse(png, content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename=Voucher.png'
    return response
