from django.db import models

# Create your models here.

class Artiste(models.Model):
    STYLE = [
        ('POP','POP'),
        ('RAP', 'RAP'),
        ('CLASSIC', 'CLASSIC'),
        ('ROCK', 'ROCK'),
        ('UNDEFINED', 'UNDEFINED'),
    ]
    nom = models.CharField(max_length=30)
    style = models.CharField(choices=STYLE, default='RAP',max_length=10)

class Chanson(models.Model):
    titre = models.CharField(max_length=30)
    duree = models.TimeField()
    date = models.DateField()
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)