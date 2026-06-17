from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("model.pkl")

# Load dataset
df = pd.read_excel("attendance.xlsx")

attendance_columns = [col for col in df.columns if "Day_" in col]

df["Present_Sessions"] = (df[attendance_columns] >= 90).sum(axis=1)

df["Absent_Sessions"] = len(attendance_columns) - df["Present_Sessions"]

df["Attendance_Percentage"] = (
    df["Present_Sessions"] / len(attendance_columns)
) * 100


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():

    gmail = request.form["gmail"]

    student = df[
        df["Gmail_ID"].astype(str).str.lower()
        == gmail.lower()
    ]

    if student.empty:
        return render_template(
            "result.html",
            found=False
        )

    student = student.iloc[0]

    features = [[
        student["Present_Sessions"],
        student["Absent_Sessions"],
        student["Attendance_Percentage"]
    ]]

    prediction = model.predict(features)[0]

    eligibility = (
        "Eligible ✅"
        if prediction == 1
        else "Not Eligible ❌"
    )

    return render_template(
        "result.html",
        found=True,
        name=student["Name"],
        gmail=student["Gmail_ID"],
        college=student["College (if mentioned)"],
        attendance=round(
            student["Attendance_Percentage"], 2
        ),
        present=student["Present_Sessions"],
        absent=student["Absent_Sessions"],
        eligibility=eligibility
    )


if __name__ == "__main__":
    app.run(debug=True)