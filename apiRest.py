from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para manejar el método GET
@app.route('/saludo', methods=['GET'])
def saludo():
    nombre = request.args.get('nombre', '')
    ip = request.remote_addr  # Obtenemos la IP del cliente
    return jsonify({
        'mensaje': f'¡Hola, {nombre}!',
        'ip': ip
    })

# Ruta para manejar el método POST
@app.route('/saludo', methods=['POST'])
def saludo_post():
    data = request.json  # Esperamos un JSON con el nombre
    nombre = data.get('nombre', '')
    ip = request.remote_addr
    return jsonify({
        'mensaje': f'¡Hola desde POST, {nombre}!',
        'ip': ip
    })

# Ruta para manejar el método PUT
@app.route('/saludo', methods=['PUT'])
def saludo_put():
    data = request.json  # Esperamos un JSON con el nombre
    nombre = data.get('nombre', '')
    ip = request.remote_addr
    return jsonify({
        'mensaje': f'¡Hola desde PUT, {nombre}!',
        'ip': ip
    })

# Ruta para manejar el método DELETE
@app.route('/saludo', methods=['DELETE'])
def saludo_delete():
    ip = request.remote_addr
    return jsonify({
        'mensaje': '¡Saludo eliminado con DELETE!',
        'ip': ip
    })

if __name__ == '__main__':
    app.run(debug=True)
