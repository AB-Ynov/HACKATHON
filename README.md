
# OpenStack Active VMs API
Ce projet contient une API simple pour récupérer les machines virtuelles actives sur un réseau OpenStack.
## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

- Accès à un tableau de bord OpenStack avec les informations de connexion nécessaires.
- Python installé sur votre système.
- Les bibliothèques Python Flask et python-openstackclient.

Vous pouvez installer les dépendances nécessaires en exécutant la commande suivante :

```bash
pip install Flask python-openstackclient
```

## Configuration

Assurez-vous de configurer vos informations de connexion OpenStack dans un fichier `clouds.yaml` ou directement dans le code Python.

## Exécution de l'API

Pour exécuter l'API, exécutez le script Python `app.py` :

```bash
python app.py
```

L'API sera alors accessible à l'adresse `http://localhost:5000/vms`.

## Utilisation

Lorsque vous accédez à l'URL de l'API, vous obtiendrez une liste des noms des machines virtuelles actives au format JSON.
