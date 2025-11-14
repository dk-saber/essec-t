# Docker : Variables d'environnement et Entrypoint

## Table des matières
- [Variables d'environnement](#variables-denvironnement)
- [Commands, Arguments et Entrypoint](#commands-arguments-et-entrypoint)

---

## Variables d'environnement

### Problématique

Lors du développement d'une application web en Python, il est courant de définir des paramètres comme la couleur de fond directement dans le code. Par exemple, une ligne pourrait définir la couleur de fond en rouge. Bien que cela fonctionne, modifier cette couleur nécessite de changer le code source de l'application, ce qui n'est pas une bonne pratique.

### Solution : Variables d'environnement

Il est recommandé de déplacer ces informations de configuration hors du code et de les stocker dans des **variables d'environnement**. Par exemple, créez une variable d'environnement appelée `APP_COLOR`.

```bash
export APP_COLOR=blue
```

Lors de l'exécution de l'application, celle-ci lira la valeur de cette variable et appliquera la couleur correspondante.

### Utilisation avec Docker

Une fois votre application empaquetée dans une image Docker, vous pouvez passer des variables d'environnement lors de l'exécution du conteneur avec l'option `-e` :

```bash
docker run -e APP_COLOR=blue nom-de-image
```

Pour déployer plusieurs conteneurs avec des couleurs différentes :

```bash
docker run -e APP_COLOR=blue nom-de-image
docker run -e APP_COLOR=green nom-de-image
docker run -e APP_COLOR=red nom-de-image
```

### Inspection des variables d'environnement

Pour vérifier les variables d'environnement d'un conteneur en cours d'exécution :

```bash
docker inspect nom-du-conteneur
```

Les variables d'environnement se trouvent dans la section `Config` du résultat.

---

## Commands, Arguments et Entrypoint

### Cycle de vie d'un conteneur

Contrairement aux machines virtuelles, **les conteneurs ne sont pas destinés à héberger un système d'exploitation**. Ils sont conçus pour exécuter une tâche ou un processus spécifique :
- Serveur web
- Serveur d'applications
- Base de données
- Calculs ou analyses

**Un conteneur ne vit que tant que le processus à l'intérieur est actif.** Une fois la tâche terminée, le conteneur s'arrête.

### Exemple avec Ubuntu

```bash
docker run ubuntu
```

Ce conteneur démarre et s'arrête immédiatement. Pourquoi ?

Le Dockerfile d'Ubuntu définit `bash` comme commande par défaut. Bash est un shell qui attend des entrées depuis un terminal. Comme Docker n'attache pas de terminal par défaut, bash ne trouve pas de terminal et s'arrête, provoquant l'arrêt du conteneur.

### L'instruction CMD

L'instruction `CMD` dans un Dockerfile définit le programme qui s'exécutera au démarrage du conteneur.

**Exemples :**
- Image nginx : `CMD ["nginx"]`
- Image MySQL : `CMD ["mysqld"]`
- Image Ubuntu : `CMD ["bash"]`

### Override de la commande par défaut

Vous pouvez remplacer la commande par défaut en l'ajoutant à la commande `docker run` :

```bash
docker run ubuntu sleep 5
```

Le conteneur exécutera `sleep 5` au lieu de `bash`, attendra 5 secondes, puis s'arrêtera.

### Créer une image personnalisée

Pour rendre ce changement permanent, créez votre propre image :

**Dockerfile :**
```dockerfile
FROM ubuntu
CMD ["sleep", "5"]
```

Ou en format shell :
```dockerfile
FROM ubuntu
CMD sleep 5
```

**Note :** En format JSON array, le premier élément doit être l'exécutable, et les paramètres doivent être des éléments séparés.

**Build et exécution :**
```bash
docker build -t ubuntu-sleeper .
docker run ubuntu-sleeper
```

### Passer des paramètres dynamiques

Pour changer le nombre de secondes :

```bash
docker run ubuntu-sleeper sleep 10
```

Mais cela nécessite de répéter la commande `sleep`, ce qui n'est pas idéal.

### L'instruction ENTRYPOINT

`ENTRYPOINT` définit le programme qui sera toujours exécuté, et les paramètres de la ligne de commande y seront **ajoutés** (et non remplacés).

**Dockerfile :**
```dockerfile
FROM ubuntu
ENTRYPOINT ["sleep"]
```

**Exécution :**
```bash
docker build -t ubuntu-sleeper .
docker run ubuntu-sleeper 10
```

Le conteneur exécutera `sleep 10`.

### Différence entre CMD et ENTRYPOINT

| Instruction | Comportement |
|-------------|--------------|
| **CMD** | Les paramètres de la ligne de commande **remplacent** complètement CMD |
| **ENTRYPOINT** | Les paramètres de la ligne de commande sont **ajoutés** à ENTRYPOINT |

### Valeur par défaut avec ENTRYPOINT + CMD

Pour définir une valeur par défaut si aucun paramètre n'est fourni :

**Dockerfile :**
```dockerfile
FROM ubuntu
ENTRYPOINT ["sleep"]
CMD ["5"]
```

**Comportement :**
- `docker run ubuntu-sleeper` → exécute `sleep 5`
- `docker run ubuntu-sleeper 10` → exécute `sleep 10`

**Important :** Les deux instructions doivent être au format JSON array pour fonctionner ensemble.

### Override de ENTRYPOINT au runtime

Pour modifier l'entrypoint lors de l'exécution :

```bash
docker run --entrypoint sleep2.0 ubuntu-sleeper 10
```

La commande finale sera `sleep2.0 10`.

---

## Résumé

- **Variables d'environnement** : Utilisez `-e` pour passer des configurations au conteneur
- **CMD** : Définit la commande par défaut, peut être remplacée
- **ENTRYPOINT** : Définit le programme principal, les paramètres sont ajoutés
- **CMD + ENTRYPOINT** : Combinaison pour des valeurs par défaut flexibles
- **Inspection** : Utilisez `docker inspect` pour voir la configuration d'un conteneur

---
