
from django.urls import path
from . import views

urlpatterns = [
    #operation
    path('', views.liste_operations, name='liste_operations'),
    path('ajouter/', views.ajouter_operation, name='ajouter_operation'),
    path('operation/<int:operation_id>/', views.afficher_operation, name='afficher_operation'),
    path('operation/<int:operation_id>/modifier/', views.modifier_operation, name='modifier_operation'),

    # Collectivités
    path('collectivites/', views.liste_collectivites, name='liste_collectivites'),
    path('collectivites/ajouter/', views.ajouter_collectivite, name='ajouter_collectivite'),

    # Entreprises
    path('entreprises/', views.liste_entreprises, name='liste_entreprises'),
    path('entreprises/ajouter/', views.ajouter_entreprise, name='ajouter_entreprise'),

    # Sous-opérations
    path('sous-operations/', views.liste_sous_operations, name='liste_sous_operations'),
    path('sous-operations/ajouter/', views.ajouter_sous_operation, name='ajouter_sous_operation'),    
    path('sous-operations/ajouter/<int:operation_id>/', views.ajouter_sous_operation, name='ajouter_sous_operation_pour_operation'),

]
