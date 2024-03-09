import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
import segno
from flask import Flask, render_template
from flask_socketio import SocketIO,emit
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode
import base64
import time

app = Flask(__name__)
socketio = SocketIO(app)

cred = credentials.Certificate("..\\keys\\ticket-checker-9ed5c-firebase-adminsdk-kwtzc-f3749f5949.json")

firebase_admin.initialize_app(cred)

#text for the qrcode
qrcode=segno.make_qr("Hello World!")
#to save the qrcode locally with custsom size(scale), outside white area(border),light(change colour of white area),dark(change colour of dark area) 
qrcode.save("basic_qrcode.png",scale=5,border=1,light="goldenrod")

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
    
def find_ticket(number):
    doc_ref=db.collection('unique').document(number)
    doc=doc_ref.get()
    if doc.exists:  
        ticket_data=doc.to_dict()
        send_realtime_data(ticket_data["name"],ticket_data["class"])
    else:
        print("No such number")
    time.sleep(2)


@app.route('/')
def index():
    return render_template('home.html')

@socketio.on('stream')
def handle_stream(image_data):
    image = Image.open(BytesIO(base64.b64decode(image_data.split(',')[1])))  # Decode base64 image data
    decoded_objects = decode(image)

    for obj in decoded_objects:
        find_ticket(obj.data.decode('utf-8'))


def send_realtime_data(name,classname):
    # Generate or retrieve real-time data here
    data = {"name": name, "class": classname}  
    print("display")
    # Send data to client
    socketio.emit('realtime_data', data)
    # Adjust the interval as needed
    time.sleep(1)
        
# generate_ticket()
# find_ticket()

if __name__=="__main__":
    import threading
    threading.Thread(target=send_realtime_data,args=("John", "ClassA")).start()
    socketio.run(app, debug=True)