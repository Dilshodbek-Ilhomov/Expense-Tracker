from .models import Transaction
from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ('owner', 'created_at')

    def validate(self, attrs):
        wallet = attrs["wallet"]
        amount = attrs["amount"]
        transaction_type = attrs["type"]

        if (
                transaction_type == "expense"
                and amount > wallet.balance
        ):
            raise serializers.ValidationError(
                "Not enough money"
            )

        return attrs