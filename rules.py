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

def generate_patient_report(patient):
 
    suggestions = generate_suggestions(patient)
    suggestion_text = "Lifestyle Suggestions:\n" + "\n".join([f"- {s}" for s in suggestions])
    return suggestion_text

def get_patient_input():
    columns = [
        'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
        'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
    ]
    
    patient = {}
    print("Enter the following patient details (separated by space):")
    print("Pregnancies Glucose BloodPressure SkinThickness Insulin BMI DiabetesPedigreeFunction Age")
    
    values = input(": ").strip().split()
    
    if len(values) != len(columns):
        print("Error: You must enter exactly", len(columns), "values.")
        return None
    
    for col, val in zip(columns, values):
        try:
            patient[col] = float(val)  
        except ValueError:
            print(f"Invalid value for {col}. Please enter a number.")
            return None
    
    

    return values,patient

def predict_stats():
    import project_3_diabetes_prediction as p
    prediction=p.predictionn()
    if(prediction==0):
        return "Low chances of diabetes"
    else:
        return "high chances of diabetes"
        

def stats(patient):
    # Prepare a formatted multi-line string
    stats_text = (
        f"AGE: {patient['Age']}\n\n"
        f"BMI: {patient['BMI']}\n\n"
        f"BLOOD PRESSURE: {patient['BloodPressure']}\n\n"
        f"PEDIGREE FUNCTION: {patient['DiabetesPedigreeFunction']}\n\n"
        f"INSULIN: {patient['Insulin']}"
    )
    return stats_text


def imgg():
    k=input("Enter Link address of image:---")
    k=k.replace("\\","\\\\")
    return k