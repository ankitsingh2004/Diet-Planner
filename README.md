🥗 Diet Planner & Fitness Assistant

A Python project to plan balanced diets, calculate BMI, and recommend workouts using simple data and logic.

🚀 Project Overview

This repository contains a Python-based diet planning and fitness tool that helps users create personalized meal plans, calculate body metrics (like BMI), and generate workout suggestions — all through Python scripts and CSV data.

It combines:

Diet planning logic

Nutritional data

BMI calculation

Workout recommendations

This is perfect for students, learners, and fitness enthusiasts who want a simple yet powerful Python project.

📁 Repository Contents
File	Description
diet_planner.py	Main diet planning logic using food data CSV
bmi_calculator.py	Calculates BMI and suggests category
workout_planner.py	Provides basic workout plan logic
app.py	Entry point (connects modules for combined functionality)
food_data.csv	List of foods + calories & nutrition
workout_data.csv	List of workouts and details
requirements.txt	Required Python packages
🛠️ Tech Stack

🐍 Python

📊 CSV datasets for food & workout data

🧠 Basic algorithms for planning and recommendations

🔍 Features
✅ Diet Planner

Reads food_data.csv

Filters items based on goals

Generates balanced daily meals

Calculates total calories & protein

✅ BMI Calculator

Takes user height & weight

Calculates Body Mass Index (BMI)

Categorizes into underweight / normal / overweight

✅ Workout Planner

Uses workout_data.csv

Suggests workouts for muscle building or fat loss goals

Works alongside diet recommendations

📈 How It Works

Load Data
Load food and workout CSV files.

User Input
Ask user for diet goals (calories/protein), height, weight.

Compute Metrics

Calories & protein totals

BMI classification

Generate Plan
Suggest foods and workouts matching user goals.

📊 Complete Metrics Used
Metric	Purpose
Total Calories	Achieve target daily intake
Protein Intake	Ensure sufficient protein
BMI	Body composition estimate
Workout Suitability	Match workouts to goals
📦 Installation

Clone the repository

git clone https://github.com/ankitsingh2004/Diet-Planner.git


Install dependencies

pip install -r requirements.txt


Run the app

python app.py

🎯 Usage Example

BMI Calculator

Enter height (cm): 170
Enter weight (kg): 65


→ Output: Your BMI is 22.5 (Normal weight)

Diet Planner

Enter daily calorie target: 1800
Enter protein target: 80


→ Plan generated with balanced meals

📚 Future Enhancements

✨ Add GUI with Tkinter or Web interface
✨ Use ML to personalize diet recommendations
✨ Add micronutrients (carbs, fats, vitamins)
✨ Save user profiles
