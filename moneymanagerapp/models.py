from django.db import models


class Account(models.Model):
  bank_name = models.CharField(max_length = 100)
  currency = models.CharField(max_length = 100)
  amount = models.DecimalField(max_digits= 1000000, decimal_places = 2)

class Expense(models.Model):
  value = models.DecimalField(max_digits= 1000000, decimal_places = 2)
  date = models.DateTimeField()
  account = models.ForeignKey(Account, on_delete = models.CASCADE)

class Income(models.Model):
  value = models.DecimalField(max_digits= 1000000, decimal_places = 2)
  date = models.DateTimeField()
  account = models.ForeignKey(Account, on_delete = models.CASCADE)

