from django.test import TestCase, Client
from django.urls import reverse
from authentification.models import *


class TestViews(TestCase):
  """_summary_

  Args:
      TestCase (_type_): _description_
  """

  def setUp(self):
    """_summary_
    """

    self.home_url = reverse('home')

  def test_home_GET(self):
    """_summary_
    """

    response = self.client.get(self.home_url)

    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'home.html')
