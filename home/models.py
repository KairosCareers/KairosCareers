from django.db import models

# Create your models here.
class Job(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    logo = models.ImageField(null=True, blank=True, upload_to='company_logos')

    def __str__ (self):
        return self.title