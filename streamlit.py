import streamlit as st

st.set_page_config(page_title="Cricket Predictor", page_icon="🏏")

st.markdown("<h1 style='text-align:center; color:#FF5733;'>🏏 Cricket Score Predictor</h1>", unsafe_allow_html=True)

st.write("### Enter Match Details")

team1 = st.text_input("Team 1", "CSK")
team2 = st.text_input("Team 2", "MI")

runs = st.number_input("Current Runs", 0, 500)
wickets = st.number_input("Wickets Fallen", 0, 10)
overs = st.number_input("Overs Completed", 0.0, 50.0)

total_overs = 50  # ODI match

if st.button("Predict Final Score"):

    if overs == 0:
        st.warning("Enter valid overs!")
    else:
        run_rate = runs / overs
        remaining_overs = total_overs - overs

        # 🧠 Smart prediction logic
        if wickets < 3:
            multiplier = 1.2   # aggressive batting
        elif wickets < 6:
            multiplier = 1.0   # balanced
        elif wickets < 8:
            multiplier = 0.8   # careful play
        else:
            multiplier = 0.6   # defensive

        predicted_score = int(runs + (run_rate * remaining_overs * multiplier))

        st.success(f"{team1} vs {team2}")
        st.info(f"📊 Predicted Final Score: {predicted_score}")
