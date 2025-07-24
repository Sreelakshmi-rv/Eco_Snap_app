import streamlit as st
import pandas as pd

# Simulated user data for demonstration
user_data = [
    {"username": "EcoWarrior", "total_co2_saved": 50, "streak_count": 10, "region": "Global"},
    {"username": "GreenThumb", "total_co2_saved": 40, "streak_count": 5, "region": "USA"},
    {"username": "SustainableSam", "total_co2_saved": 30, "streak_count": 15, "region": "USA"},
    {"username": "PlanetProtector", "total_co2_saved": 25, "streak_count": 7, "region": "Canada"},
    {"username": "EcoFriendly", "total_co2_saved": 20, "streak_count": 3, "region": "Global"},
    {"username": "TreeHugger", "total_co2_saved": 15, "streak_count": 12, "region": "USA"},
]

def display_leaderboard(filter_option):
    """
    Display the leaderboard based on the selected filter option.
    
    Parameters:
    - filter_option (str): The selected filter for the leaderboard.
    """
    # Convert user data to DataFrame for easier manipulation
    df = pd.DataFrame(user_data)

    # Filter based on the selected option
    if filter_option == "Global":
        filtered_df = df
    elif filter_option == "Regional":
        region = st.selectbox("Select your region", df['region'].unique())
        filtered_df = df[df['region'] == region]
    elif filter_option == "Friends":
        # Simulate friends filter (for demonstration, we will show all users)
        filtered_df = df  # In a real app, filter based on user's friends
    elif filter_option == "Corporate Teams":
        # Simulate corporate teams filter (for demonstration, we will show all users)
        filtered_df = df  # In a real app, filter based on user's corporate team

    # Sort by total CO₂ saved
    filtered_df = filtered_df.sort_values(by="total_co2_saved", ascending=False)

    # Display the leaderboard
    st.write("### Leaderboard")
    st.dataframe(filtered_df[['username', 'total_co2_saved', 'streak_count']])

    # Highlight gamified metrics
    top_streak_holder = filtered_df.loc[filtered_df['streak_count'].idxmax()]
    st.write(f"🏆 **Top Streak Holder:** {top_streak_holder['username']} with a streak of {top_streak_holder['streak_count']} days!")

    greenest_user = filtered_df.loc[filtered_df['total_co2_saved'].idxmax()]
    st.write(f"🌱 **Greenest User of the Month:** {greenest_user['username']} with {greenest_user['total_co2_saved']} kg CO₂ saved!")

# Main function for the Leaderboard
def leaderboard():
    st.title("Leaderboard: Compete and Motivate")

    filter_option = st.selectbox("Select Leaderboard Filter", ["Global", "Regional", "Friends", "Corporate Teams"])
    
    if st.button("Show Leaderboard"):
        display_leaderboard(filter_option)
