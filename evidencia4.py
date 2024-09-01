class Smartphone:
    def __init__(self, marca, bateria=100, almacenamiento=128):
        self.marca = marca
        self.bateria = bateria  # valor de medida de 0 a 100 en porcentaje
        self.almacenamiento = almacenamiento  # valor de medida en GB
        self.almacenamiento_usado = 0
        self.apps_abiertas = 0

    def abrir_app(self, consumo_bateria):
        if self.bateria >= consumo_bateria:
            self.bateria -= consumo_bateria
            self.apps_abiertas += 1
            print(f"Aplicacion abierta, bateria restante: {self.bateria}%")
        else:
            print("Bateria insuficiente para abrir la aplicacion")

    def cerrar_app(self):
        if self.apps_abiertas > 0:
            self.apps_abiertas = 0
            print("Todas las aplicaciones han sido cerradas")
        else:
            print("No hay aplicaciones abiertas")

    def instalar_app(self, tamano_app):
        if self.almacenamiento_usado + tamano_app <= self.almacenamiento:
            self.almacenamiento_usado += tamano_app
            print(f"Aplicacion instalada, almacenamiento usado: {self.almacenamiento_usado} GB")
        else:
            print("Almacenamiento insuficiente para instalar la aplicacion")


def __str__(self):
    return f"Smartphone {self.marca} con {self.bateria}% de bateria y {self.almacenamiento - self.almacenamiento_usado} GB de almacenamiento libre"




#My Smartphone1
mi_smartphone = Smartphone("Voltron X")
mi_smartphone.abrir_app(10)
mi_smartphone.instalar_app(20)
mi_smartphone.cerrar_app()
print(mi_smartphone)