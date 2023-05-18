from rest_framework import serializers

from .models import HistoryTransfer

class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = ('id', 'from_user', 'to_user','is_completed', 'created_at', 'amount')