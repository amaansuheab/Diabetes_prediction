
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

diabetes_dataset = pd.read_csv(r"C:\\Users\\amaan\\OneDrive\diabetes.csv")



diabetes_dataset.head()


diabetes_dataset.shape

# getting the statistical measures of the data
diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()



diabetes_dataset.groupby('Outcome').mean()

# separating the data and labels
X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
Y = diabetes_dataset['Outcome']

print(X)

print(Y)


scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']

print(X)
print(Y)


X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)



classifier = svm.SVC(kernel='linear')

classifier.fit(X_train, Y_train)



X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy score of the training data : ', training_data_accuracy)


X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score of the test data : ', test_data_accuracy)



input_data = (5,166,72,19,175,25.8,0.587,51)


input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person has chances of getting diabetes')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread(r"C:\Users\amaan\Downloads\WhatsApp Image 2025-07-22 at 12.00.34 AM.jpeg")

age = 45
bmi = round(70 / (1.63 ** 2), 1)
bp = "130-140 mmHg"
family_history = "Kidney issues"
physical_activity = "Low"
result = "Chances of diabetes are LOW-MODERATE but might increase due to lifestyle."
steps = [
    "Increase daily physical activity (30-40 mins walk).",
    "Adopt a balanced diet with less sugar and salt.",
    "Regular health checkups (every 6 months)."
]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1, 1.5]})
fig.patch.set_facecolor('#1e1e1e')  
ax1.imshow(img)
ax1.axis('off')
ax1.set_title("PATIENT IMAGE", fontsize=16, fontweight='bold', color='white', pad=15)

ax2.set_facecolor('#1e1e1e')
ax2.axis('off')

report_text = (
    f"--- PATIENT MEDICAL REPORT ---\n\n"
    f"Age: {age} years\n"
    f"BMI: {bmi} (Overweight)\n"
    f"Blood Pressure: {bp}\n"
    f"Family History: {family_history}\n"
    f"Physical Activity: {physical_activity}\n\n"
    f"HEALTH PREDICTION:\n"
    f"{result}\n\n"
    f"LIFESTYLE CHANGES SUGGESTED:\n"
    f"1. {steps[0]}\n"
    f"2. {steps[1]}\n"
    f"3. {steps[2]}"
)

ax2.text(
    0.02, 0.95, report_text,
    fontsize=14, va='top', ha='left', wrap=True,
    color='white', linespacing=2
)

plt.tight_layout()
plt.show()
