import os
import cv2
import numpy as np
from keras_facenet import FaceNet

# Load FaceNet model
embedder = FaceNet()

# Dataset path
DATASET_PATH = "dataset/processed"

embeddings = []
labels = []

# Read all student folders
students = os.listdir(DATASET_PATH)

for student in students:

    student_path = os.path.join(DATASET_PATH, student)

    images = os.listdir(student_path)

    print(f"\nProcessing {student}...")

    for image_name in images:

        image_path = os.path.join(student_path, image_name)

        image = cv2.imread(image_path)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = image.astype("float32")

        image = np.expand_dims(image, axis=0)

        embedding = embedder.embeddings(image)

        embeddings.append(embedding[0])

        labels.append(student)

print("\nSaving Embeddings...")

os.makedirs("dataset/embeddings", exist_ok=True)

np.save("dataset/embeddings/embeddings.npy", embeddings)

np.save("dataset/embeddings/labels.npy", labels)

print("Embeddings Saved Successfully!")