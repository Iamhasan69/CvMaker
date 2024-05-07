from django.db import models
from django_mysql import models as sqlmodel

# Create your models here.
class CVINFO(models.Model):
    full_name = models.CharField(max_length=80)
    job_role = models.CharField(max_length=40, default=None)
    contc_info = models.CharField(max_length=90)
    email_info = models.EmailField(blank=False)
    location = models.CharField(max_length=120)
    profile_summary = models.TextField()
    education = models.CharField(max_length=200)
    skills = sqlmodel.ListCharField(base_field=models.CharField(max_length=100),max_length=10)
    projects = sqlmodel.ListTextField(base_field=models.CharField(max_length=225))
    other_info = models.TextField(blank=True)
