class practica1:
    numero = 0

    def __init__(self, n):
        self.numero = n

    def piramide(self):
        i = 1
        while i <= self.numero:
            ob = "*"
            j = 1
            while j < i:
                ob += "*"
                j += 1
            print(ob)
            i += 1

def main():
    numero = int(input("Dame un numero para crear la Priamide: "))
    obj = practica1(numero)
    obj.piramide()


if __name__ == "__main__":
    main()