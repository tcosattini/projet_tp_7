from django.test import TestCase
from administration.forms import *
from authentification.models import *

class TestFormsTUtilisteur(TestCase):

    #Tester l'utilisation du formulaire pour un ajout
    def test_ajout(self):
        #Création d'un rôle pour le test
        test_role1 = TRole.objects.create()
        #Création du formulaire à tester
        form = TUtilisateurForm(data = {
            'nom_utilisateur': "Dupont",
            'prenom_utilisateur': "Ariane",
            'code_role': test_role1,
            'is_superuser': False,
            'is_active': True,
        })
        #Valeur du test
        self.assertTrue(form.is_valid())
    
    #Tester l'utilisation du formulaire pour une modification
    def test_ajout(self):
        #Création d'un utilisateur pour le test
        test_utilisateur1 = TUtilisateur.objects.create(username = "test_utilisateur1")
        #Création d'un rôle pour le test
        test_role1 = TRole.objects.create()
        #Création du formulaire à tester
        form = TUtilisateurForm(data = {
            'nom_utilisateur': "Dupont",
            'prenom_utilisateur': "Ariane",
            'code_role': test_role1,
            'is_superuser': False,
            'is_active': True,
        }, instance=test_utilisateur1)
        #Valeur du test
        self.assertTrue(form.is_valid())