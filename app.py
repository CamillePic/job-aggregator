import streamlit as st
import scraper  # Assurez-vous d'importer le fichier scraper.py

# Scrape les offres
jobs = scraper.scrape_indeed()

# Affichage sous forme de cartes
for job in jobs:
    with st.expander(f"{job['title']} - {job['company']}"):
        st.write(f"**Location**: {job['location']}")
        st.button("Voir l'offre", help="Clique pour voir l'annonce complète")
