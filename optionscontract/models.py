from django.db import models
import datetime

# Create your models here.

class OptionsContract(models.Model):
    CONTRACT_CHOICES = [
        ('CALL', 'Call'),
        ('PUT', 'Put'),
    ]

    POSITION_CHOICES=[
        ('BUY', 'Buy'),
        ('SELL', 'Sell')
    ]

    ticker = models.CharField(max_length=6)
    contract_type = models.CharField(choices=CONTRACT_CHOICES, max_length=4)
    position_type = models.CharField(choices=POSITION_CHOICES, max_length=4)
    expiration = models.DateField()
    strike_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_opened = models.DateField()
    date_closed = models.DateField(null=True, blank=True)
    closing_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    closed = models.BooleanField(default=False)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)