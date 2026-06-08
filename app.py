import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load model
# -----------------------------
MODEL_PATH = "final_log_reg_model_pipeline.pkl"
model = joblib.load(MODEL_PATH)

st.set_page_config(
    page_title="Cognitive Risk Assessment",
    page_icon="🧠",
    layout="centered"
)

# ==================================================
# CUSTOM CSS — dark theme friendly
# ==================================================
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">

<style>
/* ── Global font ── */
html, body, [class*="css"], p, div, span {
    font-family: 'DM Sans', sans-serif !important;
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2.5rem !important; max-width: 700px !important; }

/* ── Hero ── */
.hero-title {
    font-family: 'DM Serif Display', serif !important;
    font-size: 32px;
    line-height: 1.15;
    color: #F0EDE6 !important;
    margin-bottom: 5px;
    font-weight: 400;
}
.hero-sub {
    font-size: 14px;
    color: #8A8A8A !important;
    margin-bottom: 1.75rem;
}

/* ── Section header banners — dark-friendly tints ── */
.section-head {
    padding: 10px 16px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 11px;
    letter-spacing: .1em;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 0.75rem;
    margin-top: 1.25rem;
}
/* Teal — Demographics */
.s-demo { background: #0D3D2E; color: #5ECFA5 !important; border: 1px solid #1A6649; }
.s-demo i, .s-demo span { color: #5ECFA5 !important; }

/* Purple — Physical */
.s-phys { background: #1E1A3E; color: #A099F5 !important; border: 1px solid #3D3580; }
.s-phys i, .s-phys span { color: #A099F5 !important; }

/* Amber — Memory */
.s-mem  { background: #3A2400; color: #F5B942 !important; border: 1px solid #6B4410; }
.s-mem  i, .s-mem  span { color: #F5B942 !important; }

/* Pink — Wellbeing */
.s-well { background: #3A1025; color: #F087B3 !important; border: 1px solid #6B2044; }
.s-well i, .s-well span { color: #F087B3 !important; }

/* ── Widget labels ── */
div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label {
    font-size: 13px !important;
    color: #C8C4BC !important;
    font-weight: 500 !important;
}

/* ── Input & select boxes ── */
div[data-testid="stSelectbox"] > div > div,
div[data-testid="stNumberInput"] input {
    background-color: #1E1E1E !important;
    border: 1.5px solid #3A3A3A !important;
    border-radius: 8px !important;
    font-size: 14px !important;
    color: #EDEDED !important;
    font-weight: 400 !important;
}
div[data-testid="stSelectbox"] > div > div:focus-within,
div[data-testid="stNumberInput"] input:focus {
    border-color: #5ECFA5 !important;
    box-shadow: 0 0 0 2px rgba(94,207,165,0.15) !important;
}

/* Dropdown text & arrow */
div[data-testid="stSelectbox"] span { color: #EDEDED !important; }
div[data-testid="stSelectbox"] svg  { color: #888 !important; }

/* Number input +/- buttons */
div[data-testid="stNumberInput"] button {
    background: #2A2A2A !important;
    border-color: #3A3A3A !important;
    color: #EDEDED !important;
}

/* ── Button ── */
div[data-testid="stButton"] > button {
    background: #1D9E75 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px !important;
    font-weight: 500 !important;
    letter-spacing: .03em !important;
    padding: 0.7rem 1.5rem !important;
    width: 100% !important;
    margin-top: 0.5rem !important;
    transition: opacity .15s !important;
}
div[data-testid="stButton"] > button:hover {
    opacity: .85 !important;
    color: #ffffff !important;
}

/* ── Result card ── */
.result-card {
    border-radius: 12px;
    border: 1px solid #2E2E2E;
    overflow: hidden;
    margin-top: 1.5rem;
    background: #1A1A1A;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.result-head {
    padding: 12px 18px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #2E2E2E;
    background: #161616;
}
.result-head-label {
    font-size: 11px;
    letter-spacing: .09em;
    text-transform: uppercase;
    color: #666 !important;
    font-weight: 500;
}
.result-body {
    padding: 1.4rem 1.2rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
    background: #1A1A1A;
}
.risk-circle-wrap {
    position: relative;
    width: 100px;
    height: 100px;
    flex-shrink: 0;
}
.risk-circle-wrap svg { transform: rotate(-90deg); }
.risk-pct-label {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'DM Serif Display', serif;
    font-size: 22px;
    color: #F0EDE6 !important;
    font-weight: 400;
}
.risk-tier-title {
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
    margin-bottom: 6px;
    color: #F0EDE6 !important;
    font-weight: 400;
}
.risk-note {
    font-size: 13px;
    color: #9A9A9A !important;
    line-height: 1.65;
}
.risk-badge {
    font-size: 12px;
    padding: 4px 12px;
    border-radius: 20px;
    font-weight: 500;
}
.bar-wrap { padding: 0 1.2rem 1.2rem; background: #1A1A1A; }
.bar-track { height: 6px; background: #2E2E2E; border-radius: 3px; overflow: hidden; }
.bar-fill  { height: 100%; border-radius: 3px; }
.bar-ticks { display: flex; justify-content: space-between; margin-top: 6px; }
.bar-ticks span { font-size: 11px; color: #555 !important; }
</style>
""", unsafe_allow_html=True)

# ==================================================
# HERO
# ==================================================
st.markdown("""
<div class="hero-title">Cognitive Risk Assessment</div>
<div class="hero-sub">Answer the questions below, then click estimate.</div>
""", unsafe_allow_html=True)

# ==================================================
# LABEL MAPS
# ==================================================
race_map = {
    1: "White, non-Hispanic",
    2: "Black, non-Hispanic",
    3: "Other, non-Hispanic",
    4: "Hispanic",
    5: "More than one",
    6: "Unknown / Prefer not to answer"
}
yes_no             = {1: "Yes", 2: "No"}
memory_rating      = {1: "Excellent", 2: "Very Good", 3: "Good", 4: "Fair", 5: "Poor"}
memory_interfere   = {1: "Every day", 2: "Most days", 3: "Some days", 4: "Rarely", 5: "Never"}
self_determination = {1: "Agree a lot", 2: "Agree a little", 3: "Agree not at all"}
cheerful_map       = {1: "Every day", 2: "Most days", 3: "Some days", 4: "Rarely", 5: "Never"}
true_me_map        = {1: "Agree a lot", 2: "Agree a little", 3: "Agree not at all"}
bed_device_map     = {1: "Every time", 2: "Most times", 3: "Sometimes", 4: "Rarely", 5: "Never"}

# ==================================================
# SECTION: Demographics
# ==================================================
st.markdown('<div class="section-head s-demo"><i class="ti ti-user"></i><span>Demographics</span></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=65, max_value=97, value=75, step=1)
with col2:
    hh13dhshldnum = st.selectbox("Number of people in household", [1,2,3,4,5,6,7,8,9,10,12])

rl13dracehisp = st.selectbox("Race / Ethnicity", list(race_map.keys()), format_func=lambda x: race_map[x])

# ==================================================
# SECTION: Physical Ability
# ==================================================
st.markdown('<div class="section-head s-phys"><i class="ti ti-activity"></i><span>Physical Ability</span></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    pc13up20stair = st.selectbox("Are you able to walk up 20 stairs?",          list(yes_no.keys()), format_func=lambda x: yes_no[x])
    pc13bendover  = st.selectbox("Are you able to bend over?",                  list(yes_no.keys()), format_func=lambda x: yes_no[x])
with col2:
    pc13car20pnds = st.selectbox("Are you able to carry 20 pounds?",            list(yes_no.keys()), format_func=lambda x: yes_no[x])
    pc13hvobovrhd = st.selectbox("Are you able to lift heavy objects overhead?", list(yes_no.keys()), format_func=lambda x: yes_no[x])

# ==================================================
# SECTION: Memory & Function
# ==================================================
st.markdown('<div class="section-head s-mem"><i class="ti ti-bulb"></i><span>Memory &amp; Function</span></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    cg13ratememry = st.selectbox("Rate your memory",           list(memory_rating.keys()),    format_func=lambda x: memory_rating[x])
    mo13outhlp    = st.selectbox("Do you need help going outside?",   list(yes_no.keys()),            format_func=lambda x: yes_no[x])
with col2:
    cg13ofmemprob = st.selectbox("How often do memory problems interfere?", list(memory_interfere.keys()), format_func=lambda x: memory_interfere[x])
    mo13beddev    = st.selectbox("How often do you use any assistive device when getting out of bed?",  list(bed_device_map.keys()),   format_func=lambda x: bed_device_map[x])

# ==================================================
# SECTION: Wellbeing
# ==================================================
st.markdown('<div class="section-head s-well"><i class="ti ti-heart"></i><span>Wellbeing</span></div>', unsafe_allow_html=True)

wb13offelche1 = st.selectbox("How often do you feel cheerful?", list(cheerful_map.keys()), format_func=lambda x: cheerful_map[x])
col1, col2 = st.columns(2)
with col1:
    wb13truestme3 = st.selectbox('"I gave up improving my life"', list(true_me_map.keys()), index=2, format_func=lambda x: true_me_map[x])
with col2:
    wb13agrwstmt1 = st.selectbox('"I am able to make my own decisions"',            list(self_determination.keys()), format_func=lambda x: self_determination[x])

# ==================================================
# PREDICT BUTTON + RESULT
# ==================================================
st.markdown("<div style='margin-top:0.75rem'></div>", unsafe_allow_html=True)

if st.button("Estimate dementia probability"):
    input_df = pd.DataFrame([{
        "cg13ofmemprob": cg13ofmemprob,
        "hh13dhshldnum": hh13dhshldnum,
        "age":           age,
        "wb13agrwstmt1": wb13agrwstmt1,
        "rl13dracehisp": rl13dracehisp,
        "pc13up20stair": pc13up20stair,
        "pc13car20pnds": pc13car20pnds,
        "pc13bendover":  pc13bendover,
        "pc13hvobovrhd": pc13hvobovrhd,
        "cg13ratememry": cg13ratememry,
        "mo13outhlp":    mo13outhlp,
        "mo13beddev":    mo13beddev,
        "wb13offelche1": wb13offelche1,
        "wb13truestme3": wb13truestme3
    }])

    if hasattr(model, "predict_proba"):
        probs         = model.predict_proba(input_df)[0]
        dementia_prob = probs[1]
        pct           = round(dementia_prob * 100)
        circ          = 251.2
        offset        = circ - (dementia_prob * circ)

        if pct < 30:
            tier      = "Low risk"
            note      = "The model estimates a lower probability of dementia based on the provided inputs."
            color     = "#5ECFA5"
            badge_bg  = "#0D3D2E"
            badge_col = "#5ECFA5"
        elif pct < 60:
            tier      = "Moderate risk"
            note      = "Several factors suggest a moderate level of estimated dementia risk. Consider discussing with a healthcare provider."
            color     = "#F5B942"
            badge_bg  = "#3A2400"
            badge_col = "#F5B942"
        else:
            tier      = "Elevated risk"
            note      = "Multiple indicators suggest elevated risk. This is a screening estimate — consult a medical professional for evaluation."
            color     = "#F07070"
            badge_bg  = "#3A1010"
            badge_col = "#F07070"

        st.markdown(f"""
        <div class="result-card">
          <div class="result-head">
            <span class="result-head-label">Risk estimate</span>
            <span class="risk-badge" style="background:{badge_bg};color:{badge_col};border:1px solid {color}40;">{tier}</span>
          </div>
          <div class="result-body">
            <div class="risk-circle-wrap">
              <svg width="100" height="100" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="40" fill="none" stroke="#2A2A2A" stroke-width="8"/>
                <circle cx="50" cy="50" r="40" fill="none" stroke="{color}" stroke-width="8"
                  stroke-dasharray="{circ}" stroke-dashoffset="{offset:.2f}" stroke-linecap="round"/>
              </svg>
              <div class="risk-pct-label">{pct}%</div>
            </div>
            <div>
              <div class="risk-tier-title">{tier}</div>
              <div class="risk-note">{note}</div>
            </div>
          </div>
          <div class="bar-wrap">
            <div class="bar-track">
              <div class="bar-fill" style="width:{pct}%;background:{color};"></div>
            </div>
            <div class="bar-ticks">
              <span>0%</span><span>25%</span><span>50%</span><span>75%</span><span>100%</span>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)