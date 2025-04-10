from django.db import models


class Location(models.Model):
    input_text = models.CharField(max_length=255)
    formatted_address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.formatted_address