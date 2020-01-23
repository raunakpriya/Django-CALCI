from django.db import models

# Create your models here.
class Destination(models.Model):
    operator=models.CharField(max_length=1)
    num1=models.IntegerField()
    num2=models.IntegerField()
    res=models.IntegerField()

def __str__(self):
        return self.res
