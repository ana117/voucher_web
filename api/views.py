from django.http import JsonResponse
from rest_framework.decorators import api_view

from models.models import Voucher
from models.serializers import VoucherSerializer
from redeemer.views import redeem


@api_view(['POST'])
def redeem_api(request):
    data = request.data
    voucher_code = data.get('code', '')

    error = None
    voucher = Voucher()

    try:
        successfully_redeemed = redeem(voucher_code)
        voucher = Voucher.objects.get(code=voucher_code)
        if not successfully_redeemed:
            error = 'Voucher has been used'

    except Voucher.DoesNotExist:
        error = 'Code not found'

    serializer = VoucherSerializer(voucher)
    serialized_voucher = serializer.data
    return JsonResponse({'voucher': serialized_voucher, 'error': error})
