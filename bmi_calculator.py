def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight", "⚠️ Focus on healthy weight gain."
    elif bmi < 25:
        return "Normal", "✅ Great! Maintain your lifestyle."
    elif bmi < 30:
        return "Overweight", "⚠️ Focus on fat loss & cardio."
    else:
        return "Obese", "🚨 Medical consultation advised."


def daily_calories(goal):
    if goal == "weight_loss":
        return 1800
    elif goal == "muscle_gain":
        return 2500
    else:
        return 2200
