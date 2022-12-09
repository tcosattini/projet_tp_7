from django.test import SimpleTestCase
from administration.forms import TUtilisateurForm
from authentification.models import TUtilisateur


class TestForms(SimpleTestCase):

    def test_tUtilisateur_form_invalid_(self):
        form = TUtilisateurForm(data={

        })
