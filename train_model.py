import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_excel("attendance.xlsx")

attendance_columns = [
    col for col in df.columns
    if "Day_" in col
]

df["Present_Sessions"] = (
    df[attendance_columns] >= 90
).sum(axis=1)

df["Absent_Sessions"] = (
    len(attendance_columns)
    - df["Present_Sessions"]
)

df["Attendance_Percentage"] = (
    df["Present_Sessions"]
    / len(attendance_columns)
) * 100

df["Eligible"] = (
    df["Attendance_Percentage"] >= 80
).astype(int)

X = df[
    [
        "Present_Sessions",
        "Absent_Sessions",
        "Attendance_Percentage"
    ]
]

y = df["Eligible"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print(
    "Accuracy:",
    accuracy_score(y_test, pred)
)

joblib.dump(model, "model.pkl")

print("Model Saved Successfully")