from flask import Flask, jsonify

app = Flask(__name__)

# Exemple de données de machines virtuelles OpenStack
openstack_vms = [
    {"name": "VM1", "status": "Running", "ip": "192.168.1.101"},
    {"name": "VM2", "status": "Stopped", "ip": "192.168.1.102"},
    {"name": "VM3", "status": "Running", "ip": "192.168.1.103"}
]

@app.route('/openstack', methods=['GET'])
def get_openstack_vms():
    return jsonify(openstack_vms)

if __name__ == '__main__':
    app.run(debug=True)