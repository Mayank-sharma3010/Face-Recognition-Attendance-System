import os
import cv2
from mtcnn import MTCNN

# Initialize MTCNN detector
detector = MTCNN()

# Input and Output folders
RAW_DATASET = "dataset/raw"
PROCESSED_DATASET = "dataset/processed"

# Create processed folder if not exists
os.makedirs(PROCESSED_DATASET, exist_ok=True)

# Read all student folders
students = os.listdir(RAW_DATASET)

for student in students:

    student_raw_path = os.path.join(RAW_DATASET, student)
    student_processed_path = os.path.join(PROCESSED_DATASET, student)

    os.makedirs(student_processed_path, exist_ok=True)

    print(f"\nProcessing : {student}")

    images = os.listdir(student_raw_path)

    count = 0

    for image_name in images:

        image_path = os.path.join(student_raw_path, image_name)

        image = cv2.imread(image_path)

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        faces = detector.detect_faces(rgb)

        if len(faces) == 0:
            continue

        x, y, w, h = faces[0]['box']

        x = max(0, x)
        y = max(0, y)

        face = image[y:y+h, x:x+w]

        face = cv2.resize(face, (160,160))

        save_path = os.path.join(student_processed_path, image_name)

        cv2.imwrite(save_path, face)

        count += 1

    print(f"Saved {count} processed images.")