
from django import forms
from .models import Operation, Collectivite, Entreprise, SousOperation, OperationLiee, Contrat, LibelleContrat

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['titre', 'description', 'date', 'statut', 'technicien', 'collectivite', 'entreprise', 'type_operation', 'service']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['collectivite'].required = True

class CollectiviteForm(forms.ModelForm):
    class Meta:
        model = Collectivite
        fields = ['nom', 'code_insee', 'elu']

class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['nom', 'domaine', 'contact']

class SousOperationForm(forms.ModelForm):
    class Meta:
        model = SousOperation
        fields = ['titre', 'description', 'date', 'statut', 'operation', 'entreprise']

class OperationLieeForm(forms.ModelForm):
    class Meta:
        model = OperationLiee
        fields = ['titre', 'description', 'date', 'statut', 'operation', 'entreprise', 'operation_liee']

class ContratForm(forms.ModelForm):

    class Meta:
        model = Contrat
        fields = ['libelle', 'description', 'date', 'statut', 'operation', 'entreprise']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['libelle'].choices = [
            (lib.libelle, lib.libelle) for lib in LibelleContrat.objects.all()
        ]
