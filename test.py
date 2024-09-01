import unittest
from evidencia4 import Smartphone

class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.mi_smartphone = Smartphone("Voltron X")

    def test_abrir_app_con_bateria_sufuciente(self):
        self.mi_smartphone.abrir_app(10)
        self.assertEqual(self.mi_smartphone.bateria, 90)
        self.assertEqual(self.mi_smartphone.apps_abiertas, 1)