from django.db import models


class Voucher(models.Model):
    code = models.CharField(max_length=12, primary_key=True)
    description = models.TextField()
    is_used = models.BooleanField()
    date_used = models.DateTimeField(null=True)
