from django.db import models

# Create your models here.
class Riddim(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')
    date = models.DateField(auto_now_add=True)