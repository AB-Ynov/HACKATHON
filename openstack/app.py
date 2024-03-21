from flask import Flask, jsonify, render_template, request
import openstack
import time

app = Flask(__name__)

# Configuration OpenStack
openstack.enable_logging(debug=True)
conn = openstack.connect(cloud='devstack')

# Fonction pour créer une machine virtuelle
def create_vm(name):
    flavor = conn.compute.find_flavor(name_or_id='m1.tiny')
    image = conn.compute.find_image(name_or_id='cirros')
    network = conn.network.find_network(name_or_id='private')
    server = conn.compute.create_server(name=name, flavor_id=flavor.id, image_id=image.id, network_id=network.id)
    return server.id

# Fonction pour récupérer les machines virtuelles et leur état
def get_openstack_vms():
    vms = conn.compute.servers()
    openstack_vms = []
    for vm in vms:
        vm_info = {
            'name': vm.name,
            'status': vm.status,
            'created_at': vm.created_at
        }
        openstack_vms.append(vm_info)
    return openstack_vms

# Route pour récupérer les VMs depuis OpenStack
@app.route('/openstack/vms', methods=['GET'])
def openstack_vms():
    return jsonify(get_openstack_vms())

# Route pour créer une nouvelle VM
@app.route('/openstack/vms', methods=['POST'])
def create_openstack_vm():
    data = request.json
    vm_name = data['name']
    vm_id = create_vm(vm_name)
    time.sleep(5)  # Attendre quelques secondes pour que la VM soit opérationnelle
    vm_info = {
        'id': vm_id,
        'name': vm_name,
        'status': 'Building',
        'created_at': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    }
    return jsonify(vm_info), 201

if __name__ == '__main__':
    app.run(debug=True)