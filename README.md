# Student Performance Prediction Dashboard

A Python-based machine learning and Streamlit dashboard project for analyzing student performance factors and understanding how different academic, personal, and lifestyle-related features affect exam scores.

This project includes exploratory data analysis, data preprocessing, machine learning model comparison, and an interactive Streamlit dashboard for visualizing important student performance insights.

---

## Project Overview

Student exam performance can be influenced by multiple factors such as attendance, study hours, previous scores, sleep hours, parental involvement, access to resources, motivation level, tutoring support, and other learning conditions.

This project analyzes a student performance dataset to identify important patterns and compare machine learning models for predicting student exam scores.

The project has two main parts:

1. **Jupyter Notebook Analysis**

   * Dataset loading
   * Data cleaning
   * Missing value handling
   * Exploratory Data Analysis
   * Feature encoding
   * Model training
   * Model evaluation
   * Model comparison

2. **Streamlit Dashboard**

   * Project summary
   * Dataset overview
   * Missing value summary
   * EDA charts
   * Correlation heatmap
   * Final insights

---

## Features

* Student performance data analysis
* Missing value detection
* Statistical dataset summary
* Exploratory Data Analysis
* Exam score distribution visualization
* Attendance vs exam score analysis
* Hours studied vs exam score analysis
* Correlation heatmap
* Machine learning model comparison
* Interactive Streamlit dashboard
* Clean and beginner-friendly project structure

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Jupyter Notebook

---

## Dataset

The dataset used in this project was downloaded from Kaggle.

The dataset is **not included in this repository** because the original dataset license and redistribution permissions may vary. To use this project, download the dataset manually from Kaggle and place it inside the `data/` folder.

Expected dataset filename:

```text
StudentPerformanceFactors.csv
```

Expected dataset path:

```text
data/StudentPerformanceFactors.csv
```

The dataset contains student-related features that may affect exam performance.

Example features include:

* Hours Studied
* Attendance
* Parental Involvement
* Access to Resources
* Extracurricular Activities
* Sleep Hours
* Previous Scores
* Motivation Level
* Internet Access
* Tutoring Sessions
* Family Income
* Teacher Quality
* School Type
* Peer Influence
* Physical Activity
* Learning Disabilities
* Parental Education Level
* Distance from Home
* Gender
* Exam Score

The target variable is:

```text
Exam_Score
```

---

## Project Workflow

```text
Dataset Loading
        ↓
Data Cleaning
        ↓
Missing Value Handling
        ↓
Exploratory Data Analysis
        ↓
Feature Encoding
        ↓
Train-Test Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Comparison
        ↓
Streamlit Dashboard
```

---

## Machine Learning Models Used

The following regression models were trained and compared:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Random Forest Regressor
* Gradient Boosting Regressor

---

## Best Model

Linear Regression achieved the best performance in this project.

```text
Best Model: Linear Regression
R² Score: 0.825
```

This result suggests that the dataset mostly follows a linear pattern, where features such as attendance, study hours, and previous scores have a strong relationship with the final exam score.

---

## Key Insights

* Attendance is one of the strongest predictors of exam score.
* Hours studied has a strong positive impact on student performance.
* Previous scores show an important relationship with exam score.
* Tutoring sessions and parental involvement have moderate influence.
* Sleep hours and physical activity show weaker correlation with exam score.
* Gender has almost no visible impact on exam score in this dataset.
* Linear models performed better than tree-based models for this dataset.

---

## Streamlit Dashboard

The Streamlit dashboard provides an interactive way to explore the dataset and project results.

Dashboard pages include:

### Home

Displays the project summary and key metrics:

* Total students
* Total features
* Target variable
* Best model score

### Dataset Overview

Displays:

* Dataset shape
* Column names
* Missing values
* Statistical summary

### EDA Charts

Includes visualizations such as:

* Exam score distribution
* Attendance vs exam score
* Hours studied vs exam score
* Correlation heatmap

### Insights

Displays the final conclusions from the analysis.

---

## Project Structure

```text
student-performance-prediction-dashboard/
│
├── notebook/
│   └── SPF.ipynb
│
├── data/
│   └── .gitkeep
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

The actual dataset file is not included in the repository. After downloading the dataset from Kaggle, place it here:

```text
data/StudentPerformanceFactors.csv
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/student-performance-prediction-dashboard.git
```

Move into the project folder:

```bash
cd student-performance-prediction-dashboard
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Dataset Setup

Create a folder named `data` if it does not already exist:

```bash
mkdir data
```

Download the dataset from Kaggle and place the CSV file inside the `data` folder.

The final path should look like this:

```text
data/StudentPerformanceFactors.csv
```

Do not use a local system path such as:

```python
pd.read_csv(r"E:\RWS P\StudentPerformanceFactors.csv")
```

Use a relative path instead:

```python
pd.read_csv("data/StudentPerformanceFactors.csv")
```

This makes the project portable and allows it to run correctly after cloning from GitHub.

---

## Running the Jupyter Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```text
notebook/SPF.ipynb
```

Run the notebook cells to perform the full data analysis and model comparison.

---

## Running the Streamlit Dashboard

Run the Streamlit app:

```bash
streamlit run app.py
```

After running the command, Streamlit will open the dashboard in your browser.

Default local URL:

```text
http://localhost:8501
```

---

## Requirements

Example `requirements.txt`:

```txt
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
jupyter
```

---

## Important `.gitignore` Note

Because the dataset is not included in this repository, the `.gitignore` file should ignore CSV files or the dataset folder content.

Recommended `.gitignore` lines:

```gitignore
# Dataset files
*.csv

# Dataset files are not included because they must be downloaded from Kaggle
data/*
!data/.gitkeep
```

This keeps the `data/` folder structure in GitHub while preventing the dataset from being uploaded.

---

## How to Use This Project

1. Clone the repository.
2. Install the dependencies.
3. Download the dataset from Kaggle.
4. Place the dataset at `data/StudentPerformanceFactors.csv`.
5. Run the Jupyter notebook for full analysis.
6. Run the Streamlit app for interactive dashboard visualization.
7. Explore charts, model results, and final insights.

---

## Results Summary

The project shows that academic habits and learning support factors have a strong effect on student exam performance.

The most important factors are:

```text
Attendance
Hours Studied
Previous Scores
Tutoring Sessions
Parental Involvement
Access to Resources
```

The best model was Linear Regression with an R² score of approximately `0.825`.

---

## Future Improvements

Possible improvements for this project:

* Add a prediction form in Streamlit
* Save the trained model using Joblib or Pickle
* Allow users to enter student details and predict exam score
* Add model explainability using feature importance
* Add more advanced regression models
* Deploy the Streamlit app online
* Improve dashboard UI with custom CSS
* Add downloadable analysis report

---

## Limitations

* The dataset is not included in this repository.
* Users must download the dataset manually from Kaggle.
* The project depends on the quality and accuracy of the dataset.
* Model predictions are based only on the available dataset features.
* The dashboard currently focuses on analysis and visualization.
* The current Streamlit version is not a full prediction application unless a prediction form is added.

---

## License

This project is licensed under the MIT License.

The MIT License applies only to the source code in this repository.

The dataset belongs to its original creator or publisher on Kaggle and is not redistributed with this project.
