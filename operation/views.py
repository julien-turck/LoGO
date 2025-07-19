

from django.shortcuts import render, redirect, get_object_or_404
from .models import Operation, Collectivite, Entreprise, SousOperation, OperationLiee, LibelleContrat
from .forms import OperationForm, CollectiviteForm, EntrepriseForm, SousOperationForm, OperationLieeForm, ContratForm

#operations
def liste_operations(request):
    operations = Operation.objects.all().order_by('-date')
    # récupère l’ID de l’opération cible
    operation_cible_id = request.GET.get('lier_a')
    operation_cible = None  
    # Récupère les IDs des opérations déjà liées comme sous-opérations
    operations_deja_liees = SousOperation.objects.values_list('titre', flat=True)

    if operation_cible_id:
        try:
            operation_cible = Operation.objects.get(id=operation_cible_id)
        except Operation.DoesNotExist:
            operation_cible = None

    return render(request, 'operation/liste_operations.html', {
        'operations': operations,
        'operation_cible_id': operation_cible_id,
        'operations_deja_liees': operations_deja_liees,
        'operation_cible' : operation_cible
    })

def ajouter_operation(request):
    if request.method == 'POST':
        form = OperationForm(request.POST)
        if form.is_valid():
            operation = form.save(commit=False)
            if not operation.collectivite:
                form.add_error('collectivite', "veuillez sélectionner une collectivité")
            else:
                form.save()
                return redirect('liste_operations')
    else:
        form = OperationForm()
    return render(request, 'operation/ajouter_operation.html', {'form': form})

def afficher_operation(request, operation_id):
    operation = get_object_or_404(Operation, id=operation_id)
    sous_operations = operation.sousoperation_set.all()
    return render(request, 'operation/afficher_operation.html', {
        'operation': operation,
        'sous_operations': sous_operations
    })

def modifier_operation(request, operation_id):
    operation = get_object_or_404(Operation, id=operation_id)
    if request.method == 'POST':
        form = OperationForm(request.POST, instance=operation)
        if form.is_valid():
            form.save()
            return redirect('afficher_operation', operation_id=operation.id)
    else:
        form = OperationForm(instance=operation)
    return render(request, 'operation/modifier_operation.html', {'form': form, 'operation': operation})

def lier_operation(request, operation_cible_id, operation_a_lier_id):
    try:
        operation_cible = Operation.objects.get(id=operation_cible_id)
        operation_a_lier = Operation.objects.get(id=operation_a_lier_id)

        #Empêche de lier une opération à elle-même
        if operation_cible_id == operation_a_lier.id:
            return redirect ('afficher_operation', operation_id=operation_cible.id)

        # Vérifie si une sous-opération existe déjà
        existe_deja = SousOperation.objects.filter(
            operation=operation_cible,
            titre__icontains=operation_a_lier.titre
        ).exists()

        # Crée une sous-opération liée
        if not existe_deja and not operation_a_lier.est_liee:
            OperationLiee.objects.create(
                titre=f"{operation_a_lier.titre}",
                description=operation_a_lier.description,
                date=operation_a_lier.date,
                statut='A_FAIRE',
                operation=operation_cible,
                entreprise=operation_a_lier.entreprise,
                operation_liee=operation_a_lier
            )
            operation_a_lier.est_liee = True
            operation_a_lier.save()

        return redirect('afficher_operation', operation_id=operation_cible.id)

    except Operation.DoesNotExist:
        # Optionnel : tu peux afficher un message d’erreur ou rediriger ailleurs
        return HttpResponseRedirect(reverse('liste_operations'))

# Collectivités
def liste_collectivites(request):
    collectivites = Collectivite.objects.all()
    return render(request, 'operation/liste_collectivites.html', {'collectivites': collectivites})

def afficher_collectivite(request, pk):
    collectivite = get_object_or_404(Collectivite, pk=pk)
    operations = collectivite.operations.all()
    return render(request, 'operation/afficher_collectivite.html', {
        'collectivite': collectivite,
        'operations': operations
    })

def ajouter_collectivite(request):
    if request.method == 'POST':
        form = CollectiviteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_collectivites')
    else:
        form = CollectiviteForm()
    return render(request, 'operation/ajouter_collectivites.html', {'form': form})

