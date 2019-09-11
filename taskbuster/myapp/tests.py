from django.test import TestCase
import unittest
from selenium import webdriver
# Create your tests here.


class NewVisitorTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django: the Web framework for perfectionists with deadlines.', self.browser.title)
