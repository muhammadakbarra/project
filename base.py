
import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase


cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
firebaseConfig = {
    'apiKey': "AIzaSyBTd-PWg3Cm3G8qhSEFSGuOyXF7soW_M7o",
    'authDomain': "strength-b5e40.firebaseapp.com",
    'databaseURL': "https://strength-b5e40-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "strength-b5e40",
    'storageBucket': "strength-b5e40.appspot.com",
    'messagingSenderId': "558293525072",
    'appId': "1:558293525072:web:42346561a2c55ab73a2755"
}
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()


def get_all_collection(collection, orderBy=None, direction=None):
    if orderBy:
        collects_ref = db.collection(collection).order_by(
            orderBy, direction=direction)
    else:
        collects_ref = db.collection(collection)
    collects = collects_ref.stream()
    RETURN = []
    for collect in collects:
        ret = collect.to_dict()
        ret['id'] = collect.id
        RETURN.append(ret)
    return RETURN
