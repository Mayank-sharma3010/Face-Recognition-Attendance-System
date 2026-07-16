import subprocess
import sys
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        total_students=0,
        present_today=0,
        absent_today=0,
        attendance_rate=0,
        recent_attendance=[]
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        student_id = request.form.get("student_id")
        course = request.form.get("course")
        semester = request.form.get("semester")

        print("Name:", name)
        print("Student ID:", student_id)
        print("Course:", course)
        print("Semester:", semester)

        return f"Student {name} registered successfully!"

    return render_template("register.html")


@app.route("/attendance")
def attendance():
    subprocess.Popen([
        sys.executable,
        "src/recognize.py"
    ])

    return """
    <h1>Face Recognition Started</h1>
    <p>Camera should open in a separate window.</p>
    <p>Press ESC in the camera window to stop attendance.</p>
    <a href="/">Back to Dashboard</a>
    """


@app.route("/students")
def students():
    return "Students Page - Coming Next"


@app.route("/records")
def records():
    return "Attendance Records Page - Coming Next"


@app.route("/reports")
def reports():
    return "Reports Page - Coming Next"


if __name__ == "__main__":
    app.run(debug=True)
