# Projet_jeu_labyrinthe_PYTHON
Ce projet crée un jeu de labyrinthe graphique en Python avec la bibliothèque Turtle. Le joueur navigue à travers le labyrinthe en utilisant une interface graphique, en partant de l'entrée et en évitant les murs pour atteindre la sortie. Le labyrinthe est chargé depuis un fichier texte, permettant de varier les configurations du jeu.

projet consiste à la création d'un jeu de labyrinthe interactif en utilisant la bibliothèque Python Turtle. Le but du jeu est de naviguer dans un labyrinthe en utilisant des commandes clavier. Le labyrinthe est affiché à la fois dans le terminal et graphiquement avec Turtle.

Le jeu permet de charger un labyrinthe depuis un fichier `.laby`, de l'afficher sous forme textuelle et graphique, et de permettre à un utilisateur de se déplacer dans le labyrinthe pour en trouver la sortie.

## Fonctionnalités

- **Affichage du labyrinthe** : Chargement et affichage d'un labyrinthe depuis un fichier texte, avec une représentation à la fois textuelle et graphique.
- **Navigation du joueur** : Le joueur peut se déplacer dans le labyrinthe en utilisant les touches directionnelles.
- **Dynamique de jeu** : L'entrée et la sortie du labyrinthe sont définies et affichées.
- **Affichage terminal** : Le labyrinthe est aussi affiché sous forme textuelle dans le terminal.

**Installer Python et les dépendances** :
    Ce projet utilise Python avec la bibliothèque `turtle` (intégrée par défaut dans Python).

## Format du fichier `.laby`
Le fichier `.laby` doit suivre une structure spécifique, où chaque caractère représente un élément du labyrinthe :
- `#` pour un mur
- `.` pour un passage
- `x` pour l'entrée
- `X` pour la sortie

Exemple de fichier `.laby` : laby1.laby 