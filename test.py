import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random

cred = credentials.Certificate("..\\keys\\ticket-checker-9ed5c-firebase-adminsdk-kwtzc-f3749f5949.json")

firebase_admin.initialize_app(cred)

db = firestore.client()
data={
    'test' : 'checking2'
}

doc_ref=db.collection('unique').document('thousand')
doc_ref.set(data)
def generate_ticket():
    looping=True
    while looping:
        random_gen=random.randrange(1,10)
        print(random_gen)
        doc_ref=db.collection('unique').document(str(random_gen))
        doc=doc_ref.get()
        if doc.exists:
            looping=True
        else:
            print("entered")
            looping=False
    data={
        'name' : 'Vishnu',
        'class' : 's6cs1',
        'phno' : '1234567890'
    }
    doc_ref.set(data)
    print("Added value ",random_gen)
    
def find_ticket():
    number="8"
    doc_ref=db.collection('unique').document(number)
    doc=doc_ref.get()
    if doc.exists:  
        print(doc.to_dict())
    else:
        print("No such number")

generate_ticket()
find_ticket()
# doc_ref=db.collection('test').document('third')
# doc_ref.set(data)
# print(doc_ref.id)
# doc_ref=db.collection('test').document('first')
# doc=doc_ref.get()
# print(doc.to_dict())
