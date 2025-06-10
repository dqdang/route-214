# packs/models.py

from django.db import models

class BoosterPack(models.Model):
    tier = models.CharField(max_length=50)
    set_name = models.CharField(max_length=100)
    release_date = models.DateField()
    price_range = models.FloatField(default=0.0)
    price_charting_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.set_name

    # Add a method to parse the price_range string
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
