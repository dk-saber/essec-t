#  Docker Compose

##  Introduction
Jusqu’ici, vous lancez vos conteneurs avec des commandes comme :

```bash
docker run -d -p 5000:80 mywebapp
```

Mais si votre application a plusieurs services (ex. une app Flask + Redis + Postgres + un worker Node.js), ces commandes deviennent vite compliquées à gérer.

 **Docker Compose** permet de tout définir dans un fichier unique en YAML (`docker-compose.yml`), puis de tout démarrer en une seule commande :

```bash
docker compose up
```

---

##  Principe général
Docker Compose repose sur 3 éléments clés :

- **docker-compose.yml** → le fichier de configuration
- **docker compose up** → lance tous les conteneurs
- **docker compose down** → arrête et supprime tout

---

##  Exemple d’application — *Application de votre*
Un projet officiel de Docker qui réunit plusieurs technologies :

| Service | Langage / rôle | Dépend de |
|---------|---------------|-----------|
| vote    | Python Flask (front-end) | Redis |
| result  | Node.js (affiche les résultats) | Postgres |
| worker  | .NET (traite les votes) | Redis + Postgres |
| redis   | Base en mémoire | — |
| db      | PostgreSQL | — |

**Architecture simplifiée :**
```
vote (Flask) → Redis → worker (.NET) → Postgres → result (Node.js)
```

---

##  Étape 1 – Démarrage manuel avec `docker run`
Avant Docker Compose, vous devez lancer les conteneurs un par un :

```bash
docker run -d --name redis redis
docker run -d --name db postgres
docker run -d -p 5000:80 --name vote voting-app
docker run -d -p 5001:80 --name result result-app
docker run -d --name worker worker-app
```

Mais… rien ne fonctionne ! Les conteneurs ne se connaissent pas entre eux.

---

##  Étape 2 – Liaison entre conteneurs (legacy)
Avant, on utilisait `--link` :

```bash
docker run -d --name vote --link redis:redis -p 5000:80 voting-app
```

 **Les liens (`--link`) sont dépréciés depuis Docker 1.13.**

---

##  Étape 3 – Création du `docker-compose.yml`

###  Version 1 (ancienne)
```yaml
redis:
  image: redis

db:
  image: postgres

vote:
  image: voting-app
  ports:
    - "5000:80"
  links:
    - redis

result:
  image: result-app
  ports:
    - "5001:80"
  links:
    - db

worker:
  image: worker-app
  links:
    - redis
    - db
```

 Les `links` étaient encore utilisés ici.

---

###  Version 2 : `services:` et `depends_on`
```yaml
version: "2"

services:
  redis:
    image: redis

  db:
    image: postgres

  vote:
    image: voting-app
    ports:
      - "5000:80"
    depends_on:
      - redis

  result:
    image: result-app
    ports:
      - "5001:80"
    depends_on:
      - db

  worker:
    image: worker-app
    depends_on:
      - redis
      - db
```

 `depends_on` définit l’ordre de démarrage.  
 Plus besoin de `links`: Docker crée un réseau interne.

---

###  Version 3 (actuelle)
```yaml
version: "3"

services:
  redis:
    image: redis
    networks:
      - backend

  db:
    image: postgres
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    networks:
      - backend

  vote:
    build: ./vote
    ports:
      - "5000:80"
    depends_on:
      - redis
    networks:
      - frontend
      - backend

  result:
    build: ./result
    ports:
      - "5001:80"
    depends_on:
      - db
    networks:
      - frontend
      - backend

  worker:
    build: ./worker
    depends_on:
      - redis
      - db
    networks:
      - backend

networks:
  frontend:
  backend:
```

---
###  Différences entre Docker Compose **Version 2** et **Version 3**

| **Caractéristique**       | **Version 2**                                  | **Version 3**                                      |
|---------------------------|-----------------------------------------------|---------------------------------------------------|
| **Objectif principal**    | Déploiement local avec `docker-compose`       | Compatibilité avec **Docker Swarm** (production) |
| **Syntaxe clé**           | `services:` + `depends_on`                   | Ajout de `deploy:`, `configs:`, `secrets:`      |
| **Gestion des dépendances** | `depends_on` garantit l’ordre de démarrage    | `depends_on` existe mais **ne garantit pas** que le service est prêt (utiliser `healthcheck`) |
| **Réseaux & Volumes**     | Basique                                       | Plus flexible, multi-réseaux, volumes nommés     |
| **Orchestration**         | Non supportée                                 | Support Swarm (scaling, contraintes, ressources) |
| **Options avancées**      | Limitées                                      | `deploy:` (réplicas, ressources), secrets, configs |
| **Compatibilité**         | Idéal pour développement local                | Recommandée pour production et clusters          |

---
##  Réseaux dans Docker Compose
- Docker Compose crée automatiquement un réseau interne isolé.
- Chaque conteneur peut être connecté à plusieurs réseaux :
  - **frontend** → services exposés aux utilisateurs
  - **backend** → communication interne

---

##  Commandes principales
| Commande | Description |
|----------|-------------|
| `docker compose up` | Crée et démarre tous les conteneurs |
| `docker compose down` | Supprime les conteneurs, réseaux, etc. |
| `docker compose ps` | Liste les services en cours |
| `docker compose logs -f` | Affiche les logs |
| `docker compose build` | Reconstruit les images locales |
| `docker compose up -d` | Lance en arrière-plan |

---

##  Points importants
- Le nom du projet correspond par défaut au nom du dossier.
- Si une image n’existe pas, vous pouvez utiliser :
  ```yaml
  build: ./vote
  ```
- Chaque service peut avoir :
  - `environment:` pour les variables
  - `volumes:` pour les données
  - `depends_on:` pour l’ordre
  - `ports:` pour exposer des services

---

##  Conclusion
 Docker Compose simplifie radicalement la gestion d’applications multi-conteneurs.  
Une seule commande (`docker compose up`) permet de lancer toute la stack avec gestion automatique des réseaux et dépendances.
