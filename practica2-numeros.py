class numerosFunciones:
    numeros = []
    pares = []
    impares = []
    repetidos = []
    def __init__(self):
        self.solicitarNumeros()

    def solicitarNumeros(self):
        cantNumeros = int(input("Cuantos Numeros desea Ingresar"))
        for i in range(cantNumeros):
            numero = int(input("Ingresa Un Numero: "))
            self.numeros.append(numero)

    def ordenar(self):
        self.numeros.sort()
        print(f"Los Numeros Ordenados son: {self.numeros}")

    def paresImpares(self):
        self.numeros.sort()
        numeroAnterior = None
        for numero in self.numeros:
            if numeroAnterior == None:
              if numero%2 == 0:
                  self.pares.append(numero)
              else:
                    self.impares.append(numero)
            else:
                if numero%2 == 0 and numeroAnterior != numero:
                  self.pares.append(numero)
                elif numeroAnterior != numero:
                    self.impares.append(numero)
            numeroAnterior = numero

        print(f"Los pares son: {self.pares} Los impares son: {self.impares} ")

    def numerosRepetidos(self):
         self.numeros.sort()
         numeroAnterior = None
         cant = 0
         for numero in self.numeros:
            if numeroAnterior == None:
                numeroAnterior = numero
            else:
                if numeroAnterior == numero:   
                    if numero not in self.repetidos:             
                        self.repetidos.append(numero)
                    cant += 1
                else:
                    if numeroAnterior in self.repetidos:
                        print("El numero {} se repitio {} veces ".format(numeroAnterior,cant+1))
                    cant = 0
                numeroAnterior = numero
         if numeroAnterior in self.repetidos:
                        print("El numero {} se repitio {} veces ".format(numeroAnterior,cant+1))
         print("Los numeros repetidos son: ", self.repetidos)
            
def main():
    obj = numerosFunciones()
    obj.ordenar()
    obj.numerosRepetidos()
    obj.paresImpares()
    


if __name__ == "__main__":
    main()