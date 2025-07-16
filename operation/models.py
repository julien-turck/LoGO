import datetime
from django.db import models
from .choices import SERVICE_CHOICES, TYPE_CHOICES, STATUT_CHOICES, CONTRAT_TITRE_CHOICES


class Technicien(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='---')

    def __str__(self):
        return self.nom

class Collectivite(models.Model):
    nom = models.CharField(max_length=200)
    code_insee = models.CharField(max_length=10)
    elu = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Entreprise(models.Model):
    nom = models.CharField(max_length=200)
    domaine = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Operation(models.Model):

    titre = models.CharField(max_length=200, default="Ecrire ici l'intitulé de l'opération")
    description = models.TextField(default="Ecrire ici une description de l'opéraion")
    date = models.DateField(default=datetime.date.today)
    collectivite = models.ForeignKey(Collectivite, on_delete=models.SET_NULL, related_name="operations", null=True, blank=True)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='A_FAIRE')
    technicien = models.ForeignKey(Technicien, on_delete=models.SET_NULL, null=True, blank=True, default=1)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.SET_NULL, related_name="operations", null=True, blank=True)
    type_operation = models.CharField(max_length=3, choices=TYPE_CHOICES, default='---')
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='---')
    est_liee = models.BooleanField(default=False)

    def __str__(self):
        return f"(self.titre) ({self.get_statut_display()})"

class SousOperation(models.Model):

    titre = models.CharField(max_length=200)
    description = models.TextField(default="Écrire ici une description de la sous-opération")
    date = models.DateField(default=datetime.date.today)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='A_FAIRE')
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE)
    entreprise = models.ForeignKey('Entreprise', on_delete=models.SET_NULL, related_name='sous_operations', null=True, blank=True)

    def __str__(self):
        return f"{self.titre} ({self.get_statut_display()})"

class OperationLiee(SousOperation):
    operation_liee = models.ForeignKey(
        'Operation',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lien_en_tant_que_sous_operation'
    )

class Contrat(SousOperation):
    libelle = models.CharField(max_length=100, choices=CONTRAT_TITRE_CHOICES)
    libelle_personnalise = models.CharField(max_length=200, blank=True, null=True)

    def get_titre_affiche(self):
        return self.libelle_personnalise if self.titre == 'AUTRE' else self.get_titre_display()