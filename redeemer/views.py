from django.shortcuts import render
from models.models import Voucher

REDEEMER_PAGE = "redeemer-page.html"


def redeem_page(request):
    if request.method == "POST":
        voucher_code = request.POST.get("voucher_code")
        try:
            voucher = Voucher.objects.get(code=voucher_code)
            if voucher.is_used:
                return render(request, REDEEMER_PAGE, {"error": "Voucher has been used"})

            voucher.is_used = True
            voucher.save()
            return render(request, REDEEMER_PAGE, {"success": f"Code {voucher_code} has been redeemed!"})
        except Voucher.DoesNotExist:
            return render(request, REDEEMER_PAGE, {"error": "Code not found"})

    return render(request, REDEEMER_PAGE)
