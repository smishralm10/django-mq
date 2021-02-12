import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mq.settings")
import django
import random
django.setup()
from app.models import Employee

data = 1000000
if len(Employee.objects.all()) > 1:
    Employee.objects.all().delete()
for i in range(data):
    employee = Employee.objects.create()
    employee.gender = 'Male'
    employee.education_level = random.randint(1, 10)
    employee.relationship_status = 'Single'
    employee.unit = 'IT'
    employee.growth_rate = random.randint(1, 10)
    employee.attrition_rate = float(0.0006)
    employee.save()

