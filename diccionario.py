from io import open
import json

class TraduccionesClass:
    palabras = []

    def __init__(self):
        self.obtener_info()
        pass

    def obtener_info(self):
        archivo_traducciones = open("diccionario.txt", "r")

        self.palabras = archivo_traducciones.read()
        self.palabras = self.palabras.split("\n")
        listPalabras = []
        for palabra in self.palabras:      
          if palabra != " " and palabra != '' and palabra != "":
            listPalabras.append(json.loads(palabra))
          

        self.palabras = listPalabras

        archivo_traducciones.close()

        

    def agregarPalabra(self, espanol, ingles):
        archivo_traducciones = open("diccionario.txt", "a")
        palabra = {"espanol": espanol, "ingles": ingles}
        archivo_traducciones.write("\n"+json.dumps(palabra))
        self.palabras.append(palabra)
        archivo_traducciones.close()

    def obtenerPalabra(self,tipo, palabra):
        resultado= "No encontrada"
        if tipo == 1:
            for traduccion in self.palabras:
                if traduccion["ingles"].upper() == palabra.upper():
                    resultado = traduccion["espanol"]
                    break
        else:
            for traduccion in self.palabras:
                if traduccion["espanol"].upper() == palabra.upper():
                    resultado = traduccion["ingles"]
                    break
        return resultado
