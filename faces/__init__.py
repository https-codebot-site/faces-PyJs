import cv2
# Initialize a list to store enrolled faces
enrolled_faces = []

class dont_run:
    def compare_faces(face1, face2):
        # Resize the images to the same size
        face1 = cv2.resize(face1, (200, 200))
        face2 = cv2.resize(face2, (200, 200))
        diff = cv2.absdiff(face1, face2)
        mean_diff = diff.mean()
        return mean_diff < 50
    def scan_face():
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        return frame
    def is_match(frame):
        global enrolled_faces

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
                    if dont_run.compare_faces(enrolled_face, detected_face):
                        return (True, "That's a match!")

        return (False, "Not matched.")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def enroll_face(frame=dont_run.scan_face()):
    global enrolled_faces

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            # Crop and store each enrolled face
            enrolled_faces.append(frame[y:y+h, x:x+w])

        return (True, f"success!✅ {len(faces)} are currently saved.")
    else:
        return (False, "No face found in the frame.😞")

def match_face():
    frame = dont_run.scan_face()
    return dont_run.is_match(frame)
__version__="0.1.0"#---------------------------------------------CHANGE THIS---------------------------------------------#