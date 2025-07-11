import pandas as pd
import duckdb
import streamlit as st
from scripts.db_loader import load_data as load_combined_data

# Titre général
st.set_page_config(page_title="Comparaison BK vs MCD", layout="wide")
st.title("📊 Comparaison des données McDonald's vs Burger King")

# Chargement des données
con, combined_df = load_combined_data()

mcd_df = con.sql("SELECT * FROM mcd").df()
bk_df = con.sql("SELECT * FROM bk").df()

# Menu de navigation
menu = st.sidebar.selectbox(
    "Navigation",
    ["Présentation du projet", "Téléversement CSV", "Visualisation des données", "Analyse exploratoire", "Nettoyage des données"]
)

# === Upload de fichier CSV ===
st.sidebar.markdown("### 📁 Upload de vos données")
uploaded_file = st.sidebar.file_uploader("Chargez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    import pandas as pd
    import duckdb

    st.success("✅ Fichier chargé avec succès")

    # Lire le fichier
    df_uploaded = pd.read_csv(uploaded_file)

    # Afficher un aperçu
    st.markdown("### Aperçu du fichier chargé :")
    st.dataframe(df_uploaded.head())

    # Charger dans DuckDB
    con_upload = duckdb.connect(database=":memory:")
    con_upload.register("df_uploaded", df_uploaded)
    con_upload.execute("CREATE TABLE sales AS SELECT * FROM df_uploaded")

    # Vérification
    st.markdown("### Colonnes détectées :")
    st.dataframe(con_upload.sql("PRAGMA table_info('sales')").df())

    st.markdown("### Exemple de requête : Total par produit")
    try:
        result = con_upload.sql("SELECT produit, SUM(valeur) as total FROM sales GROUP BY produit").df()
        st.dataframe(result)
    except:
        st.warning("⚠️ Impossible d’agréger par colonne 'produit' — vérifier les noms de colonnes.")

    st.markdown("## 🎛️ Filtres dynamiques")

    # Vérifier les colonnes disponibles
    colonnes = df_uploaded.columns

    # Filtres proposés selon colonnes détectées
    date_col = st.selectbox("Sélectionnez une colonne de date :", colonnes)
    produit_col = st.selectbox("Sélectionnez une colonne produit :", colonnes)
    region_col = st.selectbox("Sélectionnez une colonne région :", colonnes)

    # Convertir la colonne date si possible
    try:
        df_uploaded[date_col] = pd.to_datetime(df_uploaded[date_col])
    except Exception as e:
        st.warning(f"⚠️ Erreur de parsing des dates : {e}")

    # Sélecteurs de filtres
    dates = st.date_input("Filtrer par date", [])
    produits = st.multiselect("Filtrer par produit", df_uploaded[produit_col].unique())
    regions = st.multiselect("Filtrer par région", df_uploaded[region_col].unique())

    # Appliquer les filtres
    filtered_df = df_uploaded.copy()

    if dates:
        if len(dates) == 2:
            filtered_df = filtered_df[
                (filtered_df[date_col] >= pd.to_datetime(dates[0])) &
                (filtered_df[date_col] <= pd.to_datetime(dates[1]))
            ]

    if produits:
        filtered_df = filtered_df[filtered_df[produit_col].isin(produits)]

    if regions:
        filtered_df = filtered_df[filtered_df[region_col].isin(regions)]

    st.markdown("### 🔎 Données filtrées")
    st.dataframe(filtered_df.head())

    st.markdown("## 📈 Indicateurs clés (KPI)")

    if not filtered_df.empty:
        # KPI 1 : Total des ventes
        total_ventes = filtered_df['sales'].sum()
        st.metric("💰 Total des ventes", f"{total_ventes:,.0f} €")

        # KPI 2 : Nombre total de transactions
        nb_transactions = len(filtered_df)
        st.metric("🧾 Nombre de transactions", nb_transactions)

        # KPI 3 : Produit le plus vendu
        top_produit = (
            filtered_df.groupby(produit_col)['sales']
            .sum()
            .idxmax()
        )
        st.metric("🏆 Produit le plus vendu", top_produit)

        # KPI 4 : Région avec le plus de ventes
        top_region = (
            filtered_df.groupby(region_col)['sales']
            .sum()
            .idxmax()
        )
        st.metric("🌍 Région avec le plus de ventes", top_region)

        # Visualisation 1 : Ventes par produit
        st.subheader("📊 Ventes par produit")
        fig1 = px.bar(
            filtered_df.groupby(produit_col)['sales'].sum().reset_index(),
            x=produit_col, y='sales', title='Ventes par produit'
        )
        st.plotly_chart(fig1)

        # Visualisation 2 : Ventes par région
        st.subheader("🗺️ Ventes par région")
        fig2 = px.pie(
            filtered_df.groupby(region_col)['sales'].sum().reset_index(),
            names=region_col, values='sales', title='Répartition des ventes par région'
        )
        st.plotly_chart(fig2)

        # Visualisation 3 : Ventes dans le temps
        st.subheader("📅 Ventes dans le temps")
        fig3 = px.line(
            filtered_df.groupby(date_col)['sales'].sum().reset_index(),
            x=date_col, y='sales', title='Évolution des ventes dans le temps'
        )
        st.plotly_chart(fig3)

        # Visualisation 4 : Boxplot des ventes par région
        st.subheader("📦 Distribution des ventes par région")
        fig4 = px.box(
            filtered_df, x=region_col, y='sales',
            title='Distribution des ventes'
        )
        st.plotly_chart(fig4)
    else:
        st.warning("Aucune donnée après filtrage.")


# === 1. Présentation ===
if menu == "Présentation du projet":
    st.subheader("📘 Contexte")
    st.markdown("""
    Ce projet a pour objectif de comparer les données nutritionnelles entre les produits de **McDonald's** et **Burger King**.
    
    Nous allons :
    - Charger les données
    - Visualiser les premières informations
    - Réaliser une analyse exploratoire (EDA)
    - Nettoyer les données en vue d'une future exploitation
    """)

# === 2. Visualisation des données ===
elif menu == "Visualisation des données":
    st.subheader("👀 Aperçu des données brutes")

    st.markdown("### 🍔 McDonald's")
    st.dataframe(mcd_df.head(10))

    st.markdown("### 🍟 Burger King")
    st.dataframe(bk_df.head(10))

# === 3. Analyse exploratoire (placeholder) ===
elif menu == "Analyse exploratoire":
    import plotly.express as px

    st.subheader("📈 Analyse exploratoire des données")

    # 1. Infos générales
    st.markdown("### 📋 Structure des tables")
    st.markdown("#### McDonald's")
    st.dataframe(con.sql("PRAGMA table_info('mcd')").df())

    st.markdown("#### Burger King")
    st.dataframe(con.sql("PRAGMA table_info('bk')").df())

    mcd_count = con.sql("SELECT COUNT(*) FROM mcd").fetchone()[0]
    bk_count = con.sql("SELECT COUNT(*) FROM bk").fetchone()[0]
    st.markdown(f"- **Nombre de lignes McDonald's :** {mcd_count}")
    st.markdown(f"- **Nombre de lignes Burger King :** {bk_count}")

    # 2. Fusion des données avec harmonisation
    combined_query = """
        SELECT 
            table_name, 
            heading, 
            item, 
            CAST(Date AS VARCHAR) AS date_str, 
            Value AS calories, 
            'mcd' AS restaurant 
        FROM mcd
        UNION ALL
        SELECT 
            item AS table_name, 
            'N/A' AS heading, 
            item, 
            CAST(Attribute AS VARCHAR) AS date_str, 
            Value AS calories, 
            'bk' AS restaurant 
        FROM bk
    """
    combined_df = con.sql(combined_query).df()

    # 3. Graphique : nombre de produits par restaurant
    st.markdown("### 🍽️ Répartition des produits")

    count_data = combined_df['restaurant'].value_counts().reset_index()
    count_data.columns = ['restaurant', 'nombre_produits']  # ✅ noms explicites

    count_fig = px.bar(
        count_data,
        x='restaurant',
        y='nombre_produits',
        color='restaurant',
        title='Nombre de produits par restaurant',
        labels={
            'restaurant': 'Restaurant',
            'nombre_produits': 'Nombre de produits'
        }
    )

    st.plotly_chart(count_fig, use_container_width=True)

   

    # 4. Boxplot : distribution des calories
    st.markdown("### 🔥 Distribution des calories")
    box_fig = px.box(
        combined_df,
        x="restaurant",
        y="calories",
        color="restaurant",
        title="Distribution des calories par restaurant"
    )
    st.plotly_chart(box_fig, use_container_width=True)

    # 5. Moyenne des calories
    st.markdown("### ⚖️ Calories moyennes par restaurant")
    avg = combined_df.groupby("restaurant")["calories"].mean().reset_index()
    avg.columns = ["restaurant", "calories moyennes"]
    st.dataframe(avg)


    # 4. Distribution des calories
    st.markdown("### 🔥 Distribution des calories")
    import seaborn as sns
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    sns.boxplot(data=combined_df, x="restaurant", y="calories", ax=ax)
    st.pyplot(fig)

    # 5. Moyenne des calories
    st.markdown("### ⚖️ Calories moyennes par restaurant")
    avg = combined_df.groupby("restaurant")["calories"].mean().reset_index()
    avg.columns = ["restaurant", "calories moyennes"]
    st.dataframe(avg)

elif menu == "Téléversement CSV":
    st.subheader("📂 Téléversement d'un fichier CSV")

    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

    if uploaded_file is not None:
        try:
            # Lecture du fichier
            df = pd.read_csv(uploaded_file)

            # Connexion à DuckDB (en mémoire pour l'instant)
            con = duckdb.connect(database=":memory:")

            # Création d'une table temporaire
            con.register("uploaded_df", df)

            # Aperçu
            st.success("Fichier chargé avec succès ✅")
            st.write("Aperçu des données :")
            st.dataframe(df.head())

            # Option : stats simples
            st.write("Résumé statistique :")
            st.dataframe(df.describe(include='all'))

        except Exception as e:
            st.error(f"Erreur lors du traitement : {e}")
    else:
        st.info("Veuillez téléverser un fichier CSV pour continuer.")

elif menu == "Indicateurs clés":
    st.subheader("📊 Indicateurs clés de performance")

    import plotly.express as px

    # Charger les données combinées
    combined_query = """
        SELECT table_name, heading, item, 
               TRY_CAST(Date AS VARCHAR) AS Date, 
               TRY_CAST(Value AS DOUBLE) AS calories,
               'mcd' AS restaurant
        FROM mcd
        UNION ALL
        SELECT item AS table_name, Attribute AS heading, item, 
               TRY_CAST(Attribute AS VARCHAR) AS Date, 
               TRY_CAST(Value AS DOUBLE) AS calories,
               'bk' AS restaurant
        FROM bk
    """
    combined_df = con.sql(combined_query).df()

    # 🧮 KPI 1 : Nombre total de produits par restaurant
    st.markdown("### 🍽️ Nombre de produits par restaurant")
    count_df = combined_df['restaurant'].value_counts().reset_index()
    count_df.columns = ['restaurant', 'nombre de produits']
    fig1 = px.bar(count_df, x='restaurant', y='nombre de produits', color='restaurant', title="Nombre de produits")
    st.plotly_chart(fig1, use_container_width=True)

    # 🔥 KPI 2 : Moyenne des calories par restaurant
    st.markdown("### 🔥 Calories moyennes par restaurant")
    avg_df = combined_df.groupby('restaurant')['calories'].mean().reset_index()
    fig2 = px.bar(avg_df, x='restaurant', y='calories', color='restaurant', title="Calories moyennes")
    st.plotly_chart(fig2, use_container_width=True)

    # 🍔 KPI 3 : Produit le plus calorique par restaurant
    st.markdown("### 🍔 Produit le plus calorique par restaurant")
    max_calories_df = combined_df.loc[combined_df.groupby('restaurant')['calories'].idxmax()]
    st.dataframe(max_calories_df[['restaurant', 'item', 'calories']])

    # 📅 KPI 4 : Répartition temporelle si disponible
    st.markdown("### 📅 Répartition des produits par date")
    if "Date" in combined_df.columns:
        try:
            combined_df['Date'] = pd.to_datetime(combined_df['Date'], errors='coerce')
            temporal_df = combined_df.dropna(subset=['Date'])
            temporal_df = temporal_df.groupby([temporal_df['Date'].dt.to_period('M').astype(str), 'restaurant']).size().reset_index(name='nombre')
            fig4 = px.line(temporal_df, x='Date', y='nombre', color='restaurant', title="Produits au fil du temps")
            st.plotly_chart(fig4, use_container_width=True)
        except Exception as e:
            st.warning(f"Problème lors du parsing des dates : {e}")
    else:
        st.info("Aucune colonne Date disponible pour une visualisation temporelle.")



# === 4. Nettoyage des données (placeholder) ===
# === 4. Nettoyage des données ===
elif menu == "Nettoyage des données":
    st.subheader("🧹 Nettoyage des données")

    # 1. Vérification des valeurs manquantes
    st.markdown("### 🔎 Valeurs manquantes")
    mcd_nulls = mcd_df.isnull().sum()
    bk_nulls = bk_df.isnull().sum()

    st.markdown("#### McDonald's")
    st.dataframe(mcd_nulls[mcd_nulls > 0])

    st.markdown("#### Burger King")
    st.dataframe(bk_nulls[bk_nulls > 0])

    # 2. Vérification des doublons
    st.markdown("### 📋 Doublons")
    mcd_duplicates = mcd_df.duplicated().sum()
    bk_duplicates = bk_df.duplicated().sum()

    st.write(f"🔁 McDonald's contient **{mcd_duplicates}** doublons.")
    st.write(f"🔁 Burger King contient **{bk_duplicates}** doublons.")

    # 3. Aperçu des types de données
    st.markdown("### 🔧 Types de données")
    st.markdown("#### McDonald's")
    st.dataframe(mcd_df.dtypes)

    st.markdown("#### Burger King")
    st.dataframe(bk_df.dtypes)

    # 4. Nettoyage de base (à faire dans une branche séparée plus tard)
    st.info("👉 Les opérations de nettoyage concrètes (remplissage NA, cast types, etc.) seront réalisées dans la branche `data_cleaning`.")



