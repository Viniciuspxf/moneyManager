from django.db import models


class Account(models.Model):
  bank_name = models.CharField()
  currency = models.CharField()
  amount = models.DecimalField(decimal_places=2)

class Expense(models.Model):
  value = models.DecimalField(decimal_places=2)
  date = models.DateTimeField()

class Income(models.Model):
  value = models.DecimalField(decimal_places=2)
  date = models.DateTimeField()

