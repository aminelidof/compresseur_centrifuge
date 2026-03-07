import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="2. Thermodynamique Centrifuge", layout="wide")

# --- STYLE CSS POUR THÈME CLAIR ET LISIBILITÉ ---
st.markdown("""
    <style>
    /* Force le texte noir sur fond blanc pour cette page */
    .main { background-color: #FFFFFF; }
    p, li, span, label { color: #000000 !important; font-size: 1.05rem; }
    h1, h2, h3 { color: #1F497D !important; }
    
    .formula-box {
        background-color: #F8F9FA;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #DEE2E6;
        margin-bottom: 20px;
    }
    .theory-card {
        background-color: #E9ECEF;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #1F497D;
    }
    </style>
""", unsafe_allow_html=True)

# --- TITRE PRINCIPAL ---
st.markdown('<h1>🔥 2. Analyse Thermodynamique du Cycle Radial</h1>', unsafe_allow_html=True)

st.write("""
L'analyse thermodynamique d'un étage centrifuge repose sur le transfert d'énergie entre un impulseur rotatif et un fluide compressible. 
Contrairement aux machines axiales, la variation du rayon entre l'entrée et la sortie joue un rôle prépondérant dans l'augmentation de pression.
""")

# --- SECTION A : ÉQUATION D'EULER ET DÉCOMPOSITION ---
st.header("A. Transfert d'Énergie (Équation d'Euler)")

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    st.write("**Équation d'Euler sous sa forme enthalpique :**")
    st.latex(r"W = \Delta h_0 = U_2 C_{w2} - U_1 C_{w1}")
    
    st.write("**Décomposition physique du travail (Forme de Bernoulli) :**")
    st.latex(r"W = \underbrace{\frac{C_2^2 - C_1^2}{2}}_{\text{Énergie Cinétique}} + \underbrace{\frac{U_2^2 - U_1^2}{2}}_{\text{Effet Centrifuge}} + \underbrace{\frac{V_1^2 - V_2^2}{2}}_{\text{Diffusion Relative}}")
    st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("🔍 Analyse détaillée des termes", expanded=True):
        st.markdown("""
        1. **Terme Cinétique** : Représente l'augmentation de la vitesse absolue du fluide. Cette énergie sera convertie en pression dans le diffuseur.
        2. **Terme Centrifuge** : C'est le gain de pression statique dû au changement de rayon ($r_2 > r_1$). Ce terme est **nul** dans les compresseurs axiaux.
        3. **Terme de Diffusion** : Représente la transformation de la vitesse relative en pression à l'intérieur des canaux de l'impulseur.
        """)

with col2:
    st.info("💡 **Note technique** : Dans un compresseur centrifuge bien conçu, environ **50%** de l'augmentation de pression totale se produit dans l'impulseur lui-même.")
    
    st.write("**Relation Température-Travail :**")
    st.latex(r"W = c_p (T_{02} - T_{01})")
    st.write("Pour l'air : $c_p = 1004.5 \, J/(kg\cdot K)$")

st.divider()

# --- SECTION B : RENDEMENTS ET PERTES ---
st.header("B. Performance et Rendement")

tab1, tab2 = st.tabs(["📉 Rendement Isentropique", "🧱 Analyse des Pertes"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Définition :**")
        st.latex(r"\eta_{is} = \frac{h_{02s} - h_{01}}{h_{02} - h_{01}} = \frac{(P_{02}/P_{01})^{\frac{\gamma-1}{\gamma}} - 1}{(T_{02}/T_{01}) - 1}")
    with c2:
        st.markdown('<div class="theory-card">', unsafe_allow_html=True)
        st.write("**Valeurs typiques :**")
        st.write("- Compresseurs industriels : 75% - 82%")
        st.write("- Turbomachines hautes performances : 83% - 88%")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.write("L'augmentation réelle de température est toujours supérieure à l'augmentation idéale à cause des pertes :")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("""
        * **Pertes par frottement** : Viscosité du fluide dans les canaux.
        * **Pertes de choc** : À l'entrée de l'impulseur (bord d'attaque).
        * **Pertes de fuite (Clearance)** : Entre les aubes et le carter.
        """)
    with col_p2:
        st.markdown("""
        * **Pertes par disque (Windage)** : Frottement entre le dos de la roue et le fluide.
        * **Pertes de recirculation** : Retour du fluide vers l'entrée.
        """)

st.divider()

# --- SECTION C : CALCULATEUR THERMODYNAMIQUE ---
st.header("⚙️ Calculateur de Performance Rapide")
st.write("Estimez l'augmentation de température et le taux de pression théorique.")

col_input, col_res = st.columns([1, 1])

with col_input:
    t01 = st.number_input("Température entrée T01 (K)", value=288.15)
    w_req = st.number_input("Travail spécifique W (kJ/kg)", value=150.0)
    eta_is_val = st.slider("Rendement isentropique estimé", 0.70, 0.95, 0.82)

with col_res:
    # Calculs
    cp = 1.0045 # kJ/kg.K
    gamma = 1.4
    delta_t0 = w_req / cp
    t02 = t01 + delta_t0
    pi = (1 + eta_is_val * (delta_t0 / t01))**(gamma/(gamma-1))
    
    st.subheader("Résultats :")
    st.metric("Élévation de Température", f"{delta_t0:.2f} K")
    st.metric("Taux de Pression (π)", f"{pi:.3f}")

st.divider()
st.caption("🚀 CentriFlow Pro - Module de Thermodynamique Avancée - Master 1 GM")