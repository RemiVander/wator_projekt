# 🌊 Wa-Tor Projekt

Simulation écologique inspirée du modèle Wa-Tor, mettant en scène l'interaction entre poissons et requins dans un environnement marin.

## 🐟 Présentation

Ce projet implémente une simulation basée sur le modèle Wa-Tor, où des poissons et des requins évoluent sur une grille représentant un océan. Les entités suivent des règles simples de déplacement, de reproduction et de prédation, offrant une visualisation dynamique des interactions écologiques.

## 📁 Structure du projet

- `main.py` : Point d'entrée de la simulation.
- `models/`
  - `fish.py` : Définit la classe `Fish` avec ses comportements.
  - `shark.py` : Définit la classe `Shark` avec ses comportements.
  - `sea.py` : Gère la grille océanique et les interactions entre entités.
- `README.md` : Ce fichier de documentation.
- `LICENSE` : Licence MIT.

## 🚀 Installation et exécution

### Prérequis

- Python 3

### Installation

```bash
git clone https://github.com/RemiVander/wator_projekt.git
cd wator_projekt
python3 main.py
```


La simulation s'affichera dans le terminal, avec des emojis représentant les entités :

    🌊 : Espace vide

    🐟 : Poisson

    🦈 : Requin


## ⚙️ Paramètres configurables

Les paramètres suivants peuvent être ajustés dans le fichier `main.py` :

- `num_fish` : Nombre initial de poissons dans la mer (ex. `num_fish=20`)
- `num_sharks` : Nombre initial de requins (ex. `num_sharks=2`)
- `width` et `height` : Dimensions de la mer (`Sea(width=50, height=30)`)
- `reproduce_interval` : Intervalle fixe de reproduction des entités (défini en dur dans la classe `Fish` ou `Shark`)
- `max_age` : Âge maximum des entités avant leur disparition
- `energy` (requins uniquement) : Niveau d'énergie consommé à chaque tour et regagné en mangeant un poisson


## 🧠 Fonctionnalités

- **Déplacement** : Les entités se déplacent vers une case vide adjacente.
- **Reproduction** : Les entités se reproduisent lorsqu'elles atteignent un âge multiple de leur `reproduce_interval`.
- **Prédation** : Les requins mangent les poissons et regagnent de l'énergie.
- **Vieillissement** : Toute entité meurt en atteignant son `max_age`.


## 📜 Licence

Ce projet est distribué sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.


## 🤝 Contribuer

Les contributions sont les bienvenues !  
Vous pouvez forker le projet, créer une branche, et proposer une pull request via GitHub.

---

> GitHub : [https://github.com/RemiVander/wator_projekt](https://github.com/RemiVander/wator_projekt)
