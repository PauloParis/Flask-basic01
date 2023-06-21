
from flask import Flask, request, render_template, url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

app = Flask(__name__)


""" 
--logger--

@app.route('/')
def inicio():
    app.logger.debug('Nivel debug')
    app.logger.info('Nivel info')
    app.logger.warn('Nivel warning') # en producción muestra desde aqui
    app.logger.error('Nivel error')
    return 'Hola mundo desde Flask' """

@app.route('/')
def inicio():
    app.logger.info(f'Entramos al path {request.path}')
    return 'Hola mundo desde Flask'


""" 
--Tipos que puede recibir como parametros--

string  ->  (default) accepts any text without a slash
int     ->  accepts positive integers
float   ->  accepts positive floating point values
path    ->  like string but also accepts slashes
uuid    ->  accepts UUID strings

 """
@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre.upper()}'

@app.route('/edad/<int:edad>')
def edad(edad):
    return f'edad: {edad + 1}'

@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar(nombre):
    return render_template('mostrar.html', nombre=nombre)


@app.route('/redireccionar')
def redireccionar():
    #return redirect(url_for('inicio'))
    return redirect(url_for('mostrar', nombre='juan'))




# MANEJO DE ERRORES

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return (render_template('error404.html', error=error), 404)
