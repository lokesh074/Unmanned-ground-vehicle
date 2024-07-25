import cv2
import torch
import numpy as np
from imutils.video import VideoStream

import serial
import pynmea2
from geopy.geocoders import Nominatim
import database
from database import *
from model import *
geolocator = Nominatim(user_agent="geoapiExercises")



def loc():
    print("running")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    location=""
    status = True
    while status:
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()
        n_data = newdata.decode('latin-1')
        if n_data[0:6] == '$GPRMC':
                print("location found")
                status= False
                newmsg=pynmea2.parse(n_data)
                lat=newmsg.latitude
                lng=newmsg.longitude
                gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
                print(gps)
                location = geolocator.geocode(str(lat)+","+str(lng))
                # Display location
                print("\nLocation of the given Latitude and Longitude:")
                print(location)
                new_location = Location(location=str(location),latitude= str(lat),longitude = str(lng), is_human=True)  # Modify with your data
                session.add(new_location)
                session.commit()
                session.close()
                return True
 

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

cap = cv2.VideoCapture(0)
focal_length = 800  # Focal length in pixels
object_height = 1.65  # Average human height in meters
gps_location= False

def calculate_distance(bbox_height):
    distance = (focal_length * object_height) / bbox_height
    return distance

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = model(frame)
    pred = results.pred[0]
    for det in pred:
        label, conf, bbox = det[5], det[4], det[:4]
        if label == 0 and conf>=0.60:  # class index 0 corresponds to humans
            gps_location = loc()
            if gps_location:
                print("gps location has been inserted",gps_location)
            x1, y1, x2, y2 = map(int, bbox)
            obj_width = x2-x1
            bbox_height = y2 - y1
            distance = calculate_distance(bbox_height)
            print("Distance: ",round(distance)," Meter")
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, f'Human: {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(img, f'Distance: {distance:.2f} m', (x1, y1 - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255
                                                                                                                  ), 2)                                                                                                     

    cv2.imshow('Human Detection', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
