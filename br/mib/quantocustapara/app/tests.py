#-*- coding: utf-8 -*-
"""
    Primeiro vem os tests do selenium, depois os testes unitários
"""
from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from models import CloudTag
from buscape import Buscape
from settings import BUSCAPE_APP_ID 

import unittest

class SearchTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_search_churrasco(self):
        # Gertrude opens her web browser, and goes to the main page
        self.browser.get(self.live_server_url)

        # Quanto custa para ?
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Quanto Custa Para', body.text)

        search_field = self.browser.find_element_by_name('search')
        search_field.send_keys('churrasco')
        search_field.send_keys(Keys.RETURN)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('churrasco', body.text)

class ModelTest(TestCase):
    def test_save_tag(self):
        
        CloudTag.objects.delete()
        
        tag = CloudTag()
        tag.name = "brigadeiro"
        tag.size = "large"
        
        tag.save()
        
        all_tags_in_database = CloudTag.objects.all()
        
        self.assertEquals(len(all_tags_in_database),1)
        only_tag_in_database = all_tags_in_database[0]
        self.assertEquals(only_tag_in_database, tag)
        
        self.assertEquals(only_tag_in_database.name, "brigadeiro")
        self.assertEquals(only_tag_in_database.size, "large")
        
    def test_article(self):
        
        tag = CloudTag()
        tag.name = "torta"
        
        self.assertEquals(tag.article(),"a")

class BuscapeTest(TestCase):
    
    def setUp(self):
        
        buscape = Buscape(BUSCAPE_APP_ID)

        self.response = buscape.find_offer_list(keyword='picanha')

    def test_offer_list(self):
        
        try:
            offer = self.response['data']['offer'][0]['offer'];
            
            self.assertIsNotNone(offer['price']['value'])
            self.assertIsNotNone(offer['thumbnail']['url'])
            self.assertIsNotNone(offer['seller']['sellername'])
            
        except( KeyError ) :
            self.fail("Api Quebrada")    
        
    @unittest.expectedFailure
    def test_broken_offer(self):

        self.response['data']['minha_vo_pelada']