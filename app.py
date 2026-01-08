import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from bmi_calculator import calculate_bmi, bmi_status, daily_calories
from diet_planner import diet_plan
from workout_planner import workout_plan

st.set_page_config(
    page_title="AI Fitness Planner",
    page_icon="💪",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align:center;color:#2E86C1;'>🏋️ AI Personalized Workout & Diet Planner</h1>",
    unsafe_allow_html=True
)

st.write("---")

# ---------------- INPUT SECTION ----------------
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=15, max_value=60)
    weight = st.number_input("Weight (kg)", min_value=30)
    height = st.number_input("Height (cm)", min_value=120)

with col2:
    goal = st.selectbox("Fitness Goal", ["weight_loss", "muscle_gain", "maintenance"])
    food = st.selectbox("Food Preference", ["veg", "non-veg"])
    budget = st.selectbox("Budget", ["low", "medium"])

with col3:
    location = st.selectbox("Workout Location", ["home", "gym"])
    level = st.selectbox("Fitness Level", ["beginner", "intermediate", "advanced"])
    time = st.slider("Daily Workout Time (minutes)", 10, 120, 30)

st.write("---")

# ---------------- OUTPUT SECTION ----------------
if st.button("🔥 Generate My Personalized Plan"):
    bmi = calculate_bmi(weight, height)
    status, msg = bmi_status(bmi)
    calories = daily_calories(goal)

    st.subheader("📊 Health Summary")
    st.success(f"**BMI:** {bmi}  |  **Status:** {status}")
    st.info(msg)
    st.write(f"**Recommended Daily Calories:** {calories}")

    # ---------------- CHART ----------------
    fig = plt.figure()
    plt.bar(["Calories Needed"], [calories])
    plt.ylabel("Calories")
    st.pyplot(fig)

    # ---------------- DIET ----------------
    st.subheader("🥗 Personalized Diet Plan")
    diet = diet_plan(food, budget)
    st.table(diet)

    # ---------------- WORKOUT ----------------
    st.subheader("🏃 Personalized Workout Plan")
    workout = workout_plan(level, location)
    st.table(workout)

    # ---------------- PROGRESS DEMO ----------------
    st.subheader("📈 Sample Progress Tracker")
    progress = pd.DataFrame({
        "Week": ["Week 1", "Week 2", "Week 3"],
        "Weight (kg)": [weight, weight - 1, weight - 2]
    })
    st.line_chart(progress.set_index("Week"))

    # ---------------- TIPS ----------------
    tips = {
        "weight_loss": "🔥 Reduce sugar, walk more, stay consistent.",
        "muscle_gain": "💪 Eat protein-rich food & lift weights.",
        "maintenance": "⚖️ Balanced diet & regular activity."
    }

    st.success(tips[goal])

    st.balloons()
