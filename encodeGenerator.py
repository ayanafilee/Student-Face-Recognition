import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# Firebase initialization
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceattendancerealtime-8e500-default-rtdb.firebaseio.com/',
    'storageBucket': 'faceattendancerealtime-8e500.appspot.com'
})

# Importing student images
folderPath = 'Images'
try:
    pathList = os.listdir(folderPath)
    print(f"Images found in folder: {pathList}")
except FileNotFoundError:
    print(f"Error: Folder '{folderPath}' not found. Ensure the folder exists and contains images.")
    pathList = []

imgList = []
studentIds = []
for path in pathList:
    try:
        img = cv2.imread(os.path.join(folderPath, path))
        if img is None:
            print(f"Error: Unable to read the image '{path}'. Skipping.")
            continue
        imgList.append(img)
        studentIds.append(os.path.splitext(path)[0])

        # Upload image to Firebase Storage
        fileName = f'Images/{path}'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(os.path.join(folderPath, path))
        print(f"Uploaded '{path}' to Firebase Storage.")
    except Exception as e:
        print(f"Error processing '{path}': {e}")

print(f"Student IDs: {studentIds}")

def findEncodings(imagesList):
    """
    Function to find face encodings for a list of images.
    """
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB for face_recognition
        try:
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        except IndexError:
            print("Warning: No face detected in one of the images. Skipping.")
    return encodeList

encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]

# Saving the encoding data to a file
with open('EncodeFile.p', 'wb') as file:
    pickle.dump(encodeListKnownWithIds, file)

print("Encoding Complete and File Saved")
