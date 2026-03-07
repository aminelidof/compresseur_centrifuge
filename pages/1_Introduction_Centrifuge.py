import streamlit as st

# 1. Configuration de la page (Cohérence avec le reste du projet)
st.set_page_config(page_title="1. Introduction - Compresseurs Centrifuges", layout="wide")

# Style CSS pour le titre (Identique à votre style Axial)
st.markdown('<h1 style="color:#58A6FF;">🌀 1. Introduction et Constitution : Flux Radial</h1>', unsafe_allow_html=True)

# --- SECTION VISUELLE & DÉFINITION ---
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("""
    ### Définition
    Le **compresseur centrifuge** (ou radial) est une turbomachine thermique réceptrice où le fluide 
    pénètre axialement et ressort **perpendiculairement** à l'axe de rotation. 
    
    L'augmentation de pression est assurée par deux phénomènes conjoints :
    1. **La Force Centrifuge** : Créée par la rotation de l'impulseur qui projette le fluide vers l'extérieur.
    2. **La Diffusion** : Conversion de la vitesse élevée en pression dans les parties fixes.
    """)
    
    st.info("💡 **Le saviez-vous ?** Un seul étage centrifuge peut atteindre un taux de compression de **4 à 8**, là où l'axial plafonne à **1.2 - 1.5** par étage.")

with col2:
    # Illustration du principe centrifuge
    st.image("centrifugal-compressor.gif", 
             caption="Schéma éclaté : 1. Entrée (Eye), 2. Impulseur, 3. Diffuseur, 4. Volute",
             use_container_width=True)

st.markdown("---")

# --- COMPARAISON TECHNIQUE AXIAL VS CENTRIFUGE ---
st.subheader("📊 Comparaison Stratégique (M1 GM)")
st.write("Le choix entre axial et centrifuge dépend de l'application (Aéronautique vs Industrie) :")

data = {
    "Critère": ["Taux de compression / étage", "Débit massique", "Encombrement frontal", "Sensibilité à l'encrassement", "Domaine de prédilection"],
    "Compresseur Axial": ["Faible (≈ 1.2)", "Élevé (Grandes turbines)", "Petit", "Très sensible", "Turboréacteurs"],
    "Compresseur Centrifuge": ["Élevé (Jusqu'à 8.0)", "Moyen à faible", "Important (Largeur)", "Robuste", "Petites turbines, Turbo-chargeurs"]
}
st.table(data)

# --- CONSTITUTION DÉTAILLÉE ---
st.markdown("### 🛠️ Les organes constitutifs")
st.write("Un étage centrifuge complet se compose de trois éléments fixes ou mobiles :")



c1, c2, c3 = st.columns(3)

with c1:
    st.success("🛸 **L'Impulseur (Roue)**")
    st.write("""
    - **Rôle** : C'est le seul élément mobile. Il fournit l'énergie cinétique et de pression.
    - **Types** : Ouvert (sans flasque) ou fermé (avec flasque).
    - **Action** : Augmente le moment cinétique du fluide par variation de rayon ($r_1 \\rightarrow r_2$).
    """)

with c2:
    st.warning("🌀 **Le Diffuseur**")
    st.write("""
    - **Rôle** : Élément fixe entourant la roue.
    - **Fonction** : Ralentit le fluide sortant à grande vitesse de la roue pour transformer cette énergie en pression statique.
    - **Types** : Lisse (vaneless) ou à aubes (vaned).
    """)

with c3:
    st.error("🐚 **La Volute (Collecteur)**")
    st.write("""
    - **Rôle** : Conduit en forme de limaçon à section croissante.
    - **Fonction** : Collecte le fluide tout autour du diffuseur et le dirige vers la tubulure de refoulement.
    - **Effet** : Contribue également à une ultime diffusion du flux.
    """)

# --- LES TYPES DE PALES (CRUCIAL POUR L'INGÉNIEUR) ---
st.markdown("---")
st.subheader("📐 Géométrie des Pales de l'Impulseur")
st.write("L'angle de sortie de la pale ($\beta_2$) définit le comportement de la machine :")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.code("Pales vers l'arrière (Backward)")
    st.write("✅ **Rendement optimal**. Stable. Utilisé dans 90% des compresseurs industriels.")
    
with col_b:
    st.code("Pales Radiales (Radial)")
    st.write("⚖️ **Compromis**. Construction robuste, supporte des vitesses de rotation extrêmes.")

with col_c:
    st.code("Pales vers l'avant (Forward)")
    st.write("❌ **Instable**. Travail élevé mais rendement faible. Rarement utilisé en compression.")

# --- FOOTER ---
st.write("")
st.caption("Support de cours Master 1 GM - Dr FODIL - Analyse des Machines à Flux Radial")