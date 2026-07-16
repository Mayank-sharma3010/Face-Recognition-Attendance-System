import cv2
import os

# Student name
student_name = input("Enter Student Name: ")

# Folder path
folder_path = os.path.join("dataset", "raw", student_name)

# Create folder if not exists
os.makedirs(folder_path, exist_ok=True)

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not found!")
    exit()

count = 0

print("\nPress 'S' to save image")
print("Press 'Q' to quit\n")

while True:

    ret, frame = camera.read()

    if not ret:
        break

    cv2.imshow("Collect Images", frame)

    key = cv2.waitKey(1)

    # Save Image
    if key == ord('s'):

        count += 1

        image_path = os.path.join(folder_path, f"image_{count}.jpg")

        cv2.imwrite(image_path, frame)

        print(f"Saved: {image_path}")

    # Quit
    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

print(f"\nTotal Images Saved : {count}")