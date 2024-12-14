import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/hp user/PycharmProjects/AI Project/serviceAccountKey.json")

firebase_admin.initialize_app(cred,
                              {'databaseURL': 'https://faceattendancerealtime-8e500-default-rtdb.firebaseio.com/'})

ref = db.reference('Students')


data = {

    "46578":
        {
            "name": "Tedros",
            "major": "WHO Director",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "87690":
        {
            "name": "Amanuel",
            "major": "SWE",
            "starting_year": 2024,
            "total_attendance": 6,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "43277":
        {
            "name": "Abdi ",
            "major": "SOftware",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"

    },

    "56733":
        {
            "name": "Jawar",
            "major": "politician",
             "starting_year": 2024,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "34767":
        {
            "name": "Abiy",
            "major": "Prime minister",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
