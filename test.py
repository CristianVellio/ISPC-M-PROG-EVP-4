import unittest
from evidencia4 import Smartphone

class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.mi_smartphone = Smartphone("Voltron X")

    def test_abrir_app(self):
        test_cases = [
            {"bateria_inicial": 100, "consumo": 10, "bateria_esperada": 90, "apps_abiertas_esperadas": 1},
            {"bateria_inicial": 10, "consumo": 20, "bateria_esperada": 10, "apps_abiertas_esperadas": 0},
            {"bateria_inicial": 0, "consumo": 5, "bateria_esperada": 0, "apps_abiertas_esperadas": 0},
        ]
#Testeo Bateria
        for case in test_cases:
            with self.subTest(case=case):
                self.mi_smartphone._Smartphone__bateria = case["bateria_inicial"]
                self.mi_smartphone._Smartphone__apps_abiertas = 0  # Reset apps abiertas
                self.mi_smartphone.abrir_app(case["consumo"])
                self.assertEqual(self.mi_smartphone.get_bateria(), case["bateria_esperada"])
                self.assertEqual(self.mi_smartphone.get_apps_abiertas(), case["apps_abiertas_esperadas"])

    def test_cerrar_app(self):
        self.mi_smartphone.abrir_app(15)
        self.assertEqual(self.mi_smartphone.get_apps_abiertas(), 1)
        self.mi_smartphone.cerrar_app()
        self.assertEqual(self.mi_smartphone.get_apps_abiertas(), 0)

# Testeo cuando no hay apps abiertas
        self.assertEqual(self.mi_smartphone.cerrar_app(), "No hay aplicaciones abiertas")
        self.assertEqual(self.mi_smartphone.get_apps_abiertas(), 0)

    def test_instalar_app(self):
        test_cases = [
            {"almacenamiento_inicial": 0, "tamano_app": 30, "almacenamiento_esperado": 30},
            {"almacenamiento_inicial": 100, "tamano_app": 30, "almacenamiento_esperado": 100},
            {"almacenamiento_inicial": 120, "tamano_app": 10, "almacenamiento_esperado": 120},
        ]

        for case in test_cases:
            with self.subTest(case=case):
                self.mi_smartphone._Smartphone__almacenamiento_usado = case["almacenamiento_inicial"]
                self.mi_smartphone.instalar_app(case["tamano_app"])
                self.assertEqual(self.mi_smartphone.get_almacenamiento_usado(), case["almacenamiento_esperado"])

    def test_str_method(self):
        self.mi_smartphone._Smartphone__bateria = 90
        self.mi_smartphone._Smartphone__almacenamiento_usado = 20
        resultado = str(self.mi_smartphone)
        self.assertEqual(resultado, "Smartphone Voltron X con 90% de bateria y 108 GB de almacenamiento libre")

if __name__ == '__main__':
    unittest.main()