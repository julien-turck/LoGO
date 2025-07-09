from django.contrib import admin
from .models import Technicien, Operation, Entreprise, SousOperation, Collectivite

admin.site.register(Technicien)
admin.site.register(Operation)
admin.site.register(SousOperation)
admin.site.register(Entreprise)
admin.site.register(Collectivite)
