import serial
import pynmea2
from geopy.geocoders import Nominatim
import database
from database import *
import model
geolocator = Nominatim(user_agent="geoapiExercises")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

while True:
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()
        n_data = newdata.decode('latin-1')
        if n_data[0:6] == '$GPRMC':
                newmsg=pynmea2.parse(n_data)
                lat=newmsg.latitude
                lng=newmsg.longitude
                gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
                print(gps)
                location = geolocator.geocode(str(lat)+","+str(lng))
                # Display location
                print("\nLocation of the given Latitude and Longitude:")
                print(location)
                
                new_location = model.Location(location=str(location),latitude= str(lat),longitude = str(lng), is_human=True)  # Modify with your data
                session.add(new_location)
                session.commit()
                session.close()
