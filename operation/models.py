import datetime
from django.db import models


class Technicien(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom

class Collectivite(models.Model):
    nom = models.CharField(max_length=200)
    code_insee = models.CharField(max_length=10)
    elu = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class Operation(models.Model):
    STATUT_CHOICES = [
        ('A_FAIRE', 'À faire'),
        ('EN_COURS', 'En cours'),
        ('TERMINE', 'Terminé'),
    ]

    titre = models.CharField(max_length=200, default="Ecrire ici l'intitulé de l'opération")
    description = models.TextField(default="Ecrire ici une description de l'opéraion")
    date = models.DateField(default=datetime.date.today)
    collectivite = models.ForeignKey(Collectivite, on_delete=models.SET_NULL, null=True, blank=True)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='A_FAIRE')
    technicien = models.ForeignKey(Technicien, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"(self.titre) ({self.get_statut_display()})"

class Entreprise(models.Model):
    nom = models.CharField(max_length=200)
    domaine = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class SousOperation(models.Model):
    STATUT_CHOICES = [
        ('A_FAIRE', 'À faire'),
        ('EN_COURS', 'En cours'),
        ('TERMINE', 'Terminé'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField(default="Écrire ici une description de la sous-opération")
    date = models.DateField(default=datetime.date.today)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='A_FAIRE')
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titre} ({self.get_statut_display()})"