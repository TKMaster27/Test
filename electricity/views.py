from django.shortcuts import render
from .models import Electricity_Expense

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def home(request):
    return render(request, 'charts.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        expenses = Electricity_Expense.objects.all()
        month_list = [i.month for i in Electricity_Expense.objects.values_list('date', flat=True)]
        averageU = 0
        averageC = 0
        labels = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        default_units = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        default_cost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for expense in expenses:
            for month in month_list:
                default_units.pop(month-1)
                default_cost.pop(month-1)
                default_units.insert(month-1, expense.units)
                default_cost.insert(month-1, expense.cost)
                month_list.pop(0)
                break
 
        for unit in default_units:
            averageU += unit

        for cost in default_cost:
            averageC += cost

        avgU = averageU/expenses.count()
        avgC = averageC/expenses.count()
        averageUnits = [avgU, avgU, avgU, avgU, avgU, avgU, avgU, avgU, avgU, avgU, avgU, avgU]
        averageCost = [avgC, avgC, avgC, avgC, avgC, avgC, avgC, avgC, avgC, avgC, avgC, avgC]
        data = {
            "labels": labels,
            "units": default_units,
            "cost": default_cost,
            "averageUnits": averageUnits,
            "averageCost": averageCost,
        }
        return Response(data)