
from django.urls import path
from . import views

urlpatterns = [
    #operation
    path('', views.liste_operations, name='liste_operations'),
    path('ajouter/', views.ajouter_operation, name='ajouter_operation'),
    path('operation/<int:operation_id>/', views.afficher_operation, name='afficher_operation'),
    path('operation/<int:operation_id>/modifier/', views.modifier_operation, name='modifier_operation'),
    path('operation/<int:operation_cible_id>/lier/<int:operation_a_lier_id>/', views.lier_operation, name='lier_operation'),
    path('operation/<int:operation_id>/ajouter-operation-liee/', views.ajouter_operation_liee, name='ajouter_operation_liee'),
    path('operation/<int:operation_id>/ajouter-contrat/', views.ajouter_contrat, name='ajouter_contrat'),

    # Collectivités
    path('collectivites/', views.liste_collectivites, name='liste_collectivites'),
    path('collectivites/ajouter/', views.ajouter_collectivite, name='ajouter_collectivite'),
    path('collectivite/<int:pk>/', views.afficher_collectivite, name='afficher_collectivite'),
    path('collectivite/<int:pk>/modifier/', views.modifier_collectivite, name='modifier_collectivite'),

    # Entreprises
    path('entreprises/', views.liste_entreprises, name='liste_entreprises'),
    path('entreprises/ajouter/', views.ajouter_entreprise, name='ajouter_entreprise'),
    path('entreprise/<int:pk>/', views.afficher_entreprise, name='afficher_entreprise'),
    path('entreprise/<int:pk>/modifier/', views.modifier_entreprise, name='modifier_entreprise'),

    # Sous-opérations
    path('sous-operations/', views.liste_sous_operations, name='liste_sous_operations'),
    path('sous-operations/ajouter/', views.ajouter_sous_operation, name='ajouter_sous_operation'),    
    path('sous-operations/ajouter/<int:operation_id>/', views.ajouter_sous_operation, name='ajouter_sous_operation_pour_operation'),
    path('sous-operation/<int:sous_operation_id>/delier/', views.delier_sous_operation, name='delier_sous_operation'),
]
