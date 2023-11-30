# Unmanned Ground Vehicle
# Overview
In the face of natural disasters or emergencies, the Disaster Management UGV aims to serve as a valuable tool for first responders. By automating the process of human detection, obstacle avoidance, and data storage, this project seeks to enhance the speed and efficiency of disaster response operations.The UGV a combination of sensors, computer vision algorithms, and autonomous navigation systems to operate seamlessly. 

# Features
## Autonomous Navigation: 
The Disaster Management UGV utilizes an integrated ultrasonic sensor for obstacle detection. This sensor emits ultrasonic sound waves, precisely measuring distances and identifying obstacles. The UGV dynamically adapts its path in real-time, ensuring efficient and safe movement through complex terrains.

## Human Detection: 
Utilizing computer vision techniques or YOLOv5 pre-trained model, the UGV achieves accurate and real-time identification of human presence in its surroundings.

## Obstacle Avoidance: 
The vehicle intelligently adapts its path by detecting and avoiding obstacles in real-time, ensuring it can traverse through dynamic environments.

## Database Integration: 
The UGV stores human detection data, including latitude and longitude coordinates, in a reliable database. Using the Python Geopy library, we convert these coordinates into easy-to-understand locations, enhancing the UGV's contribution to efficient disaster response efforts.

## Distance Measurement: 
The UGV utilizes its onboard camera to measure the distance between itself and detected humans, providing valuable insights for rescue planning.

# Hardware Requirements
Raspberry Pi 4<br />
HCSR04 Ultrasonic Sensor<br />
Neo 6m GPS Module<br />
L298N Motor Driver<br />
DC Motors<br />
Mecanum Wheels<br />
Battery (12V/3.5 Amp)<br />
Camera<br />
64GB memory card with reader<br />

# Software Requirements
Raspberry pi imager<br />
Raspberry Pi Operating System(64 bit)<br />
Python 3.11<br />
Putty<br />
Ip scanner<br />

# Installation
### Prepare the Raspberry Pi:
Insert the memory card into your laptop.
Download and install a 64-bit OS by Pi imager software onto the memory card.
### Configure Wi-Fi:
Create a Wi-Fi file with name "wpa_supplicant.conf" on the memory card (bootf) with SSID and password details.
Insert the memory card into the Raspberry Pi.
### Connect to Raspberry Pi:
Power up the Raspberry Pi and connect it to the same Wi-Fi hotspot as your laptop.
Use an IP scanner app to find the Raspberry Pi's IP address.
### Access via SSH:
Use Putty software to access the Raspberry Pi remotely via SSH.
Install xrdp on the Raspberry Pi by running sudo apt-get install xrdp in the Putty terminal.
### Enable Remote Connection:
Connect to the Raspberry Pi remotely by entering its IP address in the Remote Desktop Connection.
Ensure that both the Raspberry Pi and your laptop are connected to the same Wi-Fi hotspot.
### Configure Raspberry Pi:
Enable necessary configurations on the Raspberry Pi for the Disaster Management UGV.
### Set Up Virtual Environment and Install Required Packages:
Create a virtual environment on the Raspberry Pi by terminal for Python programming
Install the necessary Python packages for the Disaster Management UGV <br/>just run this command <br/>
pip install -r requirements.txt <br/>
Now, your Raspberry Pi is set up with a virtual environment, ready for Python programming with the required packages and ready to run the Disaster Management UGV.
# Configuration
Enable GPIO ,Serial SSH or Additional Configurations if required

# Pin Diagram
![Pin Diagram](https://github.com/lokesh074/Unmanned-ground-vehicle/raw/main/image/pin_diagram.jpg)

