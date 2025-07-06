import streamlit as st
from scripts.db_loader import load_data

# Charger les données
con = load_data()

st.title("Analyse des Données : MCD vs BK")

# Afficher les 5 premières lignes de chaque table
st.subheader("Aperçu de MCD")
df_mcd = con.sql("SELECT * FROM mcd LIMIT 5").df()
st.dataframe(df_mcd)

st.subheader("Aperçu de BK")
df_bk = con.sql("SELECT * FROM bk LIMIT 5").df()
st.dataframe(df_bk)
