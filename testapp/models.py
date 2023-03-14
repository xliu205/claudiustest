from django.db import models

# Create your models here.

class Accident(models.Model):
    
 
    name = models.CharField(max_length=100)
    GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES)

    # default True 
    description = models.CharField(max_length=100)
    annual_wage = models.FloatField()
    medical_expenses = models.FloatField()
    accident_date = models.DateField()


    class Meta:
        app_label = 'testapp'


