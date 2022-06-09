from django.forms import ModelForm

from models.models import Voucher


class VoucherForm(ModelForm):
    class Meta:
        model = Voucher
        fields = ["code", "description", "is_used"]

    def __init__(self, *args, **kwargs):
        super(VoucherForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
