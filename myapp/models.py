from django.db import models

# Create your models here.

class Point(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    adresse = models.CharField(max_length=255, blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Point ({self.latitude}, {self.longitude}) - {self.adresse}"