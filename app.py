from flask import Flask, render_template

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


@app.route("/register")
def register():
    return "Register Student Page - Coming Next"


@app.route("/attendance")
def attendance():
    return "Take Attendance Page - Coming Next"


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