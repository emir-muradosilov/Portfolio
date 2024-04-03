from django.db import models

# Create your models here.

class Project(models.Model):
    tittle = models.CharField(max_length = 100)
    discriptions = models.CharField(max_length =250)
    image = models.ImageField(upload_to ='portfolioapp/images/')
    url = models.URLField(blank = True)
