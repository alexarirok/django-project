from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=25)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"My name is {self.name}"

# Create your models here.
