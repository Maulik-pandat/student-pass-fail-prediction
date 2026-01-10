
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt


df = pd.read_csv("projec1.csv")
df["Result"] = df["Result"].map({"fail": 0, "pass": 1})

X = df[["Hours", "Attendance", "PrevMarks"]]
y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

models = {
    "Logistic Regression": LogisticRegression(),
    "SVM": SVC(kernel='linear', probability=True),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=3)
}


results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    
    print(f"--- {name} ---")
    print("Accuracy:", acc)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("\n")


plt.figure(figsize=(8,5))
plt.bar(results.keys(), results.values(), color=['blue','green','red','orange'])
plt.ylim(0,1)
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()


hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance: "))
prev_marks = float(input("Enter previous marks: "))

if hours < 0 or attendance < 0 or prev_marks < 0:
    print("Invalid input values")
else:
    input_df = pd.DataFrame([[hours, attendance, prev_marks]], columns=["Hours", "Attendance", "PrevMarks"])
    input_df_scaled = scaler.transform(input_df)

    print("Predictions for the student:")
    for name, model in models.items():
        result = model.predict(input_df_scaled)[0]
        print(f"{name}: {'PASS' if result == 1 else 'FAIL'}")
