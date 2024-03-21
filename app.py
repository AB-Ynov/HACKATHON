from flask import Flask, jsonify
import openstack

# Initialiser l'application Flask
app = Flask(__name__)

# Configuration OpenStack
openstack.enable_logging(debug=True)
conn = openstack.connect(cloud='openstack')  # Assurez-vous de configurer vos informations de connexion OpenStack

# Route pour obtenir les VMs actives
@app.route('/vms', methods=['GET'])
def get_active_vms():
    try:
        # Récupérer la liste des VMs
        vms = conn.list_servers()

        # Filtrer les VMs actives
        active_vms = [vm.name for vm in vms if vm.status == 'ACTIVE']

        # Renvoyer la liste des noms de VMs actives au format JSON
        return jsonify(active_vms), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Point d'entrée de l'application
if __name__ == '__main__':
    app.run(debug=True)