"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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