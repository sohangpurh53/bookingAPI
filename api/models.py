from django.db import models

# Create your models here.
class registration(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Mobile_no = models.CharField(max_length=10)
    Pnr_no = models.CharField(max_length=10)
    Date = models.DateField()