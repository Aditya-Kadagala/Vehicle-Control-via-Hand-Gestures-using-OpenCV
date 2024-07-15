# Vehicle-Control-via-Hand-Gestures-using-OpenCV

# Description:

This project focuses on remote vehicle control using OpenCV technology. The vehicle is controlled through hand gestures, which are captured and transmitted to the vehicle. The microcontroller decodes these commands and executes the corresponding actions.

Arduino modules are employed for vehicle control. Additionally, IR sensors are integrated for obstacle detection. If an object is detected in the vehicle's path, the system automatically halts the vehicle to prevent collisions.

# Steps to follow:

1. Connect everything according to the circuit diagram.
2. Save your Python (.py) files in your folder.
3. Connect the Arduino to your PC or laptop.
4. Choose the device name and port, and upload the Arduino code.
	4.1 Open Arduino IDE
	4.2 Click on File -> Examples -> Firmata -> StandardFirmata
	4.3 Upload the code into Arduino
	* Note: Make sure the relay module is not powered while uploading the code.
5. Update the COM port in the control2.py file.
6. Run the control2.py file.
7. Run the main.py file, a window will open.
8. Now connect the power supply to the relay.
9. Show your hand gestures in front of the laptop camera; you will see it in the window.
10. Press 'q' to close the window.
