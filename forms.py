from wtforms import Form
from wtforms import StringField, SelectField, EmailField, IntegerField, FloatField, ColorField, RadioField


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