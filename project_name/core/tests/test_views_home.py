# coding: utf-8
from django.test import TestCase


class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """
        GET / must return status code 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Index must use template base.html
        """
        self.assertTemplateUsed(self.resp, 'core/base.html')
