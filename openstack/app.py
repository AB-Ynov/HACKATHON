from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint pour récupérer les informations des VMs
@app.route('/openstack/vms')
def get_openstack_vms():
    # Ici, vous devrez intégrer la logique pour récupérer les informations des VMs d'OpenStack
    # Par exemple, en utilisant la bibliothèque python-openstackclient ou en interagissant directement avec l'API OpenStack
    # Pour l'exemple, nous renvoyons des données statiques
    vms = [
        {"name": "VM1", "status": "Running"},
        {"name": "VM2", "status": "Stopped"}
    ]
    return jsonify(vms)

if __name__ == '__main__':
    app.run(debug=True)