import unittest
from evidencia4 import Smartphone

class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.mi_smartphone = Smartphone("Voltron X")


#uso bateria

    def test_abrir_app_con_bateria_sufuciente(self):
        self.mi_smartphone.abrir_app(10)
        self.assertEqual(self.mi_smartphone.get_bateria(), 90)
        self.assertEqual(self.mi_smartphone.get_apps_abiertas(), 1)
    
    def test_abrir_app_con_bateria_insuficiente(self):
        self.mi_smartphone._Smartphone__bateria = 10
        self.mi_smartphone.abrir_app(20)
        self.assertEqual(self.mi_smartphone.get_bateria(), 10)
        self.assertEqual(self.mi_smartphone.get_apps_abiertas(), 0)

 #apps en uso       

    def test_cerrar_app_con_apps_abiertas(self):
        self.mi_smartphone.abrir_app(15)
        self.mi_smartphone.cerrar_app()
        self.assertEqual(self.mi_smartphone.get_apps_abiertas(), 0)

    def test_cerrar_app_sin_apps_abiertas(self):
        self.mi_smartphone.cerrar_app()
        self.assertEqual(self.mi_smartphone.get_apps_abiertas(), 0)

#almacenamiento

    def test_instalar_app_con_espacio_disponible(self):
        self.mi_smartphone.instalar_app(30)
        self.assertEqual(self.mi_smartphone.get_almacenamiento_usado(), 30)

    def test_instalar_app_sin_espacio_disponible(self):
        self.mi_smartphone._Smartphone__almacenamiento_usado = 100
        self.mi_smartphone.instalar_app(30)
        self.assertEqual(self.mi_smartphone.get_almacenamiento_usado(), 100)

#testing

    def test_str_method(self):
        resultado = str(self.mi_smartphone)
        self.assertEqual(resultado, "Smartphone Voltron X con 100% de bateria y 128 GB de almacenamiento libre")

if __name__ == '__main__':
    unittest.main()