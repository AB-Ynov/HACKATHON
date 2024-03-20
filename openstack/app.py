from flask import Flask, render_template, request

app = Flask(__name__)

resource_requests = []

@app.route('/')
def home():
    return render_template('index.html', requests=resource_requests)

@app.route('/submit_request', methods=['POST'])
def submit_request():
    # Récupérer les données de la demande depuis le formulaire
    resource_type = request.form['resource_type']
    quantity = int(request.form['quantity'])
    duration = int(request.form['duration'])

    # Ajouter la demande à la liste des demandes
    resource_requests.append({
        'resource_type': resource_type,
        'quantity': quantity,
        'duration': duration,
    })

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
