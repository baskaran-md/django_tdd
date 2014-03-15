from django.test import TestCase

class DemoTest(TestCase):

    def test_add(self):
        self.assertEqual(10 + 10, 20)

    def test_subtract(self):
        self.assertEqual(10 - 10, 0)

    def test_multiply(self):
        self.assertEqual(10 * 10, 100)