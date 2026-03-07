import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuration de la page
st.set_page_config(page_title="6. Simulateur Expert - CentriFlow", layout="wide")

# --- STYLE BLANC ET NOIR (LISIBILITÉ MAXIMALE) ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    .stMarkdown p, .stMarkdown li, label, .stMetric, span { 
        color: #000000 !important; 
        font-size: 1.05rem !important;
    }
    h1, h2, h3 { color: #1F497D !important; font-weight: 700; }
    [data-testid="stMetricValue"] { color: #1F497D !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Simulateur de Design de l'Impulseur")
st.write("Modifiez les paramètres de conception pour observer l'influence sur les performances de l'étage en temps réel.")

# --- SIDEBAR DE CONTRÔLE ---
with st.sidebar:
    st.header("🛠️ Paramètres de Conception")
    n = st.slider("Vitesse de rotation (tr/min)", 5000, 30000, 15000)
    d2 = st.slider("Diamètre de sortie D2 (m)", 0.1, 0.8, 0.4)
    beta2 = st.slider("Angle de pale β2 (deg)", -45, 20, 0)
    cr2 = st.slider("Vitesse radiale Cr2 (m/s)", 50, 250, 120)
    z = st.number_input("Nombre d'aubes (Z)", 12, 36, 19)
    eta_is = st.slider("Rendement isentropique", 0.70, 0.95, 0.85)

# --- CALCULS PHYSIQUES ---
cp = 1005 # J/kg.K
t01 = 288.15 # K
gamma = 1.4

# 1. Cinématique
u2 = (np.pi * d2 * n) / 60
sigma = 1 - (1.98 / z) # Formule de Stanitz
cw2_ideal = u2 + (cr2 * np.tan(np.radians(beta2)))
cw2_real = sigma * cw2_ideal
w = u2 * cw2_real # Équation d'Euler

# 2. Thermodynamique
delta_t0 = w / cp
pi = (1 + eta_is * (delta_t0 / t01))**(gamma/(gamma-1))

# --- AFFICHAGE DES RÉSULTATS ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Vitesse U2", f"{u2:.1f} m/s")
c2.metric("Travail spécifique", f"{w/1000:.1f} kJ/kg")
c3.metric("Saut Temp. ΔT0", f"{delta_t0:.1f} K")
c4.metric("Taux de Pression π", f"{pi:.2f}")

st.divider()

# --- VISUALISATION ---
col_plot, col_text = st.columns([1.5, 1])

with col_plot:
    st.subheader("📐 Triangle de Sortie Dynamique")
    fig, ax = plt.subplots(figsize=(8, 5), facecolor='white')
    
    # Dessin des vecteurs
    ax.quiver(0, 0, u2, 0, angles='xy', scale_units='xy', scale=1, color='black', label='U2 (Entraînement)')
    ax.quiver(0, 0, cw2_real, cr2, angles='xy', scale_units='xy', scale=1, color='#1F497D', label='C2 (Vitesse Absolue)')
    ax.quiver(u2, 0, cw2_real - u2, cr2, angles='xy', scale_units='xy', scale=1, color='#E63946', label='V2 (Vitesse Relative)')
    
    ax.set_xlim(-50, max(u2, cw2_real) + 100)
    ax.set_ylim(-20, cr2 + 80)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.legend(loc='upper left')
    st.pyplot(fig)

with col_text:
    st.subheader("🔬 Diagnostic d'Ingénierie")
    phi = cr2 / u2 # Coefficient de débit
    psi = w / (u2**2) # Coefficient de charge
    
    st.write(f"**Coefficient de débit ($\phi$)** : {phi:.3f}")
    st.write(f"**Coefficient de charge ($\psi$)** : {psi:.3f}")
    
    if u2 > 500:
        st.error("🚨 **Alerte** : Vitesse périphérique critique. Risque de rupture mécanique.")
    elif pi > 7:
        st.warning("⚠️ **Alerte** : Taux de pression très élevé. Risque de décrochage.")
    else:
        st.success("✅ **Design Stable** : Les paramètres respectent les standards.")

st.divider()
st.caption("CentriFlow Pro v1.0 | Simulateur Expert | © 2026 Univ. Maghnia")