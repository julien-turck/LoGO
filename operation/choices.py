
# LoGO/choices.py

# Liste des services

CONTRAT_TITRE_CHOICES = [
	('CT', 'CT'),
	('DIAG_AMIANTE', 'Diag amiante'),
	('DIAG_STRUCTURE', 'Diag structure'),
	('MOE', 'MOE'),
	('MTR', 'MTR'),
	('SPS', 'SPS'),
	('AUTRE', 'Autre')
]

SERVICE_CHOICES = [
	('---', '---'),
	('assistance juridique', 'Assistance juridique'),
	('bâtiment', 'Bâtiment'),
	('conseil en énergie', 'Conseil en énergie'),
	('informatique', 'Informatique'),
	('voirie', 'Voirie'),
]

STATUT_CHOICES = [
	('A_FAIRE', 'À faire'),
	('EN_COURS', 'En cours'),
	('TERMINE', 'Terminé'),
]

# Liste des types d'opérations
TYPE_CHOICES = [
	('---', '---'),
	('MNE', 'Maintenance du Numérique Éducatif'),
	('AMO', 'Assistance à Maîtrise d’Ouvrage'),
]
