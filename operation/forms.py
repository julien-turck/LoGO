
from django import forms
from .models import Operation, Collectivite, Entreprise, SousOperation

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
