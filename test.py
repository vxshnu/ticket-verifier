import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("ticket-checker-9ed5c-firebase-adminsdk-kwtzc-f3749f5949.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
data={
    'test' : 'checking'
}
doc_ref=db.collection('test').document()
doc_ref.set(data)
print(doc_ref.id)