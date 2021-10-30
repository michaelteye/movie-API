from django.db import models

# Create your models here.

class Film(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    form = models.CharField(max_length=100, default='all kinds')
    image = models.ImageField(upload_to = 'Image/', default= 'Images/Nono/No.img')

    def __str__(self):
        return self.name
