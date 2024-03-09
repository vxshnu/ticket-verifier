import segno
import cv2
#text for the qrcode
qrcode=segno.make_qr("Hello World!")
#to save the qrcode locally with custsom size(scale), outside white area(border),light(change colour of white area),dark(change colour of dark area) 
qrcode.save("basic_qrcode.png",scale=5,border=1,light="goldenrod")
#To start the camera for capturing the qrcode
cap=cv2.VideoCapture(0)
#to caputre the qrcode real-time
detector=cv2.QRCodeDetector()
#to read the webcam continuously
webpage_opened = False
prev=None
while True: 
    _, img = cap.read()
    #detects if a qr code appears in the webcam and then procedes to decode it and and store various values into data, bbox and no needed values('_')
    data, bbox, _ = detector.detectAndDecode(img) 
    cv2.imshow("QRCODEscanner", img) 
    #checks if a qr code exists
    if data and prev!=data:
        prev=data
        print(data)
        continue
    # '/' will be used as the exit key
    if cv2.waitKey(1) == ord("/"): 
        break
cap.release() 
cv2.destroyAllWindows()
    