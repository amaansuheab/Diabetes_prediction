from Customfnc import get_patient_input
import warnings
warnings.filterwarnings("ignore")
import sklearn as sk
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
print(diabetes_dataset.head(5))


input_data,data=get_patient_input()

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


std_data = scaler.transform(input_data_reshaped)


predictions = classifier.predict(std_data)
print(predictions)
print("------------------------------------------------------------PREDICTION------------------------------------------------------------")
if(predictions==1):
    print("Chances of Diabetes")
else:
    print("Very Low chances of Diabetes")
def predictionn():
    return data,predictions
