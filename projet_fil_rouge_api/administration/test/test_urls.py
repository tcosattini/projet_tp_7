from django.test import SimpleTestCase
from django.urls import reverse, resolve
from administration.views import *

class TestUrls(SimpleTestCase):
    
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
        
    def test_ongletObjets_url_is_resolved(self):
        url = reverse('ongletObjets', args=['1'])
        self.assertEquals(resolve(url).func, ongletObjets)
        
    def test_ajoutObjet_url_is_resolved(self):
        url = reverse('ajoutObjet', args=['1','a','2','3','4','5','6'])
        self.assertEquals(resolve(url).func, ajoutObjet)
    
    def test_modificationObjet_url_is_resolved(self):
        url = reverse('modificationObjet', args=['1','2','a','3','4','5','6','7'])
        self.assertEquals(resolve(url).func, modificationObjet)
    
    def test_statusChangeObjet_url_is_resolved(self):
        url = reverse('statusChangeObjet', args=['1','2','0'])
        self.assertEquals(resolve(url).func, statusChangeObjet)
 
    def test_ongletConditionnement_url_is_resolved(self):
        url = reverse('ongletEmballages', args=['1'])
        self.assertEquals(resolve(url).func, ongletConditionnement)
        
    def test_ajoutConditionnement_url_is_resolved(self):
        url = reverse('ajoutConditionnement', args=['1','a','2','3'])
        self.assertEquals(resolve(url).func, ajoutConditionnement)
    
    def test_modificationConditionnement_url_is_resolved(self):
        url = reverse('modificationConditionnement', args=['1','2','a','3','4'])
        self.assertEquals(resolve(url).func, modificationConditionnement)
        
    def test_ongletCommunes_url_is_resolved(self):
        url = reverse('ongletCommunes', args=['1'])
        self.assertEquals(resolve(url).func, ongletCommunes)
        
    def test_ajoutCommune_url_is_resolved(self):
        url = reverse('ajoutCommune', args=['1','a','2','b'])
        self.assertEquals(resolve(url).func, ajoutCommune)
        
    def test_modificationCommune_url_is_resolved(self):
        url = reverse('modificationCommune', args=['1','2','a','3','b'])
        self.assertEquals(resolve(url).func, modificationCommune)
        
    def test_pagePoids_url_is_resolved(self):
        url = reverse('pagePoids', args=['1'])
        self.assertEquals(resolve(url).func, pagePoids)
        
    def test_ajoutPoids_url_is_resolved(self):
        url = reverse('ajoutPoids', args=['1','2','3'])
        self.assertEquals(resolve(url).func, ajoutPoids)
        
    def test_modifierPoids_url_is_resolved(self):
        url = reverse('modifierPoids', args=['1','2','3','4'])
        self.assertEquals(resolve(url).func, modifierPoids)
        
    def test_pagePoidsVignettes_url_is_resolved(self):
        url = reverse('pagePoidsVignettes', args=['1'])
        self.assertEquals(resolve(url).func, pagePoidsVignettes)
        
    def test_ajoutPoidsVignettes_url_is_resolved(self):
        url = reverse('ajoutPoidsVignettes', args=['1','2','3'])
        self.assertEquals(resolve(url).func, ajoutPoidsVignettes)
        
    def test_modifierPoidsVignettes_url_is_resolved(self):
        url = reverse('modifierPoidsVignettes', args=['1','2','3','4'])
        self.assertEquals(resolve(url).func, modifierPoidsVignettes)