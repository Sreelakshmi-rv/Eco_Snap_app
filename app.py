# Trigger rebuild
import streamlit as st

# Import feature modules
from AI_analyzer import ai_analyzer
from Co2_estimator import co2_estimator
from CSR_dashboard import csr_dashboard
from Ecosnap_camera import eco_snap_camera
from Leaderboards import leaderboard
from Personal_dashboard import personal_dashboard
from Reward_center import reward_center
from Streak_tracker import streak_tracker

# Main App Layout
def main():
    st.set_page_config(page_title="EcoSnap 🌿", layout="wide")
    st.sidebar.title("EcoSnap Navigation")
    st.title("🌏 Welcome to EcoSnap")
    st.markdown("Track your eco-actions, estimate CO₂ savings, and earn rewards!")

    # Sidebar navigation
    pages = {
        "🌏 Home": "home",
        "📷 EcoSnap Camera": eco_snap_camera,
        "🧩 AI Analyzer": ai_analyzer,
        "📊 CO₂ Estimator": co2_estimator,
        "📈 Personal Dashboard": personal_dashboard,
        "🌱 CSR Dashboard": csr_dashboard,
        "🏆 Leaderboards": leaderboard,
        "🔥 Streak Tracker": streak_tracker,
        "⭐ Reward Center": reward_center
    }

    choice = st.sidebar.radio("Choose a feature:", list(pages.keys()))

    if choice == "🌏 Home":
        st.header("Get Started")
        st.write("Upload an image, track your actions, and explore the impact of your eco-friendly choices!")
    else:
        selected_page = pages[choice]
        if selected_page:
            selected_page()

if __name__ == "__main__":
    main()
