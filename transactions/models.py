from django.db import models
from django.conf import settings
from wallets.models import Wallet

# Create your models here.

class Transaction(models.Model):
    TYPE_CHOICES = (
        ('income', 'Income'),
        ('expense', 'Expense')
    )
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
