# TD4 : Créer sa propre image Docker

## Objectif du tutoriel

Ce tutoriel vise à enseigner la création, le test et la publication d'une image Docker à partir d'une application simple développée avec Python Flask.

---

## 1. Présentation de l'application

L'application est constituée d'un seul fichier `app.py` qui implémente une API REST simple pour gérer une liste de tâches :
- Une page d'accueil sur `/`
- Une route `/tasks` pour récupérer la liste des tâches
- Une route `/tasks/<id>` pour récupérer une tâche spécifique

### Code source de l'application

```python
from flask import Flask, jsonify
app = Flask(__name__)

# Données de démonstration
tasks = [
    {"id": 1, "title": "Apprendre Docker", "completed": False},
    {"id": 2, "title": "Créer un Dockerfile", "completed": True},
    {"id": 3, "title": "Publier sur Docker Hub", "completed": False}
]

@app.route('/')
def home():
    return jsonify({
        "message": "Bienvenue sur l'API de gestion de tâches",
        })

@app.route('/tasks')
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks/<int:task_id>')
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Tâche non trouvée"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

L'application écoute sur le port 5000 et retourne des données au format JSON. Elle est accessible via `http://<IP_du_serveur>:5000`.

---

## 2. Déploiement manuel (avant Docker)

Avant de conteneuriser l'application, voici les étapes nécessaires pour un déploiement manuel :

### Installation de Python

```bash
apt-get update
apt-get install -y python3 python3-pip
```

### Installation de Flask

```bash
pip install flask
ou
sudo apt install python3-flask
```

### Déploiement du code

Copier le fichier `app.py` dans `/opt/app/`

### Lancement du serveur

```bash
python3 /opt/app/app.py
```

Ces étapes illustrent les actions nécessaires qui seront automatisées dans un Dockerfile.

---

## 3. Création du Dockerfile

### Préparation de l'environnement de travail

```bash
mkdir mon-app-flask
cd mon-app-flask
```

### Contenu du Dockerfile

```dockerfile
# Étape 1 : Choisir une image de base
FROM ubuntu:20.04

# Étape 2 : Mettre à jour et installer Python + pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Étape 3 : Installer Flask
RUN pip install flask

# Étape 4 : Copier le code source dans l'image
COPY app.py /opt/app/app.py

# Étape 5 : Définir le point d'entrée
ENTRYPOINT ["python3", "/opt/app/app.py"]
```

---

## 4. Construction de l'image

Dans le dossier contenant le Dockerfile et `app.py`, exécuter la commande suivante :

```bash
docker build -t flask-webapp .
```

### Paramètres de la commande

- `-t flask-webapp` : attribue un nom à l'image
- `.` : indique le répertoire courant (où se trouve le Dockerfile)

### Sortie attendue

```
Step 1/5 : FROM ubuntu:20.04
Step 2/5 : RUN apt-get update && apt-get install -y python3 python3-pip
Step 3/5 : RUN pip install flask
Step 4/5 : COPY app.py /opt/app/app.py
Step 5/5 : ENTRYPOINT ["python3", "/opt/app/app.py"]
Successfully built <id_image>
Successfully tagged flask-webapp:latest
```

---

## 5. Exécution de l'image

Une fois l'image construite, l'application peut être lancée avec :

```bash
docker run -dti -p 5000:5000 flask-webapp
```

Le paramètre `-p 5000:5000` lie le port 5000 du conteneur au port 5000 de la machine hôte.

### Test de l'application

Ouvrir un navigateur ou utiliser `curl` pour accéder aux endpoints :

**Page d'accueil :**
```bash
curl http://localhost:5000
```
Retourne :
```json
{
  "message": "Bienvenue sur l'API de gestion de tâches",
}
```

**Liste des tâches :**
```bash
curl http://localhost:5000/tasks
```
Retourne :
```json
{
  "tasks": [
    {"id": 1, "title": "Apprendre Docker", "completed": false},
    {"id": 2, "title": "Créer un Dockerfile", "completed": true},
    {"id": 3, "title": "Publier sur Docker Hub", "completed": false}
  ]
}
```

**Tâche spécifique :**
```bash
curl http://localhost:5000/tasks/1
```
Retourne :
```json
{
  "id": 1,
  "title": "Apprendre Docker",
  "completed": false
}
```

---

## 6. Notion de cache dans le build

Lors de la reconstruction d'une image, Docker réutilise les couches déjà créées si aucune modification n'a été apportée aux instructions correspondantes.

Ainsi, si seul le fichier `app.py` est modifié, Docker ne réexécutera pas les étapes d'installation des dépendances, ce qui accélère considérablement le processus de build.

---

## 7. Publication de l'image sur Docker Hub

### Connexion à Docker Hub

```bash
docker login
```

Saisir les identifiants Docker Hub lorsque demandé.

### Tagage de l'image

```bash
docker tag flask-webapp saberdk/flask-webapp:1.0
```

### Publication de l'image

```bash
docker push saberdk/flask-webapp:1.0
```

Une fois le processus terminé, l'image sera visible dans l'espace Docker Hub : `https://hub.docker.com/u/dk-saber`

---

## 8. Utilisation de l'image depuis n'importe où

N'importe quel utilisateur peut désormais exécuter l'application en une seule commande :

```bash
docker run -p 5000:5000 saberdk/flask-webapp:1.0
```

---

## 9. Schéma récapitulatif du workflow

```
[ app.py ]
    ↓
[ Dockerfile ]
    ↓  docker build
[ Image Docker ]
    ↓  docker push
[ Docker Hub ]
    ↓  docker pull
[ Container en exécution ]
```

---

## Conclusion du tutoriel

Ce tutoriel a permis de couvrir les étapes suivantes :
1. Création d'un Dockerfile
2. Construction d'une image Docker
3. Exécution d'un conteneur
4. Publication de l'image sur Docker Hub

### Avantages de Docker

- **Portabilité** : déploiement de l'application sur n'importe quelle machine sans configuration manuelle
- **Encapsulation** : les dépendances sont intégrées dans l'image
- **Reproductibilité** : environnement cohérent et prévisible

---

## Ressources complémentaires

- [Documentation officielle Docker](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

**Auteur :** [dk-saber](https://www.github.com/dk-saber)
