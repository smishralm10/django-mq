from django.db import models

# Create your models here.
class Employee(models.Model):
    gender = models.CharField(max_length=50)
    education_level = models.IntegerField(blank=True, null=True)
    relationship_status = models.CharField(max_length=50)
    growth_rate = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=50)
    attrition_rate = models.DecimalField(decimal_places=5, max_digits=6, blank=True, null=True)

class AsyncResults(models.Model):

  task_id = models.CharField(blank=False, max_length=255, null=False, verbose_name=("task id"), db_index=True)
  result = models.TextField(blank=False, verbose_name=("task result"))
  location = models.CharField(blank=False, max_length=400, null=False, db_index=True)
  filename = models.CharField(blank=False, max_length=255, null=False, db_index=True)
  created_on = models.DateTimeField(auto_now_add=True, db_index=True, editable=False, verbose_name=("created_on"))