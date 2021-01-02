import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

# Scan From VideoCamera
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        x = obj.data
        print('QRCode Data: ', obj.data)

    if len(decodedObjects) != 0:
        break

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key==27:
        break



