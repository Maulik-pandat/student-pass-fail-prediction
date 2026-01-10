
STUDENT PASS FAIL PREDICTION PROJECT

ABOUT THIS PROJECT
This project is about predicting whether a student will PASS or FAIL.
The prediction is done using Machine Learning based on student data like study hours, attendance and previous marks.

I trained multiple machine learning models and compared their performance to understand which model works better.


DATASET DETAILS
Dataset file name: project1.csv

Columns used in dataset:
Hours        -> Number of study hours
Attendance  -> Attendance percentage
PrevMarks   -> Previous exam marks
Result      -> Pass or Fail (target column)


TECHNOLOGIES USED
Python
Pandas
NumPy
Scikit-learn
Matplotlib



MACHINE LEARNING MODELS USED
Logistic Regression
Support Vector Machine (SVM)
Decision Tree
K-Nearest Neighbors (KNN)



PROJECT WORKFLOW

1. Loaded the dataset using pandas
2. Converted pass/fail values into numerical form
3. Selected important features and target column
4. Split data into training and testing sets
5. Applied feature scaling using StandardScaler
6. Trained multiple machine learning models
7. Evaluated models using accuracy, confusion matrix and classification report
8. Compared model performance using a bar graph
9. Took user input to predict student result



MODEL ACCURACY GRAPH
The following graph shows accuracy comparison of different models:

model_accuracy.png



HOW TO RUN THIS PROJECT

1. Download or clone this repository
2. Install required libraries using:
   pip install pandas numpy scikit-learn matplotlib
3. Run the Python file:
   python new_project.py
4. Enter student details when asked

OUTPUT
The project shows:

* Accuracy of each model
* Confusion matrix and classification report
* Pass or Fail prediction for a student

WHAT I LEARNED FROM THIS PROJECT
Data preprocessing
Feature scaling
Training multiple ML models
Model evaluation
Data visualization
Building a real-world ML project


AUTHOR
Maulik Bhardwaj
Python | Data Science & Machine Learning Learner
