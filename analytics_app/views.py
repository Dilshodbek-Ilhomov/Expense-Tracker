from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from transactions.models import Transaction

# Create your views here.

class AnalyticsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        total_income = (
            Transaction.objects.filter(
                owner=request.user,
                type="income"
            ).aggregate(
                total=Sum("amount")
            )["total"] or 0
        )

        total_expense = (
            Transaction.objects.filter(
                owner=request.user,
                type="expense"
            ).aggregate(
                total=Sum("amount")
            )["total"] or 0
        )

        transactions_count = (
            Transaction.objects.filter(
                owner=request.user
            ).count()
        )

        balance = total_income - total_expense

        return Response({
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance,
            "transactions_count": transactions_count,
        })