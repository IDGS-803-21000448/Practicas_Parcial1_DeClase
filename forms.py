from wtforms import Form
from wtforms import StringField, SelectField, EmailField, IntegerField, FloatField, ColorField, RadioField
from wtforms import validators


class DistanciaForm(Form):
    x1=FloatField('x1')
    x2=FloatField('x2')
    y1=FloatField('y1')
    y2=FloatField('y2')
   
class ResistenciaForm(Form):
    color1=SelectField('Color 1', choices=[('Negro', 'Negro'), ('Cafe', 'Cafe'), ('Rojo', 'Rojo'), ('Naranja', 'Naranja'), ('Amarillo', 'Amarillo') , ('Verde', 'Verde') , ('Azul', 'Azul') , ('Violeta', 'Violeta') , ('Gris', 'Gris'), ('Blanco', 'Blanco')])
    color2=SelectField('Color 2', choices=[('Negro', 'Negro'), ('Cafe', 'Cafe'), ('Rojo', 'Rojo'), ('Naranja', 'Naranja'), ('Amarillo', 'Amarillo') , ('Verde', 'Verde') , ('Azul', 'Azul') , ('Violeta', 'Violeta') , ('Gris', 'Gris'), ('Blanco', 'Blanco')])
    color3=SelectField('Color 3', choices=[('Negro', 'Negro'), ('Cafe', 'Cafe'), ('Rojo', 'Rojo'), ('Naranja', 'Naranja'), ('Amarillo', 'Amarillo') , ('Verde', 'Verde') , ('Azul', 'Azul') , ('Violeta', 'Violeta') , ('Gris', 'Gris'), ('Blanco', 'Blanco')])
    tolerancia=RadioField('Color de la Tolerancia', choices=[('5', 'Dorado'), ('10', 'Plata')])


class TraduccionesForm(Form):
    espanol = StringField('Palabra en Español', [
        validators.DataRequired(message="Este campo es obligatorio."),
        validators.Length(min=1, max=50, message="La palabra debe tener entre 1 y 50 caracteres.")
    ])
    ingles = StringField('Palabra en Inglés', [
        validators.DataRequired(message="Este campo es obligatorio."),
        validators.Length(min=1, max=50, message="La palabra debe tener entre 1 y 50 caracteres.")
    ])

class TraducirForm(Form):
    palabra = StringField('Palabra a Traducir', [
        validators.DataRequired(message="Este campo es obligatorio."),
        validators.Length(min=1, max=50, message="La palabra debe tener entre 1 y 50 caracteres.")
    ])
    idioma = RadioField('Idioma de Destino', choices=[('1', 'Inglés'), ('2', 'Español')], validators=[
        validators.DataRequired(message="Debe seleccionar un idioma.")
    ])