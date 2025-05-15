# 🌊 Wa-Tor Projekt

Simulation écologique interactive inspirée du modèle **Wa-Tor**, mettant en scène l’interaction entre poissons, requins et chalutiers dans un environnement marin visualisé avec **Pygame**.

---

## 🐟 Présentation

Ce projet implémente une simulation dynamique basée sur le modèle **Wa-Tor**, dans lequel des entités marines évoluent sur une grille représentant un océan. Chaque entité suit des règles simples de déplacement, de reproduction, de prédation et de mortalité.

Une interface graphique avec **Pygame** permet une visualisation en temps réel des interactions, ainsi que des **statistiques affichées dans une barre latérale** et un **graphe dynamique** de l'évolution des populations.

Une présentation du projet est à disposition ici:
https://prezi.com/view/xknEvc59huHOhe05PPJE/

---

## 🖥️ Interface graphique

- Simulation en **temps réel** avec affichage des entités sous forme d’images (PNG).
- Couleur de fond bleue pour représenter l’eau.
- **Poissons** 🐟, **requins** 🦈 et **chalutiers** 🚢 visibles à l’écran.
- **Barre latérale** :
  - Compteur de poissons et requins.
  - Graphe des populations (nombre de poissons/requins au fil du temps).

---

## 📁 Structure du projet

```
wator_projekt/
├── assets/                  # Images PNG : fish.png, shark.png, trawler.png
├── models/
│   ├── fish.py             # Classe Fish
│   ├── shark.py            # Classe Shark
│   ├── trawler.py          # Classe Trawler (facultatif)
│   └── sea.py              # Grille de la mer et logique de simulation
├── pygame_display.py       # Affichage graphique avec Pygame
├── main.py                 # Point d’entrée de la simulation
├── README.md               # Ce fichier
└── LICENSE                 # Licence MIT
```

---

## 🚀 Installation et exécution

### Prérequis

- Python 3.x
- Pygame

### Installation

```bash
git clone https://github.com/RemiVander/wator_projekt.git
cd wator_projekt
pip install pygame
python3 main.py
```

---

## 🎮 Contrôles

- `P` : Met en pause / relance la simulation
- `R` : **Réinitialise** la simulation avec de nouvelles entités aléatoires

---

## ⚙️ Paramètres configurables (`main.py`)

- `num_fish` : Nombre initial de poissons (ex. `num_fish=30`)
- `num_sharks` : Nombre initial de requins (ex. `num_sharks=5`)
- `width`, `height` : Dimensions de la mer
- `CELL_SIZE` : Taille d'une cellule en pixels
- `FPS` : Vitesse d'exécution de la simulation

---

## 🧠 Fonctionnalités principales

- **Déplacement** : vers une case vide adjacente
- **Reproduction** : après un certain intervalle (`reproduce_interval`)
- **Prédation** : les requins mangent les poissons
- **Énergie** : les requins perdent de l’énergie à chaque tour, et en regagnent en mangeant
- **Vieillissement** : mort des entités à `max_age`
- **Graphique dynamique** : évolution des populations dans le temps

---

## 📊 Statistiques et visualisation

- Affichage en temps réel du nombre de poissons et requins
- Graphe de l’évolution des populations dans la barre latérale
- Historique glissant basé sur les derniers `n` tours (`max_history_length`)

---

## 📜 Licence

Ce projet est sous licence **MIT**.  
Voir le fichier [LICENSE](LICENSE) pour plus d'informations.

---

## 🤝 Contribuer

Les contributions sont les bienvenues !  
Forkez le projet, créez une branche, et soumettez une **pull request**.

---

> 📎 GitHub : [https://github.com/RemiVander/wator_projekt](https://github.com/RemiVander/wator_projekt)
