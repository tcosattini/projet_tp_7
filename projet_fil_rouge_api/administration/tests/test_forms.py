from django.test import SimpleTestCase
from administration.forms import TUtilisateurForm
from authentification.models import TUtilisateur


class TestForms(SimpleTestCase):
  """_summary_

  Args:
      SimpleTestCase (_type_): _description_
  """

  def test_tUtilisateur_form_invalid_(self):
    """_summary_
    """

    form = TUtilisateurForm(data={

    })
