from rest_framework import serializers

from apps.bank.models import TransferMoney

class TransferMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferMoney
        fields = ('id', 'from_user', 'to_user', 'amount', 'status' , 'created')