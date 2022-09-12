from django.db import models

# Create company models here.
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    Company_name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(("IT","IT"),("NON-IT","NON-IT")))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
