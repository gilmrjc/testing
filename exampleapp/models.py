from django.db import models

# Create your models here.
class Example(models.Model):
    example_field = models.CharField(max_length=50)
