
from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

app.secret_key = 'jBsadfS_U2/34Iv675nb.-HSDh54-jGSObO34gh56'


@app.route('/')
def inicio():
    if 'username' in session:
        return f"El usuario ya ha hecho login {session['username']}"
    return 'No ha hecho login'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # sin validaciones
        usuario = request.form['username']
        session['username'] = usuario
        
        # las 2 lineas de arriba se pueden resumir en la linea de abajo
        # session['username'] = request.form['username']

        return redirect(url_for('inicio'))

    return render_template('login.html')



@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))





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



# USO DE JSON

# rest representational state transfer
# consumo desde el front (vue, react, angular, etc)
@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_json(nombre):
    valores = {
        'nombre': nombre,
        'metodo_http': request.method
    }
    return valores
    #return jsonify(valores) # por ahora no es necesario



# MANEJO DE SESIÓN 

#app.secret_key = 'jBsadfS_U2/34Iv675nb.-HSDh54-jGSObO34gh56'