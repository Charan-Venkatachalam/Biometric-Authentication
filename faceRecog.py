#pip install face_recognition
import face_recognition
import cv2

# Load images with faces
image_of_person = face_recognition.load_image_file("person.jpg")
image_of_unknown = face_recognition.load_image_file("unknown.jpg")

# Find face encodings
person_encoding = face_recognition.face_encodings(image_of_person)[0]
unknown_encoding = face_recognition.face_encodings(image_of_unknown)[0]

# Compare the face encodings
results = face_recognition.compare_faces([person_encoding], unknown_encoding)

if results[0]:
    print("Authentication successful: Faces match!")
else:
    print("Authentication failed: Faces do not match!")
