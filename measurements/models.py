from pyexpat import model
from django.db import models

from variables.models import Variable
from alarms.models import Alarm


class Measurement (models.Model):
    variable= models.ForeignKey(Variable, on_delete=models.CASCADE, default=None)
    value= models.FloatField(null=True, blank=True, default=None)
    unit= models.CharField(max_length=50)
    place= models.CharField(max_length=50)
    dateTime= models.DateField(auto_now_add=True)
    alarm= models.ManyToManyField(Alarm)

    def __str__(self) :
        return '%s %s' % (self.value, self.unit)
