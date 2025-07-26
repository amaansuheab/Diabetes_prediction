def rule_glucose(patient):
    if patient['Glucose'] >= 126:
        return "Monitor and control sugar intake due to high glucose levels."
    elif patient['Glucose'] >= 100:
        return "Glucose slightly high, consider reducing refined carbs."
    return None

def rule_blood_pressure(patient):
    if patient['BloodPressure'] >= 130:
        return "Blood pressure is high, reduce salt and stress."
    elif patient['BloodPressure'] < 70:
        return "Blood pressure is low, ensure adequate hydration."
    return None

def rule_bmi(patient):
    bmi = patient['BMI']
    if bmi > 25:
        return "Adopt a calorie-controlled diet and regular exercise for BMI reduction."
    elif bmi < 18.5:
        return "Increase nutrient-rich calorie intake for healthy weight gain."
    return None

def rule_insulin(patient):
    if patient['Insulin'] > 200:
        return "High insulin detected, consider consulting a doctor."
    return None

def rule_pedigree(patient):
    if patient['DiabetesPedigreeFunction'] > 0.7:
        return "High family diabetes risk, regular checkups are advised."
    return None

def rule_age(patient):
    if patient['Age'] >= 45:
        return "Age is a factor, maintain an active lifestyle to lower risk."
    return None

def combo_glucose_bmi(patient):
    if patient['Glucose'] >= 126 and patient['BMI'] > 25:
        return "High glucose and BMI suggest increased diabetes risk; focus on diet + exercise."
    elif patient['Glucose'] >= 126 and patient['BloodPressure'] >= 130:
        return "High glucose and BP detected, adopt a low-salt, low-sugar diet immediately."
    return None

def combo_age_pedigree(patient):
    if patient['Age'] > 45 and patient['DiabetesPedigreeFunction'] > 0.8:
        return "Age and family history increase risk; schedule regular screenings."
    return None

def combo_insulin_glucose(patient):
    if patient['Insulin'] > 200 and patient['Glucose'] >= 126:
        return "High insulin and glucose indicate strong diabetes risk; consult a doctor."
    return None

def generate_suggestions(patient):
    single_rules = [rule_glucose, rule_blood_pressure, rule_bmi,
                    rule_insulin, rule_pedigree, rule_age]
    combo_rules = [combo_glucose_bmi, combo_age_pedigree, combo_insulin_glucose]
    suggestions = []
    for rule in single_rules + combo_rules:
        s = rule(patient)
        if s:
            suggestions.append(s)
    return suggestions

def generate_patient_report(patient, image_path=None):
 
    suggestions = generate_suggestions(patient)
    suggestion_text = "Lifestyle Suggestions:\n" + "\n".join([f"- {s}" for s in suggestions])