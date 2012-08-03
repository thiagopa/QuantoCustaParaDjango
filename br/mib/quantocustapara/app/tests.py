"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from models import CloudTag

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
        self.assertIn('Quanto Custa Para', body.text)

        # TODO: use the admin site to create a Poll
        self.fail('finish this test')
        
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