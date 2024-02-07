class Colores:
    dict_colores = {
        'Negro': '#000000',
        'Cafe': '#A52A2A',
        'Rojo': '#FF0000',
        'Naranja': '#FFA500',
        'Amarillo': '#FFFF00',
        'Verde': '#008000',
        'Azul': '#0000FF',
        'Violeta': '#EE82EE',
        'Gris': '#808080'
    }

    dict_colores_valores = {
        'Negro': 0,
        'Cafe': 1,
        'Rojo': 2,
        'Naranja': 3,
        'Amarillo': 4,
        'Verde': 5,
        'Azul': 6,
        'Violeta': 7,
        'Gris': 8
    }

    dict_colores_multi = {
        'Negro': 1,
        'Cafe': 10,
        'Rojo': 100,
        'Naranja': 1000,
        'Amarillo': 10000,
        'Verde': 100000,
        'Azul': 1000000,
        'Violeta': 10000000,
        'Gris': 100000000
    }

    def __init__(self) -> None:
        pass

    def getColor(self, color):
        return self.dict_colores[color]

    def get_primer_banda(self, color):
        return self.dict_colores_valores[color]
    
    def get_segunda_banda(self, color):
        return self.dict_colores_valores[color]
    
    def get_tercer_banda(self, color):
        return self.dict_colores_multi[color]