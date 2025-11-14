#  Docker Images

##  Introduction

Une **image Docker** est la base de tout conteneur Docker. C'est une photographie figée d'un environnement logiciel (système, dépendances, application, configuration) à partir de laquelle on crée un conteneur exécutable.

On utilise souvent des images prêtes à l'emploi depuis Docker Hub, mais dans de nombreux cas, on souhaite créer sa propre image personnalisée :
- Soit parce qu'aucune image ne correspond exactement à nos besoins
- Soit parce qu'on veut packager notre propre application pour faciliter son déploiement sur n'importe quel environnement

---

##  1. Pourquoi créer sa propre image ?

### Exemple concret

Imaginons le déploiement d'une application Python Flask.

**Si cela était fait manuellement :**
1. Installer un système d'exploitation (ex. Ubuntu)
2. Mettre à jour les dépôts : `apt-get update`
3. Installer Python et les dépendances : `apt-get install python3-pip`
4. Installer les librairies Flask : `pip install flask`
5. Copier votre code dans `/opt/app`
6. Lancer le serveur : `flask run`

 **Toutes ces étapes manuelles peuvent être automatisées dans un Dockerfile**, afin de construire une image réutilisable et portable.

---

##  2. Le Dockerfile

Un **Dockerfile** est un fichier texte contenant les instructions nécessaires à la construction d'une image. Chaque ligne représente une commande Docker.

### Exemple de Dockerfile

```dockerfile
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3-pip
COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]
```

###  Décryptage des instructions

| Instruction | Rôle |
|------------|------|
| `FROM` | Spécifie l'image de base (ici Ubuntu 20.04). C'est toujours la première ligne. |
| `RUN` | Exécute des commandes à l'intérieur de l'image lors de la construction (installation, configuration…). |
| `COPY` | Copie des fichiers du répertoire local vers l'image. |
| `WORKDIR` | Définit le dossier de travail dans l'image. |
| `ENTRYPOINT` | Définit la commande principale exécutée quand le conteneur démarre. |

---

##  3. Construction d'une image

Une fois le Dockerfile prêt, on peut construire l'image à l'aide de :

```bash
docker build -t monapp:1.0 .
```

- `-t monapp:1.0` : donne un nom et une version à l'image
- `.` : indique que le Dockerfile se trouve dans le répertoire courant

 **Docker va lire chaque ligne du Dockerfile et créer une image en couches (layers).**

---

##  4. Architecture en couches (Layered Architecture)

Chaque instruction du Dockerfile crée une nouvelle couche :

| Étape | Instruction | Effet | Taille estimée |
|-------|------------|-------|----------------|
| 1 | `FROM ubuntu:20.04` | OS de base | ~120 MB |
| 2 | `RUN apt-get install` | Dépendances système | ~300 MB |
| 3 | `RUN pip install` | Librairies Python | ~50 MB |
| 4 | `COPY` | Code source | ~10 MB |
| 5 | `ENTRYPOINT` | Configuration finale | – |

**Chaque couche n'ajoute que les modifications par rapport à la précédente.**

###  Avantage du cache

Si l'image est reconstruite après une petite modification du code source, Docker **réutilise les couches précédentes (cache)** et ne reconstruit que la dernière partie. Cela rend le build **plus rapide et plus efficace**.

---

##  5. Commandes utiles

| Commande | Description |
|----------|-------------|
| `docker images` | Liste toutes les images locales |
| `docker build -t nom_image .` | Construit une image à partir du Dockerfile |
| `docker history nom_image` | Affiche l'historique des couches |
| `docker rmi nom_image` | Supprime une image |
| `docker push nom_image` | Envoie l'image sur Docker Hub |
| `docker pull nom_image` | Télécharge une image depuis Docker Hub |

---

##  6. Publication sur Docker Hub

Une fois l'image prête, elle peut être partagée sur Docker Hub :

```bash
# Connexion à Docker Hub
docker login

# Taguer l'image pour votre compte Docker Hub
docker tag monapp:1.0 dk-saber/monapp:1.0

# Pousser l'image vers Docker Hub
docker push dk-saber/monapp:1.0
```

 **L'image devient alors publique** et peut être utilisée par d'autres :

```bash
docker run dk-saber/monapp:1.0
```

---

##  7. Résumé visuel du processus

```
[Dockerfile]
     │
     ▼
docker build  →  [Image]
     │
     ▼
docker run    →  [Container]
```

- Le **Dockerfile** contient les instructions
- Le **build** crée l'image
- Le **run** exécute cette image sous forme de conteneur

---

##  Conclusion

Les **Docker images** sont la base de tout l'écosystème Docker. Elles encapsulent tout ce dont votre application a besoin pour fonctionner : système, bibliothèques, code et configuration.

### Grâce à elles :
-  Les applications sont **portables** (même environnement partout)
-  Les déploiements sont **rapides et reproductibles**
-  Les mises à jour ne reconstruisent que ce qui a changé

---

##  Ressources

- [Documentation officielle Docker](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

---

**Auteur :** [dk-saber](https://github.com/dk-saber)
