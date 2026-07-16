import tkinter as tk
import subprocess
import os
import sys


class Dashboard:

    def __init__(self, root):

        self.root = root
        self.root.title("Face Recognition Attendance System")
        self.root.geometry("900x600")
        self.root.configure(bg="#F4F6F7")

        title = tk.Label(
            root,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Arial", 20, "bold"),
            bg="#2C3E50",
            fg="white",
            pady=15
        )
        title.pack(fill="x")

        # Register Student
        btn1 = tk.Button(
            root,
            text="Register Student",
            font=("Arial", 14),
            width=25,
            height=2,
            command=self.register_student
        )
        btn1.pack(pady=15)

        # Train Model
        btn2 = tk.Button(
            root,
            text="Train Model",
            font=("Arial", 14),
            width=25,
            height=2,
            command=self.train_model
        )
        btn2.pack(pady=15)

        # Take Attendance
        btn3 = tk.Button(
            root,
            text="Take Attendance",
            font=("Arial", 14),
            width=25,
            height=2,
            command=self.take_attendance
        )
        btn3.pack(pady=15)

        # View Attendance
        btn4 = tk.Button(
            root,
            text="View Attendance",
            font=("Arial", 14),
            width=25,
            height=2,
            command=self.view_attendance
        )
        btn4.pack(pady=15)

    # -----------------------------
    # Register Student
    # -----------------------------
    def register_student(self):
        subprocess.Popen([sys.executable, "src/collect_images.py"])

    # -----------------------------
    # Train Model
    # -----------------------------
    def train_model(self):
        subprocess.Popen([sys.executable, "src/train_model.py"])

    # -----------------------------
    # Take Attendance
    # -----------------------------
    def take_attendance(self):
        subprocess.Popen([sys.executable, "src/recognize.py"])

    # -----------------------------
    # View Attendance
    # -----------------------------
    def view_attendance(self):

        file_path = os.path.join(os.getcwd(), "attendance", "attendance.csv")

        if os.path.exists(file_path):
            os.startfile(file_path)
        else:
            print("Attendance file not found.")