# Chapitre III.1 : Les Commandes Docker

## Table des matières

- [Introduction](#introduction)
- [Les commandes de bases](#les-commandes-de-bases)
  - [Lancer un conteneur](#lancer-un-conteneur)
  - [Lister les conteneurs](#lister-les-conteneurs)
  - [Arrêter et supprimer un conteneur](#arrêter-et-supprimer-un-conteneur)
  - [Gérer les images](#gérer-les-images)
  - [Télécharger une image sans l'exécuter](#télécharger-une-image-sans-lexécuter)
  - [Pourquoi certains conteneurs s'arrêtent immédiatement](#pourquoi-certains-conteneurs-sarrêtent-immédiatement)
  - [Exécuter une commande dans un conteneur en cours d'exécution](#exécuter-une-commande-dans-un-conteneur-en-cours-dexécution)
  - [Mode attaché vs détaché](#mode-attaché-vs-détaché)
- [Commandes avancées](#commandes-avancées)
  - [Exécuter une image avec une version donnée (Tag)](#exécuter-une-image-avec-une-version-donnée-tag)
  - [Interactivité dans les conteneurs (-i et -t)](#interactivité-dans-les-conteneurs--i-et--t)
  - [Mappage des ports (Port Mapping)](#mappage-des-ports-port-mapping)
  - [Persistance des données (Volumes)](#persistance-des-données-volumes)
  - [Inspecter un conteneur (docker inspect)](#inspecter-un-conteneur-docker-inspect)
  - [Consulter les journaux (docker logs)](#consulter-les-journaux-docker-logs)
- [Conclusion](#conclusion)

## Introduction

Dans cette partie, nous allons découvrir les principales commandes Docker indispensables pour manipuler des conteneurs et des images.

À la fin de ce chapitre, vous serez en mesure de créer, exécuter, inspecter, arrêter et supprimer des conteneurs, ainsi que de gérer vos images Docker efficacement.

## Les commandes de bases

### Lancer un conteneur

La commande `docker run` permet d'exécuter un conteneur à partir d'une image.

**Exemple :**
```bash
docker run nginx
```

Cette commande exécute un conteneur basé sur l'image nginx.

- Si l'image est déjà présente localement, Docker l'utilise directement.
- Si elle n'existe pas sur l'hôte, Docker la télécharge automatiquement depuis Docker Hub (le registre public d'images).

Ce téléchargement n'a lieu que la première fois. Par la suite, Docker réutilise l'image déjà stockée localement.

### Lister les conteneurs

Pour afficher tous les conteneurs en cours d'exécution, utilisez :

```bash
docker ps
```

Cette commande affiche des informations clés :
- L'ID du conteneur
- L'image utilisée
- Le statut du conteneur
- Son nom généré automatiquement par Docker

Pour afficher tous les conteneurs, y compris ceux qui sont arrêtés, ajoutez l'option `-a` :

```bash
docker ps -a
```

### Arrêter et supprimer un conteneur

Pour arrêter un conteneur en cours d'exécution :

```bash
docker stop <nom_ou_ID_du_conteneur>
```

Ensuite, pour le supprimer définitivement :

```bash
docker rm <nom_ou_ID_du_conteneur>
```

### Gérer les images

Pour lister toutes les images présentes sur votre machine :

```bash
docker images
```

Vous y verrez le nom, la version (tag), et la taille de chaque image.

Pour supprimer une image inutilisée :

```bash
docker rmi <nom_ou_ID_de_l'image>
```

⚠️ **Note :** Vous devez d'abord supprimer les conteneurs qui utilisent cette image avant de pouvoir la retirer.

### Télécharger une image sans l'exécuter

Si vous souhaitez simplement télécharger une image sans lancer de conteneur :

```bash
docker pull ubuntu
```

Ainsi, lors d'un futur `docker run`, l'image sera déjà disponible localement.

### Pourquoi certains conteneurs s'arrêtent immédiatement

Si vous exécutez :

```bash
docker run ubuntu
```

vous constaterez que le conteneur s'exécute puis s'arrête immédiatement.

Cela s'explique par le fait qu'**un conteneur n'est pas une machine virtuelle** : il ne tourne que tant qu'un processus actif s'exécute à l'intérieur.

**Exemple :**

```bash
docker run ubuntu sleep 5
```

Le conteneur exécute la commande `sleep 5` (pause de 5 secondes), puis s'arrête dès que la commande est terminée.

### Exécuter une commande dans un conteneur en cours d'exécution

Pour exécuter une commande à l'intérieur d'un conteneur déjà lancé, utilisez :

```bash
docker exec <nom_du_conteneur> <commande>
```

**Exemple :**

```bash
docker exec ubuntu-container cat /etc/hosts
```

Cette commande affiche le contenu du fichier `/etc/hosts` à l'intérieur du conteneur spécifié.

### Mode attaché vs détaché

Par défaut, un conteneur s'exécute en **mode attaché** (foreground), c'est-à-dire que vous voyez la sortie de son exécution dans votre terminal. Le terminal est bloqué jusqu'à ce que le conteneur s'arrête.

Pour exécuter le conteneur en arrière-plan (mode détaché), ajoutez l'option `-d` :

```bash
docker run -d jenkins/jenkins
```

Vous récupérez immédiatement la main sur votre terminal, et le conteneur continue de fonctionner en tâche de fond.

Pour vous reconnecter à un conteneur en cours d'exécution :

```bash
docker attach <nom_ou_ID_du_conteneur>
```

## Commandes avancées

Dans cette section, nous allons approfondir les commandes docker run et découvrir plusieurs fonctionnalités essentielles :
- L'exécution d'images avec différentes versions
- L'interactivité dans les conteneurs
- Le mappage des ports
- La persistance des données
- L'inspection et les journaux des conteneurs

### Exécuter une image avec une version donnée (Tag)

Jusqu'à présent, nous avons vu qu'il est possible d'exécuter un conteneur Redis avec la commande suivante :

```bash
docker run redis
```

Cela télécharge et exécute la dernière version disponible de Redis (par exemple, la version 8.2.2).

Mais que faire si vous souhaitez exécuter une version antérieure, comme la 7.4 ?

Il suffit d'utiliser la notation de tag (ou balise) :

```bash
docker run redis:7.4
```

Le **tag** est une étiquette qui identifie la version de l'image.

Si vous ne précisez aucun tag, Docker utilisera `latest` par défaut, ce qui correspond à la dernière version publiée par les développeurs.

**Pour consulter la liste de toutes les versions disponibles d'une image :**
- Allez sur Docker Hub puis recherchez l'image (par exemple `redis`)
- Vous y verrez tous les tags supportés, avec leur numéro de version et leurs variantes

### Interactivité dans les conteneurs (-i et -t)

Imaginons que vous ayez une petite application qui vous demande votre nom, puis affiche un message de bienvenue.

Si vous la conteneurisez et l'exécutez avec Docker sans option particulière :

```bash
docker run monapp
```

Le conteneur s'exécute, affiche son message, puis s'arrête sans attendre votre saisie.

Par défaut, un conteneur Docker ne lit pas l'entrée standard (stdin) et n'a pas de terminal attaché.

Pour interagir avec le conteneur, vous devez activer deux options :
- **`-i`** (interactive) : permet de transmettre les entrées du clavier vers le conteneur
- **`-t`** (tty) : attache un terminal interactif (pseudo-terminal)

Ainsi :

```bash
docker run -it monapp
```

Vous pouvez maintenant entrer votre nom, voir le prompt et obtenir la réponse du programme.

### Mappage des ports (Port Mapping)

Lorsqu'une application web s'exécute à l'intérieur d'un conteneur, elle écoute souvent sur un port interne (par exemple 5000).

Mais comment y accéder depuis votre navigateur ?

Chaque conteneur Docker reçoit une adresse IP interne (par exemple : `172.17.0.2`), accessible uniquement depuis le Docker Host.

Ainsi, depuis la machine hôte, vous pouvez accéder à l'application via : `http://172.17.0.2:5000`

Mais cette adresse n'est pas accessible depuis l'extérieur. Pour la rendre accessible depuis votre réseau local, vous devez mapper un port du conteneur à un port de l'hôte :

```bash
docker run -p 80:5000 monwebapp
```

- `-p` = port
- `5000` = numéro de port utilisé par l'application à l'intérieur du conteneur
- `80` = numéro de port exposé sur la machine hôte

Les utilisateurs peuvent désormais accéder à l'application via : `http://ip-docker-host:80`

Vous pouvez exécuter plusieurs conteneurs sur des ports différents :

```bash
docker run -p 3306:3306 mysql
docker run -p 8306:3306 mysql
```

⚠️ **Attention :** Un même port hôte ne peut être mappé qu'une seule fois.

**Exemple avec nginx :**

```bash
docker run --name mon-app-nginx -d -p 8080:80 nginx
```

### Persistance des données (Volumes)

Par défaut, les fichiers et données créés dans un conteneur sont stockés à l'intérieur de son système de fichiers isolé. Cela signifie que si vous supprimez le conteneur, toutes les données sont perdues.

**Exemple :**

Lancez un conteneur nginx nommé `mon-nginx`. Le fichier `index.html` est enregistré dans : `/usr/share/nginx/html`

Si vous supprimez le conteneur avec `docker rm mon-nginx`, toutes les données sont effacées.

Pour éviter cela, Docker permet de monter un **volume persistant** (un dossier de l'hôte visible dans le conteneur) :

**Étapes :**

1. Créez un dossier et un fichier HTML personnalisé :

```bash
mkdir data-nginx
cd data-nginx/
pwd
echo "<h1>Bienvenue sur mon site Nginx via volume Docker</h1>" > /root/data-nginx/index.html
cat /root/data-nginx/index.html
```

2. Lancez un container nginx-volume :

```bash
docker run -d --name nginx-volume -p 8080:80 -v /root/data-nginx:/usr/share/nginx/html nginx
```

Ainsi :
- `-v` : volume
- `/root/data-nginx` : dossier sur l'hôte (vos fichiers restent même après suppression du conteneur)
- `:/usr/share/nginx/html` : emplacement des fichiers de données dans le conteneur

3. Vérifiez le contenu :

```bash
docker exec -it nginx-volume cat /usr/share/nginx/html/index.html
```

4. Supprimez le container :

```bash
docker stop nginx-volume
docker rm nginx-volume
```

5. Relancez un nouveau container :

```bash
docker run -d --name nginx-volume -p 8080:80 -v /root/data-nginx:/usr/share/nginx/html nginx
docker exec -it nginx-volume cat /usr/share/nginx/html/index.html
```

**Résultat :** Vos données sont sauvegardées et persistantes, même si le conteneur est supprimé ou redéployé.

### Inspecter un conteneur (docker inspect)

La commande :

```bash
docker inspect <nom_ou_ID_du_conteneur>
```

Affiche tous les détails techniques d'un conteneur sous format JSON :
- État actuel (en cours, arrêté, redémarré, etc.)
- Volumes montés
- Réseau et adresses IP
- Variables d'environnement
- Configuration complète

C'est une commande très utile pour le diagnostic et la vérification de configuration.

### Consulter les journaux (docker logs)

Lorsqu'un conteneur est lancé en mode détaché (`-d`), vous ne voyez pas les messages affichés par l'application.

Pour consulter les journaux :

```bash
docker logs <nom_ou_ID_du_conteneur>
```

Cela permet d'afficher le **contenu de la sortie standard (stdout)**, c'est-à-dire tout ce que le conteneur a imprimé depuis son démarrage.

## Conclusion

Grâce à la conteneurisation, il devient possible d'exécuter plusieurs environnements isolés sur une même machine, sans les contraintes liées à la compatibilité des systèmes ou aux dépendances.

Contrairement aux machines virtuelles, Docker ne virtualise pas un système d'exploitation complet, il partage le noyau de l'OS hôte, ce qui le rend plus léger, plus rapide et plus flexible.
