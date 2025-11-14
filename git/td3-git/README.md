# Travaux Dirigés Git

## 1. Initialisation d'un dépôt Git

### 1.1 Commande d'initialisation
**Question :** Quelle est la commande pour initialiser un dépôt Git ?

<details>
<summary>Voir la réponse</summary>

<br>

**Réponse :** `git init`

</details>

---

### 1.2 Créer et initialiser un projet
Initialisez un dépôt Git dans le répertoire `/home/utilisateur/projet-blog`

Créez le répertoire s'il n'existe pas déjà.

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`mkdir -p /home/utilisateur/projet-blog`

`cd /home/utilisateur/projet-blog`

`git init`

</details>

---

### 1.3 Les trois zones de Git
**Question :** Une fois un dépôt Git initialisé, quelle zone contient les modifications actives dans votre dépôt Git local ?

<details>
<summary>Voir la réponse</summary>

<br>

**Réponse :** Le répertoire de travail (Working Directory)

</details>

---

### 1.4 Ajouter un fichier au projet
Ajoutons un fichier à notre projet dans `/home/utilisateur/projet-blog`

**Nom du fichier :** `article.txt`

**Contenu du fichier :** `Introduction au développement web moderne`

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`cd /home/utilisateur/projet-blog`

`echo "Introduction au développement web moderne" > article.txt`

</details>

---

### 1.5 La zone de staging
**Question :** Quelle zone contient les nouvelles modifications qui seront bientôt committées dans le dépôt Git local ?

<details>
<summary>Voir la réponse</summary>

<br>

**Réponse :** La zone de staging (Index)

</details>

---

### 1.6 Vérifier le statut du dépôt
Maintenant que nous avons ajouté un fichier texte, voyons si Git a détecté le changement. Bien que nous n'ayons encore rien fait avec Git, nous avons initialisé un dépôt, donc Git est conscient de tous nos fichiers et changements.

Vous pouvez voir le statut de Git en exécutant la commande `git status`.

<details>
<summary>Voir la commande</summary>

<br>

**Commande :** `git status`

</details>

Répondez aux questions suivantes basées sur la sortie de la commande `git status`.

---

### 1.7 Nombre de commits
**Question :** Combien de commits sont listés dans le dépôt Git ?

<details>
<summary>Voir la réponse</summary>

<br>

