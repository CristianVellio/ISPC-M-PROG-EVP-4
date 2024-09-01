class Smartphone:
    def __init__(self, marca, bateria=100, almacenamiento=128):
        self.__marca = marca
        self.__bateria = bateria  # valor de medida de 0 a 100 en porcentaje
        self.__almacenamiento = almacenamiento  # valor de medida en GB
        self.__almacenamiento_usado = 0
        self.__apps_abiertas = 0

    def abrir_app(self, consumo_bateria):
        if self.__bateria >= consumo_bateria:
            self.__bateria -= consumo_bateria
            self.__apps_abiertas += 1
            print(f"Aplicacion abierta, bateria restante: {self.__bateria}%")
        else:
            print("Bateria insuficiente para abrir la aplicacion")

    def cerrar_app(self):
        if self.__apps_abiertas > 0:
            self.__apps_abiertas = 0
            print("Todas las aplicaciones han sido cerradas")
        else:
            print("No hay aplicaciones abiertas")

    def instalar_app(self, tamano_app):
        if self.__almacenamiento_usado + tamano_app <= self.__almacenamiento:
            self.__almacenamiento_usado += tamano_app
            print(f"Aplicacion instalada, almacenamiento usado: {self.__almacenamiento_usado} GB")
        else:
            print("Almacenamiento insuficiente para instalar la aplicacion")


    def __str__(self):
        return (f"Smartphone {self.__marca} con {self.__bateria}% de bateria y "
                f"{self.__almacenamiento - self.__almacenamiento_usado} GB de almacenamiento libre")



#My Smartphone1*
mi_smartphone = Smartphone("Voltron X")
mi_smartphone.abrir_app(10)
mi_smartphone.instalar_app(20)
mi_smartphone.cerrar_app()

print(mi_smartphone)