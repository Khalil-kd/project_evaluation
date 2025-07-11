# Comparaison des donnees McDonald's vs Burger King


[![Accéder à l'application](https://img.shields.io/badge/🚀%20Lancer%20l'application%20Streamlit-brightgreen?style=for-the-badge)]([https://ton-lien-streamlit.streamlit.app](https://projectevaluation-ek86xkdcoxlomubrm9ybk9.streamlit.app/))

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

## Repartition des roles

- **Bader Drissi** : Analyse de donnees, visualisations graphiques, indicateurs KPI et layout Streamlit.
- **Wael Ben Yahmed** : Integration des donnees dans DuckDB, requetes SQL et preparation des tables.
- **Khalil Kadri** : Developpement de l'application Streamlit, architecture du projet, integration des composants et gestion Git.

---

## Difficultes rencontrees et solutions apportees

| Probleme                              | Solution apportee                                               |
|---------------------------------------|------------------------------------------------------------------|
| Incompatibilite des schemas entre CSV | Utilisation de `read_csv_auto` de DuckDB et harmonisation manuelle |
| Erreurs de type sur les dates         | Conversion explicite des colonnes avec `CAST` ou `pd.to_datetime()` |
| Mauvais encodage dans le terminal     | Sauvegarde des fichiers en UTF-8 et nettoyage des caracteres    |
| Visualisations peu lisibles           | Passage a Plotly pour une meilleure lisibilite et interactivite |

---

## Technologies utilisees

- Python 3.10+
- Streamlit
- DuckDB
- Pandas
- Plotly






