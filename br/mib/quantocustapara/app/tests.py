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
    
    TEST_NAME = "testName"
    TEST_SIZE = "testSize"
    
    def test_save_tag(self):
        
        tag = CloudTag(name=self.TEST_NAME,size=self.TEST_SIZE)
        
        tag.save()
        
        test_tag = CloudTag.objects(name=self.TEST_NAME).first()
        
        self.assertEquals(test_tag, tag)
        
        self.assertEquals(test_tag.name, self.TEST_NAME)
        self.assertEquals(test_tag.size, self.TEST_SIZE)
        
        tag.delete()
        
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
            offer = self.response.offer[0].offer;
            
            self.assertIsNotNone(offer.price.value)
            self.assertIsNotNone(offer.thumbnail.url)
            self.assertIsNotNone(offer.seller.sellername)
            
        except( KeyError ) :
            self.fail("Api Quebrada")    
        
    @unittest.expectedFailure
    def test_broken_offer(self):

        self.response.minha_vo_pelada