**Réponse :** 0 (aucun commit n'a encore été effectué)

</details>

---

### 1.8 Statut du fichier
**Question :** Quel est le statut du fichier `article.txt` dans le dépôt ?

<details>
<summary>Voir la réponse</summary>

<br>

**Réponse :** Untracked (non suivi)

</details>

---

### 1.9 Zone du fichier
**Question :** Dans quelle zone du dépôt Git local se trouve le fichier `article.txt` ?

<details>
<summary>Voir la réponse</summary>

<br>

**Réponse :** Working Directory (Répertoire de travail)

</details>

---

### 1.10 Ajouter le fichier au staging
Ajoutez le fichier `article.txt` au staging pour le rendre disponible pour un commit.

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git add article.txt`

</details>

---

### 1.11 Configuration de l'utilisateur Git
Maintenant, il est temps de committer notre changement ! Un commit enregistre le changement dans le dépôt par rapport à son état précédent. Mais avant cela, nous devons configurer l'utilisateur Git qui sera le propriétaire du commit.

Configurez le nom d'utilisateur Git comme `dev` et l'email comme `dev@exemple.com` en utilisant les commandes ci-dessous.

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`git config user.email dev@exemple.com`

`git config user.name dev`

</details>

---

### 1.12 Premier commit
Committons notre changement ! Dans ce cas, nous n'avions pas de commits précédents, donc l'ajout du fichier `article.txt` est un changement par rapport à son état précédent.

Committez les fichiers qui sont actuellement dans la zone de staging.

Vérifiez d'abord le statut du fichier avec `git status`. Ensuite, committez avec le message `Ajout du premier article`

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`git status`

`git commit -m "Ajout du premier article"`

</details>

---

### 1.13 Fichier à ignorer
Le développeur crée un nouveau fichier nommé `brouillon.txt` où il prévoit d'écrire des idées pour les articles à des fins personnelles. Il ne veut pas que Git suive ce fichier ou le partage avec son équipe.

**Question :** Quel est le statut actuel du fichier `brouillon.txt` ?

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`touch brouillon.txt`

`git status`

**Réponse :** Untracked (non suivi)

</details>

---

### 1.14 Utiliser .gitignore
C'est bien que le fichier soit non suivi. Mais il est toujours sous le radar de Git. Si vous exécutez accidentellement la commande `git add .`, Git commencera à suivre ce fichier.

Configurons Git pour ignorer ce fichier de manière permanente.

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `echo "brouillon.txt" > .gitignore`

</details>

---

### 1.15 Vérifier l'effet de .gitignore
**Question :** Quel est le statut du fichier `brouillon.txt` maintenant dans la sortie de la commande `git status` ?

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git status`

**Réponse :** Le fichier `brouillon.txt` n'apparaît plus. Seul `.gitignore` apparaît comme fichier non suivi.

</details>

---

### 1.16 Suivre le fichier .gitignore
Comme vous avez pu le remarquer, le fichier `.gitignore` lui-même peut être listé comme non suivi. C'est une bonne pratique de suivre le fichier `.gitignore` avec Git.

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`git add .gitignore`

`git commit -m "Ajout du fichier gitignore"`

</details>

---

### 1.17 Analyser un autre dépôt
Explorons un autre dépôt Git. Nous avons un dépôt utilisé pour le développement d'une application cloné à `/home/utilisateur/app-gestion`.

Identifiez l'état du dépôt Git. Combien de fichiers sont en staging et combien ne le sont pas ?

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`cd /home/utilisateur/app-gestion`

`git status`

Comptez les fichiers listés sous "Changes to be committed" (en staging) et ceux sous "Changes not staged for commit" ou "Untracked files".

</details>

---

### 1.18 Commits multiples
On vous demande de committer le fichier `documentation.md` avec le message de commit `Mise a jour de la documentation` et le fichier `css/style.css` avec le message `Modification des couleurs du theme`

Notez que le fichier `documentation.md` est déjà en staging. Vous devez donc simplement le committer. Le fichier `css/style.css` doit être committé dans un commit séparé.

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`git commit -m "Mise a jour de la documentation"`

`git add css/style.css`

`git commit -m "Modification des couleurs du theme"`

</details>

---

## 2. Historique Git et Logs

### 2.1 Vérifier l'historique Git
Nous avons initialisé un dépôt Git dans `/home/utilisateur/projet-blog`. Vérifiez la sortie de la commande `git log` dans ce répertoire.

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`cd /home/utilisateur/projet-blog`

`git log`

Si aucun fichier n'a encore été committé, vous devriez voir le message : `fatal: your current branch 'master' does not have any commits yet`

</details>

---

### 2.2 Commit initial
Le développeur a écrit un article `article.txt` dans `/home/utilisateur/projet-blog/`. Veuillez le committer dans le dépôt Git local.

**Message de commit :** `Ajout du premier article`

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`git add .`

`git commit -m "Ajout du premier article"`

</details>

---

### 2.3 Analyser git log
Nous avons committé le fichier `article.txt` dans le dépôt Git `/home/utilisateur/projet-blog`. Vérifiez la sortie de la commande `git log` dans ce répertoire.

<details>
<summary>Voir la commande</summary>

<br>

**Commande :** `git log`

En fonction de la sortie de la commande, répondez aux questions suivantes.

</details>

---

### 2.4 Informations dans git log
**Question :** Quelle information n'est PAS affichée dans `git log` ?

**Options possibles :**
- Hash du commit
- Auteur
- Date
- Fichiers modifiés

<details>
<summary>Voir la réponse</summary>

<br>

**Réponse :** Fichiers modifiés (par défaut)

</details>

---

### 2.5 Option --name-only
Vous pouvez lister les fichiers modifiés en utilisant l'option `--name-only` avec la commande `git log`.

<details>
<summary>Voir la commande</summary>

<br>

**Commande :** `git log --name-only`

</details>

---

### 2.6 Identifier la branche
**Question :** Sur quelle branche les changements ont-ils été committés ?

L'information de la branche peut être vue dans la première ligne de la sortie de `git log` où `(HEAD -> {NOM_BRANCHE})` est affiché.

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git log`

**Réponse :** master

</details>

---

### 2.7 Auteur du commit
**Question :** Qui est l'auteur du commit dans le dépôt Git ?

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git log`

**Réponse :** dev

</details>

---

### 2.8 Nouveau commit par un autre utilisateur
Un autre utilisateur a committé un nouveau fichier dans le dépôt maintenant. Identifiez l'utilisateur et le nouveau fichier qui a été ajouté.

**Message de commit :** `Ajout d'un tutoriel`

Utilisez l'option `--name-only` pour voir les fichiers également.

<details>
<summary>Voir la commande</summary>

<br>

**Commande :** `git log --name-only`

</details>

---

### 2.9 Format compact de git log
**Question :** Quelle est l'option de la commande `git log` pour afficher les logs de manière compacte (un log par ligne) ?

**Options :**
- `--oneline`
- `--compact`
- `--short`
- `--brief`

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git log --oneline`

**Réponse :** `--oneline`

</details>

---

### 2.10 Explorer un autre dépôt
Un autre dépôt Git qui héberge le code d'une application de gestion est disponible à `/home/utilisateur/app-gestion`.

Explorez le dépôt, vérifiez les fichiers, le statut Git, les logs, etc.

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`cd /home/utilisateur/app-gestion`

`ls`

`git status`

`git log`

</details>

---

### 2.11 Limiter le nombre de commits affichés
Le dépôt contient de nombreux commits. Pouvez-vous essayer de lister uniquement les 5 derniers commits ?

Il devrait y avoir une option dans `git log` pour limiter la liste des sorties. Utilisez `git help log` si vous n'êtes pas sûr.

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git log -n 5`

ou

**Commande :** `git log -5`

</details>

---

### 2.12 Identifier le dernier commit
**Question :** Qui a effectué le dernier commit dans le nouveau dépôt ?

<details>
<summary>Voir la commande</summary>

<br>

**Commande :** `git log -n 1`

</details>

---

### 2.13 Identifier un développeur
**Question :** En jugeant par leurs actions, pouvez-vous deviner qui pourrait être le développeur CSS dans l'équipe ?

Regardez les logs et identifiez la personne qui a apporté des modifications au fichier `.css` récemment. Vous avez déjà appris l'option pour afficher les fichiers associés à un commit.

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`cd /home/utilisateur/app-gestion`

`git log --name-only`

Cherchez le commit qui a modifié le fichier `css/style.css`.

</details>

---

## 3. Branches et Fusion

### 3.1 Qu'est-ce qu'une branche ?
**Question :** Qu'est-ce qu'une branche dans Git ?

<details>
<summary>Voir la réponse</summary>

<br>

**Réponse :** Une branche n'est rien d'autre qu'un pointeur vers un commit spécifique dans Git.

</details>

---

### 3.2 Branche par défaut
**Question :** Quelle est la branche par défaut d'un dépôt Git ?

<details>
<summary>Voir la réponse</summary>

<br>

**Réponse :** Par défaut, la branche utilisée est `master` (ou `main` dans les versions plus récentes).

</details>

---

### 3.3 Activité du dépôt
Le développeur a travaillé sur un dépôt Git à `/home/utilisateur/projet-blog` et a écrit un article. Vérifiez la sortie de la commande `git log` dans ce répertoire pour voir l'activité.

**Question :** Quel est le nom du fichier créé par le développeur ?

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`cd /home/utilisateur/projet-blog`

`git log --name-only`

**Réponse :** `article.txt`

</details>

---

### 3.4 Branche du fichier
**Question :** Sur quelle branche le fichier `article.txt` a-t-il été committé dans le dépôt Git ?

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git log`

**Réponse :** master

</details>

---

### 3.5 Créer une nouvelle branche
Le développeur décide d'écrire un nouveau tutoriel - "Guide JavaScript". Créons et basculons vers une nouvelle branche nommée `article/javascript`

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git checkout -b article/javascript`

</details>

---

### 3.6 Position de HEAD
Affichez la sortie de la commande `git log` et identifiez la branche vers laquelle HEAD pointe maintenant.

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git log`

**Réponse :** `article/javascript`

</details>

---

### 3.7 Comprendre HEAD
Comme vous pouvez le voir, HEAD pointe toujours vers le dernier commit de la branche actuellement extraite.

---

### 3.8 Travail en cours
Le développeur est à mi-chemin du tutoriel "Guide JavaScript". Il n'est pas encore complet.

Visualisez le contenu qu'il a écrit dans le fichier `javascript.txt`

<details>
<summary>Voir la commande</summary>

<br>

**Commande :** `cat javascript.txt`

**Contenu :**
```
--------------------------------------------
      GUIDE JAVASCRIPT POUR DEBUTANTS
--------------------------------------------

JavaScript est un langage de programmation qui permet de rendre les pages web interactives.

Les variables en JavaScript peuvent être déclarées avec var, let ou const.

Les fonctions sont des blocs de code réutilisables qui effectuent une tâche spécifique.
```

</details>

---

### 3.9 Urgence sur la branche principale
Un collègue informe le développeur que dans son premier article, il y a une erreur de syntaxe qui doit être corrigée immédiatement !

Nous devons retourner et corriger l'article dans la branche master. Mais avant de faire cela, committons le nouveau tutoriel que nous avons écrit jusqu'à présent. Nous ne voulons pas transporter notre tutoriel incomplet vers la branche master.

Ajoutez au staging et committez le tutoriel avec le message `Ajout du guide JavaScript incomplet`

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`git add javascript.txt`

`git commit -m "Ajout du guide JavaScript incomplet"`

</details>

---

### 3.10 Retour à master
Maintenant, basculez vers la branche master.

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git checkout master`

</details>

---

### 3.11 Correction de l'erreur
Corrigeons l'erreur dans le fichier `article.txt`. Le mot "développement" est mal orthographié comme "developpment". Veuillez le corriger puis committer les changements.

**Message de commit :** `Correction de l'erreur de syntaxe`

Utilisez un éditeur pour modifier le fichier et corriger l'erreur. Ensuite, exécutez la commande :

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git commit -am "Correction de l'erreur de syntaxe"`

</details>

---

### 3.12 Retour au nouveau tutoriel
Parfait ! Maintenant que c'est réglé, finissons le guide JavaScript. Rebasculez vers la branche `article/javascript`.

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git checkout article/javascript`

</details>

---

### 3.13 Finaliser le tutoriel
Le développeur a maintenant terminé son tutoriel. Vérifiez les changements et committez-les avec le message `Guide JavaScript termine`

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git commit -am "Guide JavaScript termine"`

</details>

---

### 3.14 Compter les branches
Un nouveau dépôt Git est créé au chemin `/home/utilisateur/site-portfolio` pour héberger le site portfolio.

Comptez le nombre de branches disponibles dans ce dépôt, y compris la branche master.

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`cd /home/utilisateur/site-portfolio`

`git branch`

**Exemple de sortie :**
```
  feature/galerie
  feature/contact
  feature/apropos
  feature/projets
* master
```

**Réponse :** 5 branches

</details>

---

### 3.15 Origine d'une branche
En examinant l'historique des commits, essayez de deviner de quelle branche la branche `feature/contact` a été créée ?

Basculez vers la branche `feature/contact` puis utilisez la commande `git log --graph --decorate` pour voir l'historique des commits précédents ainsi que la branche sur laquelle ils ont été committés.

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`git checkout feature/contact`

`git log --graph --decorate`

</details>

---

### 3.16 Représentation graphique
En examinant l'historique des commits de toutes les branches, quelle est la meilleure représentation graphique des branches dans ce dépôt ?

Basculez vers chaque branche puis utilisez la commande `git log --graph --decorate` pour voir la branche précédente.

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`git checkout feature/projets`

`git log --graph --decorate`

</details>

---

### 3.17 État actuel du dépôt
Continuons là où nous nous sommes arrêtés. Le dépôt local du développeur devrait être disponible à `/home/utilisateur/projet-blog`

**Question :** Combien d'articles sont actuellement disponibles dans la branche master ?

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`cd /home/utilisateur/projet-blog`

`git checkout master`

`ls`

**Réponse :** 1 (seulement `article.txt`)

</details>

---

### 3.18 Nom de l'article
**Question :** Quel est le nom de l'article dans la branche master ?

<details>
<summary>Voir la réponse</summary>

<br>

**Réponse :** `article.txt`

</details>

---

### 3.19 Nombre de branches
**Question :** Combien de branches le dépôt a-t-il actuellement ?

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git branch`

**Exemple de sortie :**
```
* master
  article/javascript
```

**Réponse :** 2 branches

</details>

---

### 3.20 Analyser l'historique des branches
Le nouveau tutoriel que le développeur a écrit est dans la branche `article/javascript`. Il est temps de fusionner la branche et de l'amener dans la branche master.

Mais avant cela, regardez le log des branches master et `article/javascript` et identifiez combien de commits il y a eu dans le passé sur chaque branche.

<details>
<summary>Voir la solution</summary>

<br>

**Commandes :**

`git log`

`git checkout article/javascript`

`git log`

`git checkout master`

</details>

---

### 3.21 Comprendre l'historique
Le développeur a committé l'article initial dans la branche master, puis a créé une nouvelle branche pour le guide JavaScript, puis est retourné et a corrigé l'erreur dans l'article initial, et enfin est retourné et a terminé le guide JavaScript.

Ensuite, nous allons fusionner le nouveau tutoriel dans master pour avoir tous les contenus dans la branche master.

---

### 3.22 Fusionner les branches
Pendant que vous êtes dans la branche master, fusionnez la branche `article/javascript`. Si un message de commit vous est demandé, laissez-le par défaut et quittez l'éditeur.

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `git merge article/javascript`

Vérifiez `git log` maintenant et vous devriez voir le message de commit comme `Merge branch 'article/javascript'`

**Sortie attendue :**
```
Merge made by the 'recursive' strategy.
 javascript.txt | 25 +++++++++++++++++++
 1 file changed, 25 insertions(+)
 create mode 100644 javascript.txt
```

</details>

---

### 3.23 Vérifier l'historique après fusion
Vérifiez le log de la branche master et voyez combien de commits sont visibles maintenant.

<details>
<summary>Voir la commande</summary>

<br>

**Commande :** `git log --oneline`

</details>

---

### 3.24 Comprendre la fusion
Git a fusionné tous les commits que nous avons effectués dans la branche `article/javascript` vers la branche master. Mais comme nous avons effectué un commit supplémentaire sur master (correction de l'erreur), Git a créé un nouveau commit de fusion.

---

### 3.25 Vérification finale
Listez les fichiers dans la branche master et assurez-vous que les deux contenus sont visibles.

<details>
<summary>Voir la solution</summary>

<br>

**Commande :** `ls`

**Résultat attendu :**
```
article.txt
javascript.txt
```

</details>

---

**Fin du Travail Dirigé**
