from rest_framework import serializers

from models.models import Voucher


class VoucherSerializer(serializers.Serializer):
    def create(self, validated_data):
        return Voucher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.is_used = validated_data.get('is_used', instance.is_used)
        instance.date_used = validated_data.get('date_used', instance.date_used)
        instance.save()
        return instance

    code = serializers.CharField(max_length=12)
    description = serializers.CharField()
    is_used = serializers.BooleanField()
    date_used = serializers.DateTimeField()
