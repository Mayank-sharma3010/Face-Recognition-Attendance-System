import cv2
import numpy as np
import csv
import os
from datetime import datetime
from mtcnn import MTCNN
from keras_facenet import FaceNet

# ==========================
# Load FaceNet & MTCNN
# ==========================
embedder = FaceNet()
detector = MTCNN()

# ==========================
# Load Saved Embeddings
# ==========================
known_embeddings = np.load(
    "dataset/embeddings/embeddings.npy",
    allow_pickle=True
).astype(np.float32)

known_labels = np.load(
    "dataset/embeddings/labels.npy",
    allow_pickle=True
)

# ==========================
# Attendance File
# ==========================
ATTENDANCE_FILE = "attendance/attendance.csv"

os.makedirs("attendance", exist_ok=True)

# Create attendance file if it doesn't exist
if not os.path.exists(ATTENDANCE_FILE):
    with open(ATTENDANCE_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time"])


# ==========================
# Attendance Function
# ==========================
def mark_attendance(name):

    today = datetime.now().strftime("%d-%m-%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    already_present = False

    with open(ATTENDANCE_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) >= 2:
                if row[0] == name and row[1] == today:
                    already_present = True
                    break

    if not already_present:
        with open(ATTENDANCE_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, today, current_time])

        print(f"{name} Attendance Marked")


# ==========================
# Face Recognition Function
# ==========================
def recognize_face(face):

    rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
    rgb = rgb.astype(np.float32)

    # FaceNet Normalization
    

    rgb = np.expand_dims(rgb, axis=0)

    embedding = embedder.embeddings(rgb)[0]

    distances = []

    for emb in known_embeddings:
        distance = np.linalg.norm(embedding - emb)
        distances.append(distance)

    min_index = np.argmin(distances)
    min_distance = distances[min_index]

    # ==========================
    # Print Distance
    # ==========================
    print("Distance =", round(min_distance, 3))

    # Recognition Threshold
    threshold = 1.35

    if min_distance < threshold:
        return known_labels[min_index]

    return "Unknown"


# ==========================
# Open Webcam
# ==========================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not found!")
    exit()

print("Press ESC to Exit")

# ==========================
# Main Loop
# ==========================
while True:

    ret, frame = cap.read()

    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = detector.detect_faces(rgb)

    for face in faces:

        x, y, w, h = face["box"]

        # Prevent negative coordinates
        x = max(0, x)
        y = max(0, y)

        x2 = x + w
        y2 = y + h

        crop = frame[y:y2, x:x2]

        if crop.size == 0:
            continue

        try:
            crop = cv2.resize(crop, (160, 160))
        except:
            continue

        crop = crop.astype(np.float32)

        # Recognize Face
        name = recognize_face(crop)

        if name != "Unknown":
            color = (0, 255, 0)
            mark_attendance(name)
        else:
            color = (0, 0, 255)

        # Draw Rectangle
        cv2.rectangle(frame, (x, y), (x2, y2), color, 2)

        # Show Name
        cv2.putText(
            frame,
            str(name),
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

    cv2.imshow("AI Face Attendance System", frame)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# ==========================
# Release Resources
# ==========================
cap.release()
cv2.destroyAllWindows()