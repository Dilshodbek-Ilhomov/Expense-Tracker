from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializers import TransactionSerializer

# Create your views here.

class TransactionListCreateAPIView(ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):

        transaction = serializer.save(
            owner=self.request.user
        )

        wallet = transaction.wallet

        if transaction.type == "income":
            wallet.balance += transaction.amount
        elif transaction.type == "expense":
            wallet.balance -= transaction.amount

        wallet.save()
