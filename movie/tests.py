from django.test import TestCase

class DemoTest(TestCase):

    def test_add(self):
        self.assertEqual(10 + 10, 30)

