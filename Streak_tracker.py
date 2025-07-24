import streamlit as st
from datetime import datetime, timedelta

# Simulated in-memory user data for demonstration
user_data = {
    "user_id": "user123",
    "last_action_date": None,
    "streak_count": 0,
    "milestones": [5, 10, 15],  # Example milestones for badges
    "badges": []
}

def update_streak(user_id):
    """
    Update the streak count based on the last action date.
    
    Parameters:
    - user_id (str): The ID of the user.
    
    Returns:
    - int: Updated streak count.
    """
    current_date = datetime.now().date()
    last_action_date = user_data["last_action_date"]

    if last_action_date is None:
        # First action
        user_data["streak_count"] = 1
    else:
        # Calculate the difference in days
        diff = (current_date - last_action_date).days
        if diff == 1:
            # Increment streak
            user_data["streak_count"] += 1
        elif diff > 1:
            # Reset streak
            user_data["streak_count"] = 1

    # Update last action date
    user_data["last_action_date"] = current_date

    # Check for milestones
    check_milestones(user_data["streak_count"])

    return user_data["streak_count"]

def check_milestones(streak_count):
    """
    Check if the user has reached any milestones and award badges.
    
    Parameters:
    - streak_count (int): The current streak count.
    """
    for milestone in user_data["milestones"]:
        if streak_count == milestone and milestone not in user_data["badges"]:
            user_data["badges"].append(milestone)
            st.success(f"Congratulations! You've reached a milestone of {milestone} days and earned a badge!")

def display_streak():
    """
    Display the current streak count and badges to the user.
    """
    st.title("Streak Tracker")
    streak_count = user_data["streak_count"]
    last_action_date = user_data["last_action_date"]

    st.write(f"Current Streak: {streak_count} day(s)")
    if last_action_date:
        st.write(f"Last Action Date: {last_action_date.strftime('%Y-%m-%d')}")
    else:
        st.write("No actions recorded yet.")

    if user_data["badges"]:
        st.write("Badges Earned:")
        for badge in user_data["badges"]:
            st.write(f"🏅 {badge} days badge")

# Main function for the Streak Tracker
def streak_tracker():
    st.title("Streak Tracker: Maintain Your Eco-Friendly Actions")

    if st.button("Record Eco-Friendly Action"):
        updated_streak = update_streak(user_data["user_id"])
        st.success(f"Action recorded! Your current streak is {updated_streak} day(s).")
    
    display_streak()
