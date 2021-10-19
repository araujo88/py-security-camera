# py-security-camera
A simple security camera written in Python which starts recording when a face is detected and warns the user by e-mail.

## Usage
Install requirements:
  - ```pip install -r requirements.txt``` (Windows)
  - ```pip3 install -r requirements.txt``` (Linux/macOS)

Configure settings:
  - Set ```EMAIL_USER``` and ```EMAIL_PASSWORD``` as system variables
  - Substitute ```sender@email.com```, ```recipient@email.com``` and ```smtp.email.com``` in the ```py-security-camera.py``` file with your sender and destinatary e-mails and your e-mail provider. Be sure to use SMTPS (secured SMTPS).