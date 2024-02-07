from math import sqrt, pow
import forms
from flask import Flask, render_template, request, template_rendered

from Colores import Colores



app = Flask(__name__)

@app.route("/")
def index():
    #return "<h1>Hola <br> Mundo</h1>"
    escuela = "UTL!!!"
    alumnos = ["Mario", "Pedro", "Luis", "Dario"]
    return render_template("index.html",escuela = escuela, alumnos = alumnos)

@app.route("/hola")
def hola():
    return "<p> <h1> Hola desde HOLA!!!!! <h1> </p>"

@app.route("/user/<string:name>")
def user(name):
    return "<h1> Hola "+name+"</h1>"

@app.route("/numero/<int:n>")
def numero(n):
    return "El numero es: {}".format(n)

@app.route("/user/<int:id>/<string:name>")
def func(id, name):
    return f"ID: {id} Nombre: {name}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"La suma es {n1} + {n2} = {n1+n2}"

@app.route("/default")
@app.route("/default/<string:ab>")
def func1(ab = "UTL"):
    return "El Valor es "+ab

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")


@app.route("/multiplicar", methods=["GET", "POST"])
def multiplicar():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")

        return f"<h1> La multiplicacion es: {str(int(num1) * int(num2))} </h1>"
    else:
        return '''
                <form action="/multiplicar" method="POST">
                    <label>N1: </label>
                    <input type= "text" name="n1"/> </br>
                    <label>N2: </label>
                    <input type= "text" name="n2"/> </br>
                    <input type="submit"/>
                </form>
             '''

@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")



@app.route("/resultado",  methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        operacion = request.form.get("operacion")
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        if operacion == "Multiplicacion":
            return f"<h1> La Multiplicacion es: {str(int(num1) * int(num2))} </h1>"
        elif operacion == "Suma":
            return f"<h1> La Suma es: {str(int(num1) + int(num2))} </h1>"
        elif operacion == "Resta":
            return f"<h1> La Resta es: {str(int(num1) - int(num2))} </h1>"
        elif operacion == "Division":
            return f"<h1> La Division es: {str(int(num1) / int(num2))} </h1>"


@app.route("/cinepolis")
def cinepolis():
    return render_template("cinepolis.html")

@app.route("/procesar",  methods=["POST"])
def procesar():
    nombre = request.form.get('nombre')
    cantCompradores = int(request.form.get('cantidadCompradores'))
    tarjetaCineco = request.form.get('tarjetaCineco')
    cantBoletos = int(request.form.get('cantidadBoletos')) 
    precioBoleto = 12.00
    maxBoletos = 7

    porcentajeDescuento = 0
    valorPagar = 0

    if cantBoletos > cantCompradores * maxBoletos:
        return template_rendered("cinepolis.html")

    if cantBoletos > 0:
        valorPagar = cantBoletos * precioBoleto
        if cantBoletos > 5:
            valorPagar *= 0.85
        elif cantBoletos > 2 and cantBoletos <= 5:
            valorPagar *= 0.90
        if tarjetaCineco == 'Si':
            valorPagar *= 0.90 
        
    return template_rendered("cinepolis.html", valorPagar = str(valorPagar), 
                           nombre = str(nombre),cantidadCompradores = str(cantCompradores)
                            ,tarjetaCineco = tarjetaCineco, cantidadBoletos= cantBoletos  )


@app.route("/distancia",  methods=["GET","POST"])
def distancia():
    distancia_form = forms.DistanciaForm(request.form)
    res = ""
    if request.method == "POST":
        x1 = distancia_form.x1.data
        x2 = distancia_form.x2.data
        y1 = distancia_form.y1.data
        y2 = distancia_form.y2.data
        res = sqrt((pow((x2-x1),2)) + (pow((y2-y1),2)))
        


    return render_template("distancia.html",
                            form = distancia_form,
                            res = res)

@app.route("/resistencias",  methods=["GET","POST"])
def resistencia():
    resistencia_form = forms.ResistenciaForm(request.form)
    res = ""
    colores = Colores()

    if request.method == "POST":
        color1 = resistencia_form.color1.data
        hexColor1 = colores.getColor(color1)
        color2 = resistencia_form.color2.data
        hexColor2 = colores.getColor(color2)
        color3 = resistencia_form.color3.data
        hexColor3 = colores.getColor(color3)
        tolerancia = resistencia_form.tolerancia.data

        primer_banda = colores.get_primer_banda(color1)
        segunda_banda = colores.get_segunda_banda(color2)
        multiplicador = colores.get_tercer_banda(color3)


        valor = int(str(primer_banda) + str(segunda_banda) ) * multiplicador

        maximo = valor + (valor * (int(tolerancia)/100))

        minimo = valor - (valor * (int(tolerancia)/100))




    return render_template("resistencia.html",
                            form = resistencia_form,
                            hexColor1 = hexColor1, hexColor2 = hexColor2, hexColor3 = hexColor3, valor = valor, maximo = maximo, minimo = minimo)


if __name__ == "__main__":
    app.run(debug=True)
