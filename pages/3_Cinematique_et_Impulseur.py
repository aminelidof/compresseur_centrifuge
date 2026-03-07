import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuration de la page
st.set_page_config(page_title="3. Cinématique & Impulseur", layout="wide")

# --- STYLE CSS : HAUTE LISIBILITÉ (TEXTE NOIR SUR FOND BLANC) ---
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    p, li, span, label { color: #000000 !important; font-size: 1.05rem; }
    h1, h2, h3 { color: #1F497D !important; }
    
    .metric-container {
        background-color: #F8F9FA;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #DEE2E6;
        text-align: center;
    }
    .analysis-box {
        background-color: #E9ECEF;
        padding: 20px;
        border-radius: 10px;
        border-left: 6px solid #1F497D;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1>📐 3. Cinématique de l\'Impulseur et Glissement</h1>', unsafe_allow_html=True)

# --- SIDEBAR INTERACTIVE ---
with st.sidebar:
    st.header("⚙️ Design de la Roue")
    N = st.number_input("Vitesse de rotation (tr/min)", value=15000, step=500)
    D2 = st.slider("Diamètre de sortie D2 (m)", 0.1, 0.8, 0.4)
    Z = st.slider("Nombre d'aubes (Z)", 12, 30, 19)
    beta2_blade = st.slider("Angle géométrique pale β2 [°]", -45, 20, 0)
    Cr2 = st.slider("Vitesse radiale (Débit) Cr2 (m/s)", 50, 250, 120)

# --- CALCULS NOYAU ---
U2 = (np.pi * D2 * N) / 60
# Facteur de glissement selon Stanitz
sigma = 1 - (1.98 / Z)

# Calcul des composantes (Idéal vs Réel)
beta2_rad = np.radians(beta2_blade)
Cw2_ideal = U2 + (Cr2 * np.tan(beta2_rad))
Cw2_real = sigma * Cw2_ideal
W_real = U2 * Cw2_real

# --- AFFICHAGE DES RÉSULTATS ---
st.subheader("📊 Tableau de Bord de l'Impulseur")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Vitesse Entraînement U2", f"{U2:.1f} m/s")
with c2:
    st.metric("Slip Factor (Stanitz)", f"{sigma:.3f}")
with c3:
    st.metric("Travail Réel (Euler)", f"{W_real/1000:.2f} kJ/kg")
with c4:
    st.metric("Giration Réelle Cw2", f"{Cw2_real:.1f} m/s")

st.divider()

# --- ANALYSE GRAPHIQUE ET THÉORIQUE ---
col_txt, col_graph = st.columns([1, 1.2])

with col_txt:
    st.markdown('<div class="analysis-box">', unsafe_allow_html=True)
    st.markdown("### 🛡️ Physique du Glissement (*Slip*)")
    st.write("""
    Dans un impulseur réel, le fluide ne suit pas parfaitement l'angle géométrique de la pale. 
    Ce phénomène est dû à l'**inertie du fluide** qui crée un vortex relatif inverse dans les canaux.
    """)
    st.latex(r"W_{réel} = \sigma \cdot U_2 \cdot C_{w2, idéal}")
    
    st.write("**Impact de la Géométrie :**")
    if beta2_blade < 0:
        st.success("✅ **Pales en arrière (Backward)** : Rendement élevé, stable, mais nécessite une vitesse $U_2$ plus grande pour le même travail.")
    elif beta2_blade == 0:
        st.info("⚖️ **Pales Radiales** : Équilibre entre robustesse mécanique et transfert d'énergie. Très commun en industrie.")
    else:
        st.warning("⚠️ **Pales en avant (Forward)** : Travail maximal mais instabilité aérodynamique élevée.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_graph:
    st.markdown("### 📐 Triangle de Sortie")
    
    # Dessin des triangles avec Matplotlib
    fig, ax = plt.subplots(figsize=(8, 5), facecolor='white')
    
    # Vecteur U2 (Base)
    ax.quiver(0, 0, U2, 0, angles='xy', scale_units='xy', scale=1, color='black', width=0.015, label='U2 (Entraînement)')
    
    # Vecteur C2 (Absolu Réel)
    ax.quiver(0, 0, Cw2_real, Cr2, angles='xy', scale_units='xy', scale=1, color='#1F497D', width=0.015, label='C2 (Vitesse Absolue)')
    
    # Vecteur V2 (Relatif Réel)
    ax.quiver(U2, 0, Cw2_real - U2, Cr2, angles='xy', scale_units='xy', scale=1, color='#E63946', width=0.012, label='V2 (Vitesse Relative)')
    
    # Limites et style
    limit_x = max(U2, Cw2_real) + 50
    limit_y = Cr2 + 50
    ax.set_xlim(-20, limit_x)
    ax.set_ylim(-20, limit_y)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.legend(loc='upper left', fontsize='small')
    
    st.pyplot(fig)

st.divider()

# --- SECTION ÉDUCATIVE COMPLÉMENTAIRE ---


st.header("🔬 Analyse des Paramètres Adimensionnels")
col_phi, col_psi = st.columns(2)

with col_phi:
    phi = Cr2 / U2
    st.markdown("**Coefficient de Débit ($\phi$)**")
    st.latex(rf"\phi = \frac{{C_{{r2}}}}{{U_2}} = {phi:.3f}")
    st.write("Représente la capacité de débit de la roue.")

with col_psi:
    psi = W_real / (U2**2)
    st.markdown("**Coefficient de Charge ($\psi$)**")
    st.latex(rf"\psi = \frac{{W}}{{U_2^2}} = {psi:.3f}")
    st.write("Indique l'efficacité du transfert d'énergie cinétique.")

st.divider()
st.caption("Module Expert M1 GM - Analyse Cinématique - Dr FODIL - Univ. Maghnia")