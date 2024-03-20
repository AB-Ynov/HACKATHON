from flask import Flask, jsonify
import nmap

app = Flask(__name__)

def get_active_vms():
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.1.0/24', arguments='-sn')  # Modifier l'adresse IP ou la plage selon votre réseau
    active_vms = []
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            active_vms.append({
                'ip': host,
                'mac_address': nm[host]['addresses']['mac'],
                'vendor': nm[host]['vendor'][nm[host]['addresses']['mac']]
            })
    return active_vms

@app.route('/api/active_vms', methods=['GET'])
def active_vms():
    return jsonify(get_active_vms())

if __name__ == '__main__':
    app.run(debug=True)