def modifier_collectivite(request, pk):
    collectivite = get_object_or_404(Collectivite, pk=pk)
    if request.method == 'POST':
        form = CollectiviteForm(request.POST, instance=collectivite)
        if form.is_valid():
            form.save()
            return redirect('afficher_collectivite', pk=pk)
    else:
        form = CollectiviteForm(instance=collectivite)
    return render(request, 'operation/modifier_collectivite.html', {'form': form, 'collectivite': collectivite})

# Entreprises
def liste_entreprises(request):
    entreprises = Entreprise.objects.all()
    return render(request, 'operation/liste_entreprises.html', {'entreprises': entreprises})

def afficher_entreprise(request, pk):
    entreprise = get_object_or_404(Entreprise, pk=pk)
    operations = entreprise.operations.filter(est_liee=False)
    sous_operations = entreprise.sous_operations.all()
    elements = list(operations) + list(sous_operations)

    return render(request, 'operation/afficher_entreprise.html', {
        'entreprise': entreprise,
        'elements' : elements    
    })

def ajouter_entreprise(request):
    if request.method == 'POST':
        form = EntrepriseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_entreprises')
    else:
        form = EntrepriseForm()
    return render(request, 'operation/ajouter_entreprises.html', {'form': form})

def modifier_entreprise(request, pk):
    entreprise = get_object_or_404(Entreprise, pk=pk)
    if request.method == 'POST':
        form = EntrepriseForm(request.POST, instance=entreprise)
        if form.is_valid():
            form.save()
            return redirect('afficher_entreprise', pk=pk)
    else:
        form = EntrepriseForm(instance=entreprise)
    return render(request, 'operation/modifier_entreprise.html', {'form': form, 'entreprise': entreprise})

# Sous-opérations
def liste_sous_operations(request):
    sous_operations = SousOperation.objects.all()
    return render(request, 'operation/liste_sous_operations.html', {'sous_operations': sous_operations})

def ajouter_sous_operation(request, operation_id=None):
    if request.method == 'POST':
        form = SousOperationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('afficher_operation', operation_id=form.cleaned_data['operation'].id)
    else:
        if operation_id:
            form = SousOperationForm(initial={'operation': operation_id})
        else:
            form = SousOperationForm()
    return render(request, 'operation/ajouter_sous_operation.html', {'form': form})

def delier_sous_operation(request, sous_operation_id):
    sous_operation = get_object_or_404(SousOperation, id=sous_operation_id)
    operation_id = sous_operation.operation.id

    try:
        operation_liee = OperationLiee.objects.get(id=sous_operation_id)
        if operation_liee.operation_liee:
            operation_liee.operation_liee.est_liee = False
            operation_liee.operation_liee.save()
        operation_liee.delete()
    except OperationLiee.DoesNotExist:
        sous_operation.delete()
    return redirect('afficher_operation', operation_id=operation_id)

def ajouter_operation_liee(request, operation_id=None):
    if request.method == 'POST':
        form = OperationLieeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('afficher_operation', operation_id=form.cleaned_data['operation'].id)
        else:
            form = OperationLieeForm(initial={'operation': operation_id} if operation_id else None)
        return render(request, 'operation/ajouter_operation_liee.html', {'form': form})


def ajouter_contrat(request, operation_id=None):
    if request.method == 'POST':
        print("Formulaire soumis")

        nouveau_libelle = request.POST.get('nouveau_libelle', '').strip()
        post_data = request.POST.copy()

        if nouveau_libelle:
            libelle_obj, created = LibelleContrat.objects.get_or_create(libelle=nouveau_libelle)
            print("LibelleContrat créé ou récupéré :", libelle_obj)

            # Injecte l'ID dans le champ 'libelle'
            post_data['libelle'] = str(libelle_obj.id)

        form = ContratForm(post_data)
        # Mise à jour explicite du queryset
        form.fields['libelle'].queryset = LibelleContrat.objects.all()

        if form.is_valid():
            print("Formulaire valide")
            contrat = form.save(commit=False)

            # Sécurité : on force l'opération si elle n'est pas transmise correctement
            if not contrat.operation_id and operation_id:
                contrat.operation_id = operation_id

            contrat.save()
            print("Contrat enregistré :", contrat)
            return redirect('afficher_operation', operation_id=contrat.operation.id)
        else:
            print("Formulaire invalide :", form.errors)
            return render(request, 'operation/ajouter_contrat.html', {'form': form})
    else:
        form = ContratForm(initial={'operation': operation_id} if operation_id else None)
        return render(request, 'operation/ajouter_contrat.html', {'form': form})
