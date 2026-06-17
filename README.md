# Smart Attendance & Certificate Eligibility System

## 📌 Project Overview

The **Smart Attendance & Certificate Eligibility System** is a Machine Learning and Flask-based web application developed to manage and analyze student attendance records for online training sessions.

The system allows users to search for a student using their Gmail ID and instantly view:

* Student Name
* Gmail ID
* College Name
* Attendance Percentage
* Present Sessions
* Absent Sessions
* Certificate Eligibility Status

The project processes attendance data from an Excel dataset containing records of 980+ students attending online sessions.

---

## 🎯 Problem Statement

Managing attendance for a large number of students is challenging and time-consuming.

This project automates:

* Attendance calculation
* Present/Absent classification
* Attendance percentage calculation
* Certificate eligibility verification
* Student information retrieval

---

## 📊 Attendance Rules

| Condition             | Status  |
| --------------------- | ------- |
| Duration ≥ 90 Minutes | Present |
| Duration < 90 Minutes | Absent  |

### Session Information

* Total Students: 980+
* Total Sessions: 45
* Session Duration: 120 Minutes

### Certificate Eligibility

A student is eligible for certification if:

Attendance Percentage ≥ 80%

---

## 🤖 Machine Learning Component

The project uses a **Random Forest Classifier** to predict certificate eligibility based on attendance metrics.

### Features Used

* Present Sessions
* Absent Sessions
* Attendance Percentage

### Target Variable

* Eligible (1)
* Not Eligible (0)

---

## 🛠️ Technologies Used

### Frontend

* HTML
* CSS

### Backend

* Python
* Flask

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* Random Forest Classifier

### Dataset

* Excel (.xlsx)

---

## 📂 Project Structure

Attendance_System/

├── app.py

├── attendance.xlsx

├── model.pkl

├── train_model.py

├── templates/

│ ├── index.html

│ └── result.html

├── static/

│ └── style.css

└── README.md

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Attendance-System.git

cd Attendance-System
```

### Install Dependencies

```bash
pip install flask pandas scikit-learn openpyxl joblib
```

---

## 🚀 Running the Project

### Step 1: Train Model

```bash
python train_model.py
```

This creates:

```text
model.pkl
```

### Step 2: Start Flask Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```


## 🔍 How It Works

1. User enters a Gmail ID.
2. System searches the Excel dataset.
3. Attendance percentage is calculated.
4. Machine Learning model predicts eligibility.
5. Student details are displayed on a separate results page.


## 📈 Sample Output

Student Name: Rahul Kumar

College: ABC Engineering College

Attendance Percentage: 86.67%

Present Sessions: 39

Absent Sessions: 6

Certificate Eligibility: Eligible ✅


## 🌟 Features

* Gmail-based student search
* Attendance percentage calculation
* Automatic eligibility checking
* Machine Learning prediction
* User-friendly interface
* Excel dataset support
* Fast student lookup

## 🔮 Future Enhancements

* Admin Login System
* Dashboard Analytics
* Attendance Charts & Graphs
* PDF Report Generation
* Email Notifications
* Database Integration (MySQL)
* Cloud Deployment

## 👨‍💻 Author

Jagadeesh Tungala

B.Tech – Artificial Intelligence & Machine Learning

Vasireddy Venkatadri Institute of Technology (VVIT)


## 📜 License

This project is developed for educational and academic purposes.



**OUTPUT**
<img width="1920" height="1020" alt="Screenshot 2026-06-17 113806" src="https://github.com/user-attachments/assets/3aa86c73-5d25-40dc-8998-d8724832ac50" />
<img width="1920" height="1020" alt="Screenshot 2026-06-17 113816" src="https://github.com/user-attachments/assets/57e57517-9db3-41a7-a667-ecbe040ae7e8" />

