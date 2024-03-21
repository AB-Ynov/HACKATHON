from flask import Flask, jsonify
from openstack import connection

app = Flask(__name__)

# Configuration OpenStack
auth_url = 'https://<OPENSTACK_AUTH_URL>'
project_name = '<PROJECT_NAME>'
username = '<USERNAME>'
password = '<PASSWORD>'
user_domain_name = '<USER_DOMAIN_NAME>'
project_domain_name = '<PROJECT_DOMAIN_NAME>'

# Connexion à OpenStack
conn = connection.Connection(
    auth_url=auth_url,
    project_name=project_name,
    username=username,
    password=password,
    user_domain_name=user_domain_name,
    project_domain_name=project_domain_name
)

@app.route('/vms', methods=['GET'])
def get_vms():
    # Récupérer les machines virtuelles actives
    vms = conn.compute.servers()

    # Créer une liste de noms de machines virtuelles
    vm_names = [vm.name for vm in vms]

    # Retourner la liste de noms de machines virtuelles en tant que réponse JSON
    return jsonify(vm_names)

if __name__ == '__main__':
    app.run()