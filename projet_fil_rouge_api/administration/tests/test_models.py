from django.test import TestCase
from authentification.models import *

class TestUtilisateurs(TestCase):

    #Tester le code des utilisateurs
    def test_utilisateurs_code(self):
        test_code1 = TUtilisateur.objects.create(code_utilisateur = 100, username = "test_code1")
        test_code2 = TUtilisateur.objects.create(username = "test_code2")
        #Vérifier que le code des deux utilisateurs n'est pas
        #identique, donc est unique, et automatiquement crée
        self.assertNotEqual(test_code1.code(), test_code2.code())
        #Vérifier que le code prend bien la valeur du
        #code incrémentée du dernier utilisateur crée avant celui-là 
        self.assertEqual(test_code2.code(), test_code1.code()+1)
    
    #Tester le nom des utilisateurs
    def test_utilisateurs_nom(self):
        test_nom1 = TUtilisateur.objects.create(nom_utilisateur = "Dupont", prenom_utilisateur = "Ariane", username = "test_nom1")
        test_nom2 = TUtilisateur.objects.create(nom_utilisateur = "Dupont", prenom_utilisateur = "Ariane", username = "test_nom2")
        #Vérifier que deux utilisateurs peuvent avoir le même nom et prénom
        #mais pas la même identité
        self.assertEqual(test_nom1.nom(), test_nom2.nom())
        self.assertEqual(test_nom1.prenom(), test_nom2.prenom())
        self.assertNotEqual(test_nom1.code(), test_nom2.code())
    
    #Tester le rôle d'un utilisateur
    def test_utilisateurs_role(self):
        test_role1 = TRole.objects.create()
        test_role_utilisateur1 = TUtilisateur.objects.create(code_role = test_role1, username = "test_role1")
        #Vérifer que le rôle est bien assigné
        self.assertEqual(test_role1, test_role_utilisateur1.coderole())
    
    #Tester l'attribut is_superuser des utilisateurs
    def test_utilisateurs_is_superuser(self):
        test_is_superuser1 = TUtilisateur.objects.create(username = "test_is_superuser1")
        #Vérifier que is_superuser est automatiquement à la valeur False
        self.assertEqual(test_is_superuser1.superuser(), False)
    
    #Tester l'attribut is_active des utilisateurs
    def test_utilisateurs_is_active(self):
        test_is_active1 = TUtilisateur.objects.create(username = "test_is_active1")
        #Vérifier que is_active est automatiquement à la valeur True
        self.assertEqual(test_is_active1.active(), True)


class TestCommunes(TestCase):

    #Tester le libélé de la commune
    def test_communes_str(self):
        test1 = TCommunes.objects.create(communes = "Libélé test")
        self.assertEqual(str(test1), "Libélé test")

