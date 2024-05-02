# ©2023 PyJs

import os
try:
    import cv2
except:
    os.system("pip3 install opencv-python")
    import cv2
print("THIS USES CV2. RUN \"pip uninstall opencv-python\" TO UNINSTALL.")
# Initialize a list to store enrolled faces
enrolled_faces = []

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def scan_face():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    return frame

def enroll_face():
    frame=scan_face()
    global enrolled_faces

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            # Crop and store each enrolled face
            enrolled_faces.append(frame[y:y+h, x:x+w])

        return True
    else:
        return False

# Function to match a face
def is_match():
    global enrolled_faces
    frame=scan_face()
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            # Crop the detected face for comparison
            detected_face = frame[y:y+h, x:x+w]

            # Check if the detected face matches any of the enrolled faces
            for enrolled_face in enrolled_faces:
                if reuowg_w(enrolled_face, detected_face):
                    return True

    return False

# Function to compare faces (a basic image comparison)
def reuowg_w(face1, face2):
    # Resize the images to the same size
    face1 = cv2.resize(face1, (200, 200))
    face2 = cv2.resize(face2, (200, 200))
    diff = cv2.absdiff(face1, face2)
    mean_diff = diff.mean()
    return mean_diff < 50