import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="5. Atelier Pratique - CentriFlow", layout="wide")

# --- 2. STYLE HAUTE LISIBILITÉ (SÉCURISÉ : FOND BLANC / TEXTE NOIR) ---
st.markdown("""
    <style>
    /* Fond blanc global */
    .stApp { background-color: #FFFFFF !important; }
    
    /* Force le texte noir profond sur tout le contenu Markdown et les étiquettes */
    [data-testid="stMarkdownContainer"] p, 
    [data-testid="stMarkdownContainer"] li, 
    [data-testid="stMarkdownContainer"] span,
    label { 
        color: #000000 !important; 
        font-size: 1.05rem !important;
    }
    
    /* Titres en bleu industriel pour le contraste */
    h1, h2, h3 { 
        color: #1F497D !important; 
        font-weight: 700 !important;
    }

    /* Encadrés pour les énoncés des exercices (Gris clair) */
    .exo-card {
        background-color: #F8F9FA;
        border: 1px solid #DEE2E6;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        border-left: 6px solid #1F497D;
    }

    /* Encadrés pour les solutions (Vert pâle) */
    .sol-card {
        background-color: #E7F3EF;
        border: 1px solid #D1E7DD;
        padding: 20px;
        border-radius: 10px;
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛠️ 5. Atelier Pratique : Exercices & Solutions")

st.write("""
Cette section regroupe les applications directes des principes de thermodynamique et de cinématique étudiés. 
Chaque exercice est conçu pour préparer l'étudiant aux calculs réels de conception de turbomachines radiales.
""")

# --- EXERCICE 1 : PUISSANCE ET TRAVAIL ---
st.markdown('<div class="exo-card">', unsafe_allow_html=True)
st.subheader("Exercice 1 : Calcul de la Puissance Absorbée")
st.write("""
Un compresseur centrifuge traite un débit massique $\dot{m} = 2 \, kg/s$ d'air.
- Vitesse de rotation : $18\,000 \, tr/min$
- Diamètre de sortie de roue : $0.5 \, m$
- Pales radiales ($\\beta_2=0$) avec un facteur de glissement $\sigma = 0.9$.
""")
st.write("**Question :** Calculer la puissance théorique absorbée par la machine.")
st.markdown('</div>', unsafe_allow_html=True)

with st.expander("✅ Voir la Solution Détaillée"):
    st.markdown('<div class="sol-card">', unsafe_allow_html=True)
    st.write("1. **Vitesse périphérique ($U_2$)** :")
    st.latex(r"U_2 = \frac{\pi \cdot D_2 \cdot N}{60} = \frac{\pi \cdot 0.5 \cdot 18000}{60} = 471.2 \, m/s")
    st.write("2. **Travail spécifique ($W$)** (avec $C_{w2} = \sigma U_2$) :")
    st.latex(r"W = \sigma \cdot U_2^2 = 0.9 \cdot (471.2)^2 \approx 199.8 \, kJ/kg")
    st.write("3. **Puissance ($\mathcal{P}$)** :")
    st.latex(r"\mathcal{P} = \dot{m} \cdot W = 2 \cdot 199.8 = 399.6 \, kW")
    st.markdown('</div>', unsafe_allow_html=True)

# --- EXERCICE 2 : THERMODYNAMIQUE ---
st.markdown('<div class="exo-card">', unsafe_allow_html=True)
st.subheader("Exercice 2 : Taux de Pression de l'Étage")
st.write("""
L'air entre à $T_{01} = 288 \, K$. Le rendement isentropique est $\eta_{is} = 0.82$. 
On utilise le travail $W = 199.8 \, kJ/kg$ calculé précédemment.
Données : $c_p = 1005 \, J/kg\cdot K$ et $\gamma = 1.4$.
""")
st.write("**Question :** Déterminer le taux de pression $\pi$ de cet étage.")
st.markdown('</div>', unsafe_allow_html=True)

with st.expander("✅ Voir la Solution Détaillée"):
    st.markdown('<div class="sol-card">', unsafe_allow_html=True)
    st.write("1. **Augmentation de température totale ($\Delta T_0$)** :")
    st.latex(r"\Delta T_0 = \frac{W}{c_p} = \frac{199838}{1005} \approx 198.8 \, K")
    st.write("2. **Taux de pression ($\pi$)** :")
    st.latex(r"\pi = \left[ 1 + \eta_{is} \frac{\Delta T_0}{T_{01}} \right]^{3.5} \approx 4.45")
    st.markdown('</div>', unsafe_allow_html=True)

# --- EXERCICE 3 : INFLUENCE DU NOMBRE D'AUBES ---
st.markdown('<div class="exo-card">', unsafe_allow_html=True)
st.subheader("Exercice 3 : Facteur de Glissement (Stanitz)")
st.write("""
Calculer le facteur de glissement $\sigma$ pour une roue possédant $Z = 12$ aubes, puis pour $Z = 24$ aubes.
""")
st.markdown('</div>', unsafe_allow_html=True)

with st.expander("✅ Voir la Solution Détaillée"):
    st.markdown('<div class="sol-card">', unsafe_allow_html=True)
    st.write("**Formule de Stanitz** : $\sigma = 1 - \frac{1.98}{Z}$")
    st.write("- Pour $Z=12$ : $\sigma = 0.835$")
    st.write("- Pour $Z=24$ : $\sigma = 0.917$")
    st.info("💡 Plus le nombre d'aubes est élevé, plus le fluide suit l'angle de la pale (glissement réduit).")
    st.markdown('</div>', unsafe_allow_html=True)

# --- EXERCICE 4 : CINÉMATIQUE ---
st.markdown('<div class="exo-card">', unsafe_allow_html=True)
st.subheader("Exercice 4 : Vitesse Absolue de Sortie")
st.write("""
Données : $U_2 = 400 \, m/s$, $C_{r2} = 120 \, m/s$, $\sigma = 0.9$.
""")
st.write("**Question :** Calculer la vitesse absolue $C_2$ et l'angle d'écoulement $\alpha_2$.")
st.markdown('</div>', unsafe_allow_html=True)

with st.expander("✅ Voir la Solution Détaillée"):
    st.markdown('<div class="sol-card">', unsafe_allow_html=True)
    st.write("1. **Giration ($C_{w2}$)** : $C_{w2} = \sigma \cdot U_2 = 360 \, m/s$")
    st.write("2. **Vitesse absolue ($C_2$)** :")
    st.latex(r"C_2 = \sqrt{360^2 + 120^2} \approx 379.5 \, m/s")
#    st.write("3. **Angle de sortie ($\alpha_2$)** : $\tan \alpha_2 = 360/120 \implies \alpha_2 \approx 71.5^\circ$")
#    st.markdown('</div>', unsafe_allow_html=True)

    st.write("3. **Angle de sortie (α<sub>2</sub>)** : ", unsafe_allow_html=True)
    st.latex(r'\tan \alpha_2 = \frac{360}{120} \implies \alpha_2 \approx 71.5^\circ')
    st.markdown('</div>', unsafe_allow_html=True)

# --- EXERCICE 5 : DIMENSIONNEMENT ---
st.markdown('<div class="exo-card">', unsafe_allow_html=True)
st.subheader("Exercice 5 : Limite de Vitesse au Moyeu")
st.write("""
Vitesse de rotation $N = 15\,000 \, tr/min$. On limite la vitesse périphérique au moyeu à $U_{hub} = 150 \, m/s$.
""")
st.write("**Question :** Déterminer le diamètre maximal du moyeu ($D_{max}$).")
st.markdown('</div>', unsafe_allow_html=True)

with st.expander("✅ Voir la Solution Détaillée"):
    st.markdown('<div class="sol-card">', unsafe_allow_html=True)
    st.latex(r"D = \frac{60 \cdot U}{\pi \cdot N} = \frac{60 \cdot 150}{\pi \cdot 15000} \approx 0.191 \, m")
    st.markdown('</div>', unsafe_allow_html=True)



st.divider()

# --- SYNTHÈSE FINALE ---
st.header("🚀 Synthèse du cours")
st.markdown("""
| Paramètre | Compresseur Axial | Compresseur Centrifuge |
| :--- | :--- | :--- |
| **Taux de Pression / Étage** | Faible (1.2 - 1.5) | Élevé (4.0 - 7.0) |
| **Débit Massique** | Très Élevé | Moyen |
| **Stabilité** | Sensible | Robuste |
""")

st.success("Félicitations ! Vous avez terminé le module CentriFlow Pro.")
st.caption("Support de cours Master 1 GM | Université de Maghnia | Dr FODIL")
