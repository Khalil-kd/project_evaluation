# 📊 Comparateur de Ventes – McDonald's vs Burger King

Projet de création d'une application interactive avec **Streamlit** et **DuckDB**, permettant d'importer un fichier CSV, analyser les ventes, filtrer dynamiquement, et visualiser 4 indicateurs clés de performance (KPI).

---

👥 Répartition des rôles
Membre de l'équipe	Rôle principal	Détails des contributions
Bader Drissi	📊 Data Analyst & Visualisation	Chargée des explorations graphiques, choix des indicateurs clés (KPI), et dashboard Streamlit
Wael Ben Yahmed	🧠 Responsable base de données & intégration DuckDB	Mise en place des requêtes SQL, chargement des données et structure des tables
Khalil Kadri 🛠️ Développeur Streamlit & Gestion du projet Git	Architecture de l'application, gestion du dépôt Git, fusions de branches et app UI


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


##🧪 Fonctionnalités principales
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

##🧱 Difficultés rencontrées & Solutions
Problème rencontré	Solution apportée
Erreurs d'import duckdb malgré installation	Activation correcte de l'environnement virtuel avant lancement (venv\Scripts\activate)
Structure des fichiers non détectée par Streamlit	Respect strict de l'arborescence scripts/, et import relatifs
Erreurs lors de la jointure des tables CSV (UNION ALL)	Harmonisation des noms de colonnes avec alias (AS) pour chaque table
Mauvais affichage des graphiques	Passage de matplotlib à Plotly pour une meilleure interaction
Problème de chemin relatif dans os.path.join()	Vérification que les fichiers .csv sont bien dans un dossier data/





📌 Remarques
Ce projet peut être facilement adapté à tout jeu de données de ventes.

L’utilisation de DuckDB permet une performance optimale sur fichiers CSV volumineux.




