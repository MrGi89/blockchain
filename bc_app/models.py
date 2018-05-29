from django.db import models
from django.contrib.postgres.fields import ArrayField, HStoreField


class Address(models.Model):

    address = models.CharField(max_length=128)
    hash160 = models.CharField(max_length=128)
    final_balance = models.BigIntegerField()
    n_tx = models.IntegerField()
    total_received = models.BigIntegerField()
    total_sent = models.BigIntegerField()


class Transaction(models.Model):

    block_height = models.IntegerField()
    double_spend = models.BooleanField()
    hash = models.CharField(max_length=128)
    relayed_by = models.CharField(max_length=128)
    size = models.IntegerField()
    time = models.IntegerField()
    tx_index = models.IntegerField()
    version = models.SmallIntegerField()
    inputs = ArrayField(
        HStoreField()
    )
    outputs = ArrayField(
        HStoreField()
    )
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, related_name='transactions')
