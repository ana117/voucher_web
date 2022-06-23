from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from models.models import Voucher

REDEEMER_PAGE = "redeemer-page.html"


def redeem(voucher_code):
    voucher = Voucher.objects.get(code=voucher_code)
    if voucher.is_used:
        return False

    voucher.is_used = True
    voucher.date_used = timezone.now()
    voucher.save()
    return True


def redeem_page(request):
    if request.method == "POST":
        voucher_code = request.POST.get("voucher_code")
        try:
            successfully_redeemed = redeem(voucher_code)
            if successfully_redeemed:
                return render(request, REDEEMER_PAGE, {"success": f"Code {voucher_code} has been redeemed!"})
            else:
                return render(request, REDEEMER_PAGE, {"error": "Voucher has been used"})

        except Voucher.DoesNotExist:
            return render(request, REDEEMER_PAGE, {"error": "Code not found"})

    return render(request, REDEEMER_PAGE)
