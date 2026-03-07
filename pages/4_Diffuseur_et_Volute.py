import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="4. Diffuseur & Volute - CentriFlow", layout="wide")

# --- 2. STYLE ÉPURÉ (SÉCURISÉ POUR LE DOM) ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    
    /* On cible le texte sans casser la structure des widgets */
    .stMarkdown p, .stMarkdown li, label, .stText { 
        color: #000000 !important; 
    }
    
    h1, h2, h3 { 
        color: #1F497D !important; 
        font-weight: 700 !important;
        border-bottom: 1px solid #DEE2E6;
        padding-bottom: 10px;
    }

    /* Style pour les encadrés utilisant les composants natifs */
    div[data-testid="stVerticalBlock"] > div[style*="border"] {
        border: 1px solid #DEE2E6 !important;
        background-color: #F8F9FA !important;
        padding: 20px !important;
        border-radius: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🐚 4. Organes Statiques : Diffuseur et Volute")

st.write("""
Une fois que le fluide quitte l'impulseur, il possède une énergie cinétique massive (vitesse absolue $C_2$). 
L'objectif des composants statiques (fixes) est de transformer cette vitesse en **pression statique** par un ralentissement contrôlé.
""")

# --- SECTION 1 : LE DIFFUSEUR ---
st.header("A. Le Diffuseur : Cœur de la Conversion")

# Sélecteur placé avec une clé unique pour stabiliser le rendu
diff_tech = st.radio(
    "Technologie de diffusion :",
    ["Diffuseur Lisse (Vaneless)", "Diffuseur à Aubes (Vaned)"],
    key="nav_diff_tech_final_fix",
    horizontal=True
)

st.divider()

col_info, col_img = st.columns([1, 1.2])

with col_info:
    # Utilisation d'un container fixe pour éviter les erreurs de "removeChild"
    info_zone = st.container(border=True)
    
    if diff_tech == "Diffuseur Lisse (Vaneless)":
        info_zone.subheader("🌀 Diffuseur Lisse")
        info_zone.write("**Principe Physique :** Basé sur la conservation du moment cinétique.")
        info_zone.latex(r"r \times C_w = \text{constante}")
        info_zone.write("Le fluide suit une trajectoire en spirale logarithmique.")
        info_zone.write("✅ **Grande Stabilité** : Très large plage de fonctionnement.")
        info_zone.write("✅ **Robustesse** : Simple à fabriquer.")
        info_zone.write("❌ **Encombrement** : Nécessite un grand diamètre radial.")
    else:
        info_zone.subheader("📐 Diffuseur à Aubes (Vaned)")
        info_zone.write("**Principe Physique :** Utilise des canaux divergents physiques.")
        info_zone.write("✅ **Haute Efficacité** : Rendement maximal au point de design.")
        info_zone.write("✅ **Compacité** : Plus compact qu'un diffuseur lisse.")
        info_zone.write("❌ **Instabilité** : Risque de **Pompage (Surge)** élevé hors design.")

with col_img:
    st.info("💡 **Équation de Continuité Radiale :**")
    st.latex(r"C_3 = C_2 \cdot \left( \frac{r_2}{r_3} \right) \cdot \left( \frac{b_2}{b_3} \right)")
    
    st.write("Le choix résulte d'un compromis entre rendement et plage de stabilité.")

st.divider()

# --- SECTION 2 : LA VOLUTE ---
st.header("B. La Volute (Le Limaçon)")

c1, c2 = st.columns([1.2, 1])

with c1:
    st.write("""
    La **volute** collecte le flux sortant du diffuseur sur 360° pour le diriger vers la sortie.
    Sa section transversale $A$ croît proportionnellement à l'angle $\theta$.
    """)
    st.latex(r"A(\theta) = A_{sortie} \cdot \frac{\theta}{360^\circ}")

with c2:
    
    st.warning("⚠️ **Poussée Radiale** : Hors design, la pression asymétrique peut endommager les paliers.")

# --- SECTION 3 : RÉCAPITULATIF ---
st.header("📊 Synthèse des Pertes Statiques")
st.table({
    "Organe": ["Diffuseur Lisse", "Diffuseur à Aubes", "Volute"],
    "Type de Perte": ["Friction", "Décollement", "Expansion"],
    "Objectif": ["Stabilité", "Performance", "Collecte"]
})

st.divider()
st.caption("CentriFlow Pro v1.0 | M1 GM | © 2026 Univ. Maghnia")