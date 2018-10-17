from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User



class NPModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    employee_count = models.IntegerField()
    operating_budget = models.FloatField()
    established_date = models.DateTimeField(default=datetime.now)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.name