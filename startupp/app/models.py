from django.db import models

# Create your models here.
class Employee(models.Model):
    Lead = models.CharField(max_length = 40)
    ID = models.CharField(max_length = 40, primary_key=True)
    Services = models.CharField(max_length = 40)
    Domain = models.CharField(max_length = 40)
    Channels = models.CharField(max_length = 40)
    Stage = models.CharField(max_length = 40)
    Status = models.CharField(max_length = 40)
    Amount = models.CharField(max_length = 40)
    Sale_Representative = models.CharField(max_length=100)
    Created_at = models.CharField(max_length = 40)
    Signed_at = models.CharField(max_length = 40)
    Closed_at = models.CharField(max_length = 40)
