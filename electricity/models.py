from django.db import models

# Create your models here.
class Electricity_Expense(models.Model):
    units = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    cost = models.DecimalField(default=0.0, max_digits=6, decimal_places=2)

    def __str__(self):
        return f'Units bought: {self.units} on {self.date} at R{self.cost/self.units}/unit'