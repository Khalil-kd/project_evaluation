# Comparaison des donnees McDonald's vs Burger King

## Description du projet

Cette application web interactive permet de comparer les informations nutritionnelles de produits issus de McDonald's et Burger King.

Elle a pour objectifs :
- Le chargement et la visualisation des donnees issues de fichiers CSV.
- La manipulation des donnees avec DuckDB.
- La construction d'interfaces interactives avec Streamlit.
- L'affichage de 4 indicateurs cles (KPI) a travers des visualisations interactives.
- L'utilisation de filtres dynamiques pour affiner les resultats par date ou produit.

Ce projet vise a evaluer nos competences en manipulation de donnees, SQL, visualisation et collaboration avec Git.

---

## Fonctionnalites principales

- Chargement automatique des donnees McDonald's et Burger King (fichiers CSV).
- Visualisation des structures de donnees.
- Analyse exploratoire des valeurs (calories, categories, etc.).
- Repartition des produits par restaurant, par date, par type.
- Filtres dynamiques sur les donnees.
- Affichage de quatre visualisations interconnectees representant les indicateurs cles.

---

## Architecture du projet
<img width="880" height="438" alt="image" src="https://github.com/user-attachments/assets/231e02de-0d7f-477f-bf20-b9be9a427cfb" />


## 👥 Répartition des rôles

- Bader Drissi	 : 📊 Data Analyst & Visualisation	Chargée des explorations graphiques, choix des indicateurs clés (KPI), et dashboard Streamlit
- Wael Ben Yahmed	 : 🧠 Responsable base de données & intégration DuckDB	Mise en place des requêtes SQL, chargement des données et structure des tables
- Khalil Kadri  : 🛠️ Développeur Streamlit & Gestion du projet Git	Architecture de l'application, gestion du dépôt Git, fusions de branches et app UI


## 🧰 Technologies


## 🚀 Objectifs

- Importer et interroger dynamiquement des données CSV via **DuckDB**
- Visualiser les **KPI essentiels** d’un fichier de ventes
- Filtrer les résultats par **date**, **région**, et **produit**
- Fournir une **interface web intuitive** avec **Streamlit**

---


- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [DuckDB](https://duckdb.org/)
- [Plotly](https://plotly.com/python/)

---

## 🏗️ Architecture du projet

project_evaluation/
├── data/
│ └── [fichiers .csv importés]
├── scripts/
│ └── db_loader.py
├── app.py
├── requirements.txt
└── README.md


## 🧪 Fonctionnalités principales
✅ Importation de fichiers CSV
✅ Requêtes SQL avec DuckDB
✅ Filtres dynamiques : date, produit, région
✅ 4 indicateurs clés :

💰 Total des ventes

🧾 Nombre de transactions

🏆 Produit le plus vendu

🌍 Région la plus rentable

✅ 4 graphiques :

Barres, camembert, ligne, boxplot

## 🧱 Difficultés rencontrées & Solutions
Problème rencontré	Solution apportée
Erreurs d'import duckdb malgré installation	Activation correcte de l'environnement virtuel avant lancement (venv\Scripts\activate)
Structure des fichiers non détectée par Streamlit	Respect strict de l'arborescence scripts/, et import relatifs
Erreurs lors de la jointure des tables CSV (UNION ALL)	Harmonisation des noms de colonnes avec alias (AS) pour chaque table
Mauvais affichage des graphiques	Passage de matplotlib à Plotly pour une meilleure interaction
Problème de chemin relatif dans os.path.join()	Vérification que les fichiers .csv sont bien dans un dossier data/





📌 Remarques
Ce projet peut être facilement adapté à tout jeu de données de ventes.

L’utilisation de DuckDB permet une performance optimale sur fichiers CSV volumineux.




