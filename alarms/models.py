from django.db import models

class Alarm (models.Model):
    hora= models. CharField(max_length=5)

    def __str__(self) :
        return '{}'.format(self.hora)