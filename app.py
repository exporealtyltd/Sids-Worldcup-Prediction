import streamlit as st
import numpy as np
import pandas as pd
import requests

# --- PREMIUM PAGE CONFIGURATION ---
st.set_page_config(
    page_title="2026 WORLD CUP MASTER INTEL", 
    page_icon="🏆", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS INJECTION FOR PREMIUM LOOK ---
st.markdown("""
    <style>
        /* Main background and font styling */
        .main {
            background-color: #0e1117;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        /* Metric Card Styling */
        div[data-testid="stMetricValue"] {
            font-size: 2rem !important;
            color: #00ffcc !important;
            font-weight: 700;
        }
        div[data-testid="stMetricLabel"] {
            font-size: 0.9rem !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #a3a8b4 !important;
        }
        /* Custom Header Banners */
        .main-header {
            font-size: 2.5rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 5px;
            letter-spacing: -1px;
        }
        .sub-header {
            font-size: 1.1rem;
            color: #00ffcc;
            margin-bottom: 25px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
    </style>
""", unsafe_content_html=True)

# --- SECURE API CONFIGURATION ---
API_KEY = "def0410353msh4f0c9e999c853b2p19875fjsne44396d20fe1" 
API_HOST = "free-api-live-football-data.p.rapidapi.com"

@st.cache_data(ttl=300)
def fetch_live_world_cup_data():
    url = f"https://{API_HOST}/football-get-all-leagues-with-countries"
    headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": API_HOST}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("response", []) if isinstance(data, dict) else data
        return []
    except:
        return []

live_tournament_feed = fetch_live_world_cup_data()

# --- HARDCODED 24-GAME OPENING ROUND DIRECTORY ---
opening_round_schedule = {
    "Thursday, June 11": [
        {"match": "Mexico vs South Africa", "group": "Group A", "score": "1–0", "market": "Mexico ML & Under 2.5", "prop": "S. Giménez Anytime Goal"},
        {"match": "South Korea vs Czechia", "group": "Group A", "score": "1–1", "market": "South Korea Win or Draw (DC)", "prop": "H. Son Over 1.5 Shots on Target"}
    ],
    "Friday, June 12": [
        {"match": "Canada vs Bosnia & Herzegovina", "group": "Group B", "score": "2–1", "market": "Canada ML & Over 2.5", "prop": "J. David Anytime Assist"},
        {"match": "USA vs Paraguay", "group": "Group D", "score": "2–0", "market": "USA ML / Under 2.5", "prop": "C. Pulisic Over 1.5 Fouled"}
    ],
    "Saturday, June 13": [
        {"match": "Qatar vs Switzerland", "group": "Group B", "score": "0–2", "market": "Switzerland ML / Qatar U0.5 Goals", "prop": "G. Xhaka Over 55.5 Completed Passes"},
        {"match": "Brazil vs Morocco", "group": "Group C", "score": "2–0", "market": "Brazil ML & Under 2.5", "prop": "Vinícius Jr. Over 1.5 Takeons"},
        {"match": "Haiti vs Scotland", "group": "Group C", "score": "1–3", "market": "Scotland ML & Over 2.5", "prop": "S. McTominay Over 0.5 Shots on Target"},
        {"match": "Australia vs Türkiye", "group": "Group D", "score": "1–2", "market": "Türkiye ML or Draw (DC)", "prop": "H. Calhanoglu Over 1.5 Key Passes"}
    ],
    "Sunday, June 14": [
        {"match": "Germany vs Curaçao", "group": "Group E", "score": "4–0", "market": "Germany -2.5 Asian Handicap", "prop": "F. Wirtz Over 1.5 Scoring Contributions"},
        {"match": "Netherlands vs Japan", "group": "Group F", "score": "2–2", "market": "Both Teams to Score (BTTS)", "prop": "K. Mitoma Over 2.5 Dribbles Completed"},
        {"match": "Ivory Coast vs Ecuador", "group": "Group E", "score": "1–1", "market": "Match Draw (Value Play)", "prop": "P. Estupiñán Over 1.5 Interceptions"},
        {"match": "Sweden vs Tunisia", "group": "Group F", "score": "1–0", "market": "Sweden ML & Under 2.5", "prop": "A. Isak Anytime Goalscorer"}
    ],
    "Monday, June 15": [
        {"match": "Spain vs Cape Verde", "group": "Group H", "score": "3–0", "market": "Spain Win to Nil", "prop": "L. Yamal Anytime Assist"},
        {"match": "Belgium vs Egypt", "group": "Group G", "score": "2–1", "market": "Belgium ML & Over 1.5 Goals", "prop": "M. Salah Over 1.5 Shots on Target"},
        {"match": "Saudi Arabia vs Uruguay", "group": "Group H", "score": "0–3", "market": "Uruguay ML & Over 2.5 Goals", "prop": "D. Núñez Score Anytime"},
        {"match": "Iran vs New Zealand", "group": "Group G", "score": "1–0", "market": "Iran ML & Under 2.5", "prop": "M. Taremi Anytime Goal"}
    ],
    "Tuesday, June 16": [
        {"match": "France vs Senegal", "group": "Group I", "score": "2–0", "market": "France ML & Under 2.5", "prop": "K. Mbappé Anytime Goal"},
        {"match": "Iraq vs Norway", "group": "Group I", "score": "0–2", "market": "Norway -1.5 Asian Handicap", "prop": "E. Haaland First Goalscorer"},
        {"match": "Argentina vs Algeria", "group": "Group J", "score": "3–1", "market": "Argentina ML & Over 2.5", "prop": "L. Messi Over 2.5 Key Passes"},
        {"match": "Austria vs Jordan", "group": "Group J", "score": "2–0", "market": "Austria Win to Nil", "prop": "M. Sabitzer Anytime Assist"}
    ],
    "Wednesday, June 17": [
        {"match": "Portugal vs DR Congo", "group": "Group K", "score": "3–0", "market": "Portugal -1.5 Asian Handicap", "prop": "B. Fernandes Over 2.5 Shots"},
        {"match": "England vs Croatia", "group": "Group L", "score": "1–0", "market": "England ML & Under 2.5", "prop": "J. Bellingham Over 2.5 Tackles"},
        {"match": "Ghana vs Panama", "group": "Group L", "score": "2–0", "market": "Ghana ML", "prop": "M. Kudus Score or Assist"},
        {"match": "Uzbekistan vs Colombia", "group": "Group K", "score": "1–2", "market": "Colombia ML & Over 1.5", "prop": "L. Díaz Over 1.5 Shots on Target"}
    ]
}

# --- WORLD CUP 48-TEAM SEED MATRIX ---
base_world_cup_teams = {
    "Mexico": {"off": 2.1, "def": 0.8, "form_mod": 1.0}, "South Africa": {"off": 1.1, "def": 1.3, "form_mod": 1.0},
    "South Korea": {"off": 1.8, "def": 1.2, "form_mod": 1.0}, "Czechia": {"off": 1.4, "def": 1.1, "form_mod": 1.0},
    "Canada": {"off": 2.2, "def": 1.2, "form_mod": 1.0}, "Switzerland": {"off": 1.9, "def": 0.8, "form_mod": 1.0},
    "Qatar": {"off": 1.0, "def": 1.9, "form_mod": 1.0}, "Bosnia & Herzegovina": {"off": 1.3, "def": 2.0, "form_mod": 1.0},
    "Brazil": {"off": 2.9, "def": 0.6, "form_mod": 1.0}, "Morocco": {"off": 1.8, "def": 0.7, "form_mod": 1.0},
    "Scotland": {"off": 1.4, "def": 1.5, "form_mod": 1.0}, "Haiti": {"off": 0.9, "def": 2.5, "form_mod": 1.0},
    "USA": {"off": 2.2, "def": 0.9, "form_mod": 1.0}, "Paraguay": {"off": 1.1, "def": 1.1, "form_mod": 1.0},
    "Australia": {"off": 1.3, "def": 1.4, "form_mod": 1.0}, "Türkiye": {"off": 1.8, "def": 1.3, "form_mod": 1.0},
    "Germany": {"off": 3.2, "def": 0.5, "form_mod": 1.0}, "Curaçao": {"off": 0.8, "def": 2.9, "form_mod": 1.0},
    "Ivory Coast": {"off": 1.9, "def": 1.2, "form_mod": 1.0}, "Ecuador": {"off": 1.8, "def": 1.0, "form_mod": 1.0},
    "Netherlands": {"off": 2.4, "def": 0.8, "form_mod": 1.0}, "Japan": {"off": 2.2, "def": 1.1, "form_mod": 1.0},
    "Sweden": {"off": 1.7, "def": 1.1, "form_mod": 1.0}, "Tunisia": {"off": 1.1, "def": 1.4, "form_mod": 1.0},
    "Belgium": {"off": 2.3, "def": 1.0, "form_mod": 1.0}, "Egypt": {"off": 1.7, "def": 1.2, "form_mod": 1.0},
    "Iran": {"off": 1.2, "def": 1.2, "form_mod": 1.0}, "New Zealand": {"off": 1.0, "def": 1.8, "form_mod": 1.0},
    "Spain": {"off": 2.8, "def": 0.6, "form_mod": 1.0}, "Uruguay": {"off": 2.5, "def": 0.8, "form_mod": 1.0},
    "Saudi Arabia": {"off": 1.2, "def": 1.9, "form_mod": 1.0}, "Cabo Verde": {"off": 1.1, "def": 2.0, "form_mod": 1.0},
    "France": {"off": 3.1, "def": 0.6, "form_mod": 1.0}, "Senegal": {"off": 1.8, "def": 1.1, "form_mod": 1.0},
    "Norway": {"off": 2.2, "def": 1.3, "form_mod": 1.0}, "Iraq": {"off": 1.1, "def": 1.7, "form_mod": 1.0},
    "Argentina": {"off": 3.0, "def": 0.6, "form_mod": 1.0}, "Algeria": {"off": 1.6, "def": 1.3, "form_mod": 1.0},
    "Austria": {"off": 1.9, "def": 1.1, "form_mod": 1.0}, "Jordan": {"off": 1.0, "def": 2.1, "form_mod": 1.0},
    "Portugal": {"off": 2.8, "def": 0.7, "form_mod": 1.0}, "Colombia": {"off": 2.3, "def": 0.9, "form_mod": 1.0},
    "Uzbekistan": {"off": 1.2, "def": 1.6, "form_mod": 1.0}, "DR Congo": {"off": 1.3, "def": 1.5, "form_mod": 1.0},
    "England": {"off": 2.7, "def": 0.7, "form_mod": 1.0}, "Croatia": {"off": 1.7, "def": 1.0, "form_mod": 1.0},
    "Ghana": {"off": 1.9, "def": 1.3, "form_mod": 1.0}, "Panama": {"off": 1.1, "def": 1.8, "form_mod": 1.0}
}

# BRANDED HEADERS
st.markdown('<div class="main-header">🏆 QUANTUM WORLD CUP QUANT DATA</div>', unsafe_content_html=True)
st.markdown('<div class="sub-header">PRO-TIER BETTING BLUEPRINTS & SIMULATION SYSTEMS</div>', unsafe_content_html=True)

# --- NAVIGATION SIDEBAR ---
st.sidebar.markdown("### 🖥️ CONTROL TERMINAL")
view_mode = st.sidebar.radio("Navigate Views:", ["📈 Opening Round Cheat Sheets", "🤖 Algorithmic Monte Carlo Sim"])

if view_mode == "📈 Opening Round Cheat Sheets":
    st.markdown("### 📋 24-Game Opening Round Master Matrix")
    
    days = list(opening_round_schedule.keys())
    selected_day = st.selectbox("📅 Select Tournament Slate:", days)
    
    # Generate Table Data Dynamic
    day_matches = opening_round_schedule[selected_day]
    parsed_table = []
    for match in day_matches:
        parsed_table.append({
            "Match Event": match["match"],
            "Group": match["group"],
            "Proj Score": match["score"],
            "Value Angle (Best Market)": match["market"],
            "High-Conviction Prop": match["prop"]
        })
    
    st.dataframe(pd.DataFrame(parsed_table), use_container_width=True, hide_index=True)
    
    st.markdown("""
        <div style="background-color: #1e293b; padding: 15px; border-left: 4px solid #00ffcc; border-radius: 4px; margin-top: 20px;">
            <span style="color: #ffffff; font-weight: bold;">💎 Anchor Slates:</span> 
            <span style="color: #cbd5e1;">Cross-parlay Germany -2.5, Uruguay ML, and Ghana ML for highly optimized value padding.</span>
        </div>
    """, unsafe_content_html=True)

else:
    st.markdown("### 🤖 10,000-Iteration Generative Model Matrix")
    available_countries = sorted(list(base_world_cup_teams.keys()))
    
    c1, c2 = st.columns(2)
    with c1:
        team_a = st.selectbox("Side A (Favorite Profile)", available_countries, index=available_countries.index("USA") if "USA" in available_countries else 0)
    with c2:
        team_b = st.selectbox("Side B (Underdog Profile)", available_countries, index=available_countries.index("Paraguay") if "Paraguay" in available_countries else 1)
        
    if st.button("🚀 Calculate Generative Odds"):
        stats_a = base_world_cup_teams[team_a]
        stats_b = base_world_cup_teams[team_b]
        
        lambda_a = (stats_a["off"] * stats_a["form_mod"]) * (stats_b["def"]) / 1.5
        lambda_b = (stats_b["off"] * stats_b["form_mod"]) * (stats_a["def"]) / 1.5
        
        sim_a = np.random.poisson(lambda_a, 10000)
        sim_b = np.random.poisson(lambda_b, 10000)
        
        w_a = np.sum(sim_a > sim_b) / 10000
        dr = np.sum(sim_a == sim_b) / 10000
        w_b = np.sum(sim_a < sim_b) / 10000
        
        o25 = np.sum((sim_a + sim_b) > 2.5) / 10000
        u25 = np.sum((sim_a + sim_b) < 2.5) / 10000
        btts = np.sum((sim_a > 0) & (sim_b > 0)) / 10000
        
        # Display Output Metrics with stunning layout
        st.markdown(f"#### 🎯 Probabilities Blueprint: **{team_a} vs {team_b}**")
        m1, m2, m3 = st.columns(3)
        m1.metric(f"{team_a} Win", f"{w_a*100:.1f}%")
        m2.metric("Draw Factor", f"{dr*100:.1f}%")
        m3.metric(f"{team_b} Win", f"{w_b*100:.1f}%")
        
        st.markdown(f"### 📊 Most Probable Scoreline: `{round(np.mean(sim_a))} - {round(np.mean(sim_b))}`")
        
        st.subheader("💰 Smart Derivative Lines")
        p1, p2, p3 = st.columns(3)
        p1.metric("Over 2.5 Match Goals", f"{o25*100:.1f}%")
        p2.metric("Under 2.5 Match Goals", f"{u25*100:.1f}%")
        p3.metric("Both Teams to Score", f"{btts*100:.1f}%")
