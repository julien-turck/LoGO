

from django.shortcuts import render, redirect, get_object_or_404
from .models import Operation, Collectivite, Entreprise, SousOperation
from .forms import OperationForm, CollectiviteForm, EntrepriseForm, SousOperationForm

#operations
def liste_operations(request):
    operations = Operation.objects.all().order_by('-date')
    return render(request, 'operation/liste_operations.html', {'operations': operations})

def ajouter_operation(request):
    if request.method == 'POST':
        form = OperationForm(request.POST)
        if form.is_valid():
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

# Collectivités
def liste_collectivites(request):
    collectivites = Collectivite.objects.all()
    return render(request, 'operation/liste_collectivites.html', {'collectivites': collectivites})

def ajouter_collectivite(request):
    if request.method == 'POST':
        form = CollectiviteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_collectivites')
    else:
        form = CollectiviteForm()
    return render(request, 'operation/ajouter_collectivites.html', {'form': form})

# Entreprises
def liste_entreprises(request):
    entreprises = Entreprise.objects.all()
    return render(request, 'operation/liste_entreprises.html', {'entreprises': entreprises})

def ajouter_entreprise(request):
    if request.method == 'POST':
        form = EntrepriseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_entreprises')
    else:
        form = EntrepriseForm()
    return render(request, 'operation/ajouter_entreprises.html', {'form': form})

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
