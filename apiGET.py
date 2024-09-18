# Importamos Flask
from flask import Flask, request, jsonify

# Creamos la instancia de la aplicación Flask
app = Flask(__name__)

# Definimos una ruta y el método GET
@app.route('/saludo', methods=['GET'])
def saludo():
    # Obtenemos el parámetro 'nombre' de la URL (si es que está)
    nombre = request.args.get('nombre', 'Mundo')  # Por defecto será 'Mundo' si no se pasa el parámetro

    # Retornamos el saludo en formato JSON
    return jsonify({'mensaje': f'¡Hola, {nombre}!'})

# Ejecutamos la aplicación en modo de desarrollo
if __name__ == '__main__':
    app.run(debug=True)