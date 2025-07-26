# 🩺 Diabetes Prediction Medical Report

This project generates a **medical-style report** using patient health metrics, predicts the chances of diabetes, and provides **personalized lifestyle suggestions**. It also embeds a **QR code** linking to trusted health resources.

---

## 📌 Features
- **Machine Learning Prediction**: Uses a trained classifier to predict diabetes risk (low/moderate/high).
- **Custom Medical Report**:
  - Patient image on the left.
  - Predictions & patient stats on the right.
  - Lifestyle suggestions below.
  - QR code for additional health tips.
- **Matplotlib-based Layout**: Custom 2x2 subplot design with dark theme.
- **Rule-Based Suggestions**: Generates advice based on key columns such as:
  - Glucose
  - Blood Pressure
  - BMI
  - Insulin levels
  - Family history
- **QR Code Integration**: Scannable QR linking to a health guide (e.g., [Healthline](https://www.healthline.com)).

---

## 🛠 Tech Stack
- **Python 3.10+**
- **Matplotlib** – for plotting the report layout.
- **NumPy & Pandas** – for data handling.
- **Scikit-learn** – for diabetes prediction.
- **PIL / Matplotlib Image** – for image handling.
- **qrcode** – for generating QR codes.

---

## ⚙️ How It Works
1. **Input Patient Data**:
   - Age, BMI, Blood Pressure, Glucose, etc.
2. **Prediction**:
   - A trained classifier (`project_3_diabetes_prediction.py`) predicts diabetes chances.
3. **Lifestyle Suggestions**:
   - `rules.py` applies multiple rule-based conditions to provide actionable steps.
4. **Report Generation**:
   - `matplotlib` creates a **visual report** (Image + Predictions + Suggestions + QR Code).
5. **QR Code**:
   - Provides additional resources for healthy lifestyle tips.

---

## 🚀 Getting Started

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/diabetes-medical-report.git
cd diabetes-medical-report
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Project
bash
Copy
Edit
python main.py
🧠 Example Patient Data
Column	Value
Age	45
BMI	26.5
Blood Pressure	130-140
Family History	Kidney Issues
Physical Activity	Low

📷 Sample Report Output
Left: Patient image.

Right: Predictions & stats.

Bottom-left: Suggestions.

Bottom-right: QR code + Report generation time.

📌 Future Enhancements
Deploy report generator as a web app (Flask/Streamlit).

Add downloadable PDF reports.

Integrate with real-time health APIs.
