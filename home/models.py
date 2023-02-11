from django.db import models

class Team(models.Model):
    country_name = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    points = models.CharField(max_length=255)

