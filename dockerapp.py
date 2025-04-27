from flask import Flask, request, jsonify
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/start', methods=['POST'])
def start_container():
    data = request.json
    image = data.get('image')
    name = data.get('name')
    port = data.get('port')  # format "8080:80"

    if not all([image, name, port]):
        return jsonify({"error": "Missing parameters"}), 400

    try:
        container = client.containers.run(
            image, name=name,
            ports={f"{port.split(':')[1]}/tcp": int(port.split(':')[0])},
            detach=True
        )
        return jsonify({"message": f"Container {name} started."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stop', methods=['POST'])
def stop_container():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({"error": "Missing container name"}), 400

    try:
        container = client.containers.get(name)
        container.stop()
        return jsonify({"message": f"Container {name} stopped."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/list', methods=['GET'])
def list_containers():
    containers = client.containers.list()
    container_info = [{"name": c.name, "status": c.status} for c in containers]
    return jsonify(container_info), 200

@app.route('/remove', methods=['POST'])
def remove_container():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({"error": "Missing container name"}), 400

    try:
        container = client.containers.get(name)
        container.remove(force=True)
        return jsonify({"message": f"Container {name} removed."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
