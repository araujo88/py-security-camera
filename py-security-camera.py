import cv2
import time
import datetime

import smtplib, os
from email.message import EmailMessage

def send_email():
	msg = EmailMessage()
	msg.set_content('A face was detected in your security camera!')
	msg['Subject'] = f'Py-Security-Camera - Face detected'
	msg['From'] = 'sender@email.com' # enter sender email address here
	msg['To'] = 'recipient@email.com' # enter destinatary email address here

	email_user = os.environ.get('EMAIL_USER') # set EMAIL_USER as a system variable
	email_password = os.environ.get('EMAIL_PASSWORD') # set EMAIL_PASSWORD as a system variable
	server = smtplib.SMTP_SSL('smtp.email.com', 465) # secured connection - enter your smtp server here
	server.ehlo()
	server.login(email_user, email_password)
		
	server.send_message(msg)
	print("E-mail sent!")
	server.quit()


if __name__ == "__main__":

	cap = cv2.VideoCapture(0) # opens webcam

	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # face classifier

	frame_size = (int(cap.get(3)), int(cap.get(4))) # captures webcam frame size
	fourcc = cv2.VideoWriter_fourcc(*"mp4v") # video format

	detection = False
	detection_stopped_time = None
	timer_started = False
	SECONDS_TO_RECORD_AFTER_DETECTION = 5

	while True:
		_, frame = cap.read() # reads frame
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # new image with gray scale
		faces = face_cascade.detectMultiScale(gray, 1.3, 5) # scale factor = 1.3 (1.1, 1.5), number of faces = 5
		if len(faces) > 0:
			if detection:
				timer_started = False
			else:
				detection = True
				current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
				out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20.0, frame_size)
				print("Started recording!")
				send_email()
		elif detection:
			if timer_started:
				if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
					detection = False
					timer_started = False
					out.release()
					print("Stopped recording!")
			else:
				timer_started = True
				detection_stopped_time = time.time()
		if detection:
			out.write(frame) # writes frame

		cv2.imshow("Camera", frame) # displays frame

		if cv2.waitKey(1) == ord('q'): # exit key
			break

	out.release() # releases video capture
	cap.release() # release camera resources
	cv2.destroyAllWindows() # closes windows
