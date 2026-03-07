import streamlit as st

# --- 1. CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="CentriFlow Pro | M1-GM",
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THÈME CLAIR "HAUTE LISIBILITÉ" (CSS INVERSÉ) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    /* Fond principal blanc et texte noir */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] { 
        font-family: 'Inter', sans-serif; 
        background-color: #FFFFFF !important; 
        color: #000000 !important;
    }

    /* Barre latérale gris très clair */
    [data-testid="stSidebar"] { 
        background-color: #F8F9FA !important; 
        border-right: 1px solid #DEE2E6 !important; 
    }

    /* --- LISIBILITÉ DU MENU LATÉRAL --- */
    /* Titres de catégories en bleu foncé */
    [data-testid="stSidebarNavSeparator"] + div span, 
    [data-testid="stSidebarNav"] div div {
        color: #1F497D !important; 
        font-weight: 800 !important;
        text-transform: uppercase;
    }

    /* Liens des pages en noir */
    [data-testid="stSidebarNavLink"] span {
        color: #000000 !important; 
        font-weight: 500 !important;
    }

    /* Page active dans le menu */
    [data-testid="stSidebarNavLink"][aria-current="page"] {
        background-color: #E9ECEF !important;
        border-left: 5px solid #1F497D !important;
    }

    /* --- CONTENU PRINCIPAL --- */
    /* Tous les paragraphes et listes en noir profond */
    [data-testid="stMarkdownContainer"] p, 
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stMarkdownContainer"] span {
        color: #000000 !important; 
        font-size: 1.05rem !important;
        line-height: 1.6 !important;
    }

    /* Titres en bleu industriel pour le contraste */
    h1, h2, h3 { 
        color: #1F497D !important; 
        font-weight: 700 !important;
    }

    /* Carte Utilisateur en bas de sidebar */
    .id-card { 
        background-color: #FFFFFF; 
        padding: 15px; 
        border-radius: 10px; 
        border: 1px solid #DEE2E6; 
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .id-card p, .id-card b {
        color: #000000 !important;
    }

    /* Footer discret */
    .footer { 
        position: fixed; 
        left: 0; 
        bottom: 0; 
        width: 100%; 
        background: #F8F9FA; 
        color: #6C757D; 
        text-align: center; 
        padding: 8px; 
        font-size: 12px; 
        border-top: 1px solid #DEE2E6; 
        z-index: 99; 
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. INFOS D'IDENTIFICATION (SIDEBAR) ---
with st.sidebar:
    st.markdown("### 👤 Utilisateur")
    st.markdown(f"""
    <div class="id-card">
        <p style="margin:0; color:#1F497D; font-size:11px; font-weight:bold; text-transform:uppercase;">Application</p>
        <p style="margin:0 0 5px 0; font-size:18px; font-weight:800; color:#000000;">CentriFlow <span style="color:#1F497D;">Pro</span></p>
        <p style="margin:0; font-size:14px;"><b>👨‍🏫 Dr. FODIL M.E.A.</b></p>
        <p style="margin:0; font-size:13px; color:#495057;">Master 1 Génie Mécanique</p>
        <p style="margin:0; font-size:13px; color:#495057;">🏫 Université de Maghnia</p>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

# --- 4. DÉFINITION DES PAGES ---
intro = st.Page("pages/1_Introduction_Centrifuge.py", title="Concept & Bases", icon="📘")
thermo = st.Page("pages/2_Thermodynamique_Centrifuge.py", title="Cycles & Énergie", icon="⚡")
cine = st.Page("pages/3_Cinematique_et_Impulseur.py", title="Cinématique (Roue)", icon="📐")
diff = st.Page("pages/4_Diffuseur_et_Volute.py", title="Diffuseur & Volute", icon="🐚")
exo = st.Page("pages/5_Atelier_Centrifuge.py", title="Atelier Pratique", icon="🛠️")
simu = st.Page("pages/6_Simulateur_Expert.py", title="Simulateur de Design", icon="🚀")

# --- 5. NAVIGATION (MODIFIÉE ICI) ---
pg = st.navigation({
    "📖 FORMATION THÉORIQUE": [intro, thermo],
    "⚙️ ANALYSE RADIALE": [cine, diff],
    "🏁 ÉVALUATION": [exo, simu]  # <--- AJOUTEZ 'simu' ICI
})

# --- 6. FOOTER ---
st.markdown("""
    <div class="footer">
        <b>CentriFlow Pro v1.0</b> | M1 GM | © 2026 Univ. Maghnia
    </div>
""", unsafe_allow_html=True)

pg.run()
