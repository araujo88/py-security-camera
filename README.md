# py-security-camera
A simple security camera written in Python which starts recording when a face is detected and warns the user by e-mail using the Python library OpenCV.

## Installation and settings
Install requirements:
  - ```pip install -r requirements.txt``` (Windows)
  - ```pip3 install -r requirements.txt``` (Linux/macOS)

Configure settings:
  - Set ```EMAIL_USER``` and ```EMAIL_PASSWORD``` as system variables
  - Substitute ```sender@email.com```, ```recipient@email.com``` and ```smtp.email.com``` in the ```py-security-camera.py``` file with your sender and destinatary e-mails and your e-mail provider. Make sure to use SMTPS (secured SMTP).

## Usage
Run the program with:
 - ```python py-security-camera.py``` (Windows)
 - ```python3 py-security-camera.py``` (Linux/macOS)

 When the program is running, the webcam is turned on and cannot be used by other applications. It starts recording whenever a face is detected by the camera and sends an e-mail warning to the preconfigured e-mail setting. 
 
 It stops recording 5 seconds after no face is being detected on screen. This 5 seconds setting can be modified by altering the variable ```SECONDS_TO_RECORD_AFTER_DETECTION```.
 
 The application can be exited by pressing ```q```.
