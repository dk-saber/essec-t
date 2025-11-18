# TD6 : Variables d'Environnement Docker - Application Flask

Une application Flask simple qui démontre l'utilisation des variables d'environnement Docker pour configurer dynamiquement la couleur de fond d'une page web.

##  Prérequis

- Git installé
- Docker installé sur votre machine
- Un compte GitHub
- Un compte Docker Hub
- Un navigateur web

##  Installation

### 1. Cloner le repository

```bash
git clone https://github.com/dk-saber/essec-t.git
cd essec-t/docker/3.1-td6-color-app
```

### 2. Créer le Dockerfile

Créez un fichier `Dockerfile` à la racine du projet avec votre éditeur préféré :

**Avec vim :**
```bash
vim Dockerfile
```

**Ou avec nano :**
```bash
nano Dockerfile
```

Contenu du `Dockerfile` :

```dockerfile
# Utilisation de l'image Python 3.9 slim comme base
FROM python:3.9-slim

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie du fichier app.py dans le conteneur
COPY app.py .

# Copie du fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installation des dépendances Python sans cache pour réduire la taille de l'image
RUN pip install --no-cache-dir -r requirements.txt

# Exposition du port 5000 pour l'application Flask
EXPOSE 5000

# Commande par défaut pour démarrer l'application
CMD ["python", "app.py"]
```

**Enregistrez et quittez :**
- **vim** : Appuyez sur `ESC`, tapez `:wq` puis `Enter`
- **nano** : Appuyez sur `CTRL+X`, puis `Y`, puis `Enter`

### 3. Push du Dockerfile vers GitHub

```bash
git add Dockerfile
git commit -m "Add Dockerfile"
git push origin main
```

##  Gestion de l'image Docker

### 4. Build de l'image Docker

```bash
docker build -t color-app .
```

Vérifiez que l'image a été créée :

```bash
docker images
```

Pour taguer l'image pour Docker Hub (remplacez `votre-username` par votre nom d'utilisateur Docker Hub) :

```bash
docker tag color-app votre-username/color-app:latest
```

Vérifiez les images avec le nouveau tag :

```bash
docker images
```

Vous devriez voir deux entrées : `color-app` et `votre-username/color-app:latest`

### 5. Connexion à Docker Hub

```bash
docker login
```

Entrez votre nom d'utilisateur et mot de passe Docker Hub.

### 6. Push de l'image vers Docker Hub

```bash
docker push votre-username/color-app:latest
```

Pour faire un push avec plusieurs tags :

```bash
docker push votre-username/color-app:latest
docker tag votre-username/color-app:latest votre-username/color-app:v1.0
docker push votre-username/color-app:v1.0
```

### 7. Pull de l'image depuis Docker Hub

```bash
docker pull votre-username/color-app:latest
```

### 8. Run de l'image

**Exécution basique (couleur par défaut - rouge) :**
```bash
docker run -it -p 5000:5000 votre-username/color-app:latest
```

Accédez à l'application : http://localhost:5000

**Avec une couleur personnalisée :**
```bash
docker run -it -p 5000:5000 -e APP_COLOR=blue votre-username/color-app:latest
```

**En mode détaché (arrière-plan) :**
```bash
docker run -d -it -p 5000:5000 -e APP_COLOR=green --name my-color-app votre-username/color-app:latest
```

##  Utilisation avancée

### Exécution avec différentes couleurs

```bash
# Couleur bleue
docker run -it -p 5000:5000 -e APP_COLOR=blue votre-username/color-app:latest

# Couleur verte
docker run -it -p 5000:5000 -e APP_COLOR=green votre-username/color-app:latest

# Couleur jaune
docker run -it -p 5000:5000 -e APP_COLOR=yellow votre-username/color-app:latest

# Couleur personnalisée (code hexadécimal)
docker run -it -p 5000:5000 -e APP_COLOR=#FF5733 votre-username/color-app:latest
```

##  Déploiement multi-conteneurs

Pour déployer plusieurs instances avec des couleurs différentes :

```bash
# Conteneur 1 - Rouge sur le port 5001
docker run -d -it -p 5001:5000 -e APP_COLOR=red --name app-red votre-username/color-app:latest

# Conteneur 2 - Bleu sur le port 5002
docker run -d -it -p 5002:5000 -e APP_COLOR=blue --name app-blue votre-username/color-app:latest

# Conteneur 3 - Vert sur le port 5003
docker run -d -it -p 5003:5000 -e APP_COLOR=green --name app-green votre-username/color-app:latest
```

**Accès aux conteneurs :**
- Rouge : http://localhost:5001
- Bleu : http://localhost:5002
- Vert : http://localhost:5003

##  Commandes de gestion

### Inspection des conteneurs

**Voir les conteneurs en cours d'exécution :**
```bash
docker ps
```

**Voir tous les conteneurs :**
```bash
docker ps -a
```

**Inspecter les variables d'environnement :**
```bash
docker inspect app-blue
```

**Filtrer uniquement les variables d'environnement :**
```bash
docker inspect app-blue | grep -A 10 "Env"
```

**Voir les logs :**
```bash
docker logs app-blue
```

**Logs en temps réel :**
```bash
docker logs -f app-blue
```

### Arrêt et suppression

**Arrêter un conteneur :**
```bash
docker stop app-blue
```

**Arrêter plusieurs conteneurs :**
```bash
docker stop app-red app-blue app-green
```

**Supprimer un conteneur :**
```bash
docker rm app-blue
```

**Supprimer plusieurs conteneurs :**
```bash
docker rm app-red app-blue app-green
```

**Supprimer une image locale :**
```bash
docker rmi votre-username/color-app:latest
```

**Arrêter et supprimer tous les conteneurs :**
```bash
docker stop $(docker ps -q)
docker rm $(docker ps -aq)
```


##  Commandes Docker essentielles

| Commande | Description |
|----------|-------------|
| `docker build -t nom .` | Construire une image |
| `docker images` | Lister les images locales |
| `docker tag image new-tag` | Taguer une image |
| `docker run -it -p 5000:5000 image` | Exécuter un conteneur (mode interactif) |
| `docker run -d -it -p 5000:5000 image` | Exécuter en arrière-plan (mode détaché) |
| `docker ps` | Conteneurs en cours d'exécution |
| `docker ps -a` | Tous les conteneurs |
| `docker logs <nom>` | Afficher les logs |
| `docker stop <nom>` | Arrêter un conteneur |
| `docker rm <nom>` | Supprimer un conteneur |
| `docker rmi <image>` | Supprimer une image |
| `docker login` | Se connecter à Docker Hub |
| `docker push <image>` | Pousser vers Docker Hub |
| `docker pull <image>` | Récupérer depuis Docker Hub |

##  Dépannage

### Le conteneur s'arrête immédiatement
```bash
docker logs <nom-conteneur>
```

### Le port est déjà utilisé
```bash
docker run -it -p 5001:5000 -e APP_COLOR=blue votre-username/color-app:latest
```

### Erreur lors du push vers Docker Hub
Vérifiez que vous êtes connecté :
```bash
docker login
```

Vérifiez que le tag contient votre username :
```bash
docker tag color-app votre-username/color-app:latest
```

### L'image n'est pas trouvée
```bash
docker pull votre-username/color-app:latest
```

##  Liens utiles

- Docker Hub : https://hub.docker.com/
- Documentation Docker : https://docs.docker.com/

---
