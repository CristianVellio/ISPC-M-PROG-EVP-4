class Smartphone:
    def __init__(self, marca, bateria=100, almacenamiento=128):
        self.__marca = marca
        self.__bateria = bateria  # valor de medida de 0 a 100 en porcentaje
        self.__almacenamiento = almacenamiento  # valor de medida en GB
        self.__almacenamiento_usado = 0
        self.__apps_abiertas = 0

    def __puede_abrir_app(self, consumo_bateria):
        return self.__bateria >= consumo_bateria

    def __hay_apps_abiertas(self):
        return self.__apps_abiertas > 0

    def abrir_app(self, consumo_bateria):
        """Intenta abrir una app y consumir batería."""
        if self.__puede_abrir_app(consumo_bateria):
            self.__consumir_bateria(consumo_bateria)
            self.__apps_abiertas += 1
            return f"Aplicacion abierta, bateria restante: {self.__bateria}%"
        return "Bateria insuficiente para abrir la aplicacion"

    def cerrar_app(self):
        """Cierra todas las aplicaciones abiertas."""
        if self.__hay_apps_abiertas():
            self.__apps_abiertas = 0
            return "Todas las aplicaciones han sido cerradas"
        return "No hay aplicaciones abiertas"

    def instalar_app(self, tamano_app):
        """Instala una app si hay suficiente almacenamiento."""
        if self.__almacenamiento_libre() >= tamano_app:
            self.__almacenamiento_usado += tamano_app
            return f"Aplicacion instalada, almacenamiento usado: {self.__almacenamiento_usado} GB"
        return "Almacenamiento insuficiente para instalar la aplicacion"

    def __consumir_bateria(self, cantidad):
        self.__bateria = max(self.__bateria - cantidad, 0)

    def __almacenamiento_libre(self):
        return self.__almacenamiento - self.__almacenamiento_usado

    def __str__(self):
        return (
            f"Smartphone {self.__marca} con {self.__bateria}% de bateria "
            f"y {self.__almacenamiento_libre()} GB de almacenamiento libre"
        )

    def get_bateria(self):
        return self.__bateria

    def get_apps_abiertas(self):
        return self.__apps_abiertas

    def get_almacenamiento_usado(self):
        return self.__almacenamiento_usado


# Mi Smartphone1
mi_smartphone = Smartphone("Voltron X")
print(mi_smartphone.abrir_app(10))
print(mi_smartphone.instalar_app(20))
print(mi_smartphone.cerrar_app())
print(mi_smartphone)