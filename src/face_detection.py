import cv2

# Load Face Detection Model
face_cascade = cv2.CascadeClassifier(
    "models/haarcascade_frontalface_default.xml"
)

# Open Webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not found!")
    exit()

while True:

    ret, frame = camera.read()

    if not ret:
        break

    # Convert image to Gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    # Draw Rectangle
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0,255,0),
            2
        )

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()