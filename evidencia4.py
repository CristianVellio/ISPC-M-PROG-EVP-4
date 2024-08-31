class smartphone:
    def __init__(self, marca, bateria=100, almacenamiento=128):
        self.marca = marca
        self.bateria = bateria #valor de medida de 0 a 100 en porcentaje
        self.almacenamiento = almacenamiento #valor de medida en GB
        self.almacenamiento_usado = 0
        self.apps_en_uso = 0
        
