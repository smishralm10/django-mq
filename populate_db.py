import os
import pandas as pd
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mq.settings")
import django
django.setup()
from app.models import Employee

df = pd.read_csv('Train.csv')
cols = ['Gender', 'Education_Level', 'Relationship_Status', 'Unit', 'growth_rate', 'Attrition_rate']
df = df[cols]
data = 2000
if len(Employee.objects.all()) > 1:
    Employee.objects.all().delete()
for i in range(data):
    employee = Employee.objects.create()
    employee.gender = str(df['Gender'][i])
    employee.education_level = int(df['Education_Level'][i])
    employee.relationship_status = str(df['Relationship_Status'][i])
    employee.unit = str(df['Unit'][i])
    employee.growth_rate = int(df['growth_rate'][i])
    employee.attrition_rate = float(df['Attrition_rate'][i])
    employee.save()

