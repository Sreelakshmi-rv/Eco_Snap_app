import streamlit as st

# Simulated in-memory user data (would normally be in a database)
user_data = {
    "user_id": "user123",
    "total_co2_saved": 52.3,  # Total CO₂ saved by the user
    "available_rewards": [],
    "redeemed_rewards": []
}

# Predefined CO2 milestones and corresponding rewards
REWARD_MILESTONES = {
    5: "5% Discount Voucher for Eco Products",
    10: "Coupon from Partner Brand",
    30: "Tree Planting Credit",
    50: "Digital Certificate of Green Achievement"
}

def update_rewards(user):
    """
    Check user's CO2 savings and update available rewards based on milestones.
    """
    for milestone, reward in REWARD_MILESTONES.items():
        if user["total_co2_saved"] >= milestone and reward not in user["available_rewards"] and reward not in user["redeemed_rewards"]:
            user["available_rewards"].append(reward)

def reward_center():
    st.title("Reward Center: Earn and Redeem Your Green Rewards")

    # Update rewards based on total CO2 saved
    update_rewards(user_data)

    st.write(f"Total CO₂ Saved: {user_data['total_co2_saved']:.2f} kg")

    # Display available rewards
    st.subheader("Available Rewards")
    if user_data["available_rewards"]:
        for reward in user_data["available_rewards"]:
            st.write(f"- {reward}")
    else:
        st.write("No rewards available yet. Keep going!")

    # Redeem reward
    if user_data["available_rewards"]:
        reward_to_redeem = st.selectbox("Select a reward to redeem", user_data["available_rewards"])
        if st.button("Redeem Reward"):
            user_data["available_rewards"].remove(reward_to_redeem)
            user_data["redeemed_rewards"].append(reward_to_redeem)
            st.success(f"Reward '{reward_to_redeem}' redeemed successfully!")
    
    # Display redeemed rewards
    st.subheader("Redeemed Rewards")
    if user_data["redeemed_rewards"]:
        for reward in user_data["redeemed_rewards"]:
            st.write(f"✅ {reward}")
    else:
        st.write("No rewards redeemed yet.")

    # Notification example
    if user_data["available_rewards"]:
        st.info("🎉 You've unlocked new rewards! Redeem them now!")

