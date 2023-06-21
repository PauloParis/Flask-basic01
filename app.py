
from flask import Flask, request

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
    return f'Nombre: {nombre}'