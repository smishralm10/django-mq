import pandas as pd
import os
import sys
import random
from mq.celery import app
from celery import shared_task
from .models import Employee, AsyncResults
from django.http import HttpResponse
from django.conf import settings

@shared_task(bind=True)
def createCSV(self, amount):
    columns = ['id', 'gender', 'education_level', 'relationship_status', 'growth_rate', 'unit', 'attrition_rate']
    employees = Employee.objects.all()[:int(amount)].values(*columns)

    employees_df = pd.DataFrame.from_records(employees, columns=columns)
    filename = str(random.randint(1000000, 100000000000)) + '.csv'
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    employees_df.to_csv(file_path, index=False)
    try:
        result = 200
        async_result = AsyncResults.objects.create(task_id=self.request.id, result=result, location=file_path, filename=filename)
        async_result.save()
    except:
        result = str(sys.exc_info()[0])
        async_result = AsyncResults.objects.create(task_id=task_id, result=result)
        async_result.save()


