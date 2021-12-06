from django.test import TestCase

from web_app.models import Employee
from web_app import solver


class TestModels(TestCase):

    def setUp(self):
        self.web_app = Employee.objects.create(name='test employee',
                                               shift=1,
                                               fte=0.5,
                                               active=True)

    def test_employee_model(self):
        d = self.web_app
        self.assertTrue(isinstance(d, Employee))
        self.assertEqual(str(d.name), 'test employee')
        self.assertEqual(d.shift, 1)
        self.assertEqual(d.fte, 0.5)
        self.assertEqual(d.active, True)
