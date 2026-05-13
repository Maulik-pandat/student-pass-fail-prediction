# STUDENT PASS FAIL PREDICTION PROJECT

 ABOUT THIS PROJECT-
This project predicts whether a student will PASS or FAIL using Machine Learning.

The prediction is based on:
- Study Hours
- Attendance
- Previous Marks

Multiple machine learning models were trained and compared to find the best performing model.

---

# DATASET DETAILS

**Dataset File:** `project1.csv`

# Columns Used
- `Hours` → Number of study hours
- `Attendance` → Attendance percentage
- `PrevMarks` → Previous exam marks
- `Result` → Pass or Fail (Target Column)

---

# TECHNOLOGIES USED
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

---

# MACHINE LEARNING MODELS USED
- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- K-Nearest Neighbors (KNN)

---

# PROJECT WORKFLOW

1. Loaded dataset using pandas
2. Converted pass/fail values into numerical form
3. Selected features and target column
4. Split data into training and testing sets
5. Applied feature scaling using `StandardScaler`
6. Trained multiple machine learning models
7. Evaluated models using:
   - Accuracy Score
   - Confusion Matrix
   - Classification Report
8. Compared model performance using a bar graph
9. Predicted student result using user input

---

## MODEL ACCURACY GRAPH

The graph below compares the accuracy of different machine learning models.

`model_accuracy.png`

---

# HOW TO RUN THIS PROJECT

### 1. Clone the Repository
```bash
git clone <your-github-repo-link>
```

# 2. Install Required Libraries
```bash
pip install pandas numpy scikit-learn matplotlib
```

# 3. Run the Project
```bash
python new_project.py
```

# 4. Enter Student Details
Provide:
- Study Hours
- Attendance
- Previous Marks

---

# OUTPUT

The project displays:
- Accuracy of each model
- Confusion Matrix
- Classification Report
- PASS or FAIL prediction

---

# WHAT I LEARNED FROM THIS PROJECT
- Data Preprocessing
- Feature Scaling
- Machine Learning Model Training
- Model Evaluation
- Data Visualization
- Building a Real-World ML Project

---

## AUTHOR 

MAULIK BHARDWAJ 
**Maulik Bhardwaj**

Python | Data Science & Machine Learning Learner
