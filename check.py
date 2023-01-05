import cv2
import numpy as np
import os
import sqlite3
import b
import sys
from PIL import Image
from tkinter import *

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('D:\\python\\pjck\\recognizer\\traimd.yml')

def getProfile(id):
	con = sqlite3.connect('D:\\python\\pjck\\gdata.db')
	query = 'SELECT * FROM customer WHERE id=' +str(id)
	cusror = con.execute(query)

	profile =None

	for row in cusror:
		profile=row 
	con.close()
	return profile
cap =cv2.VideoCapture(0)
fontface=cv2.FONT_HERSHEY_SIMPLEX
def run():
	running=True
	while running:
		ret, frame= cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray)
		for (x,y,h,w) in faces:
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,225,0),2)
			cut_gray=gray[y:y+h,x:x+w]
			id,confidence = recognizer.predict(cut_gray)

			if confidence<60:
				profile = getProfile(id)
				if profile!=None:
					win=Tk()
					b.window2(win)
					sys.exit()
					running=False
			else:
				cv2.putText(frame,'unknow,press x to exit', (x+10,y+h+30),fontface,1,(0,0,255),2)
		cv2.imshow('CHECKING',frame)
		if cv2.waitKey(1)==ord('x'):
			break
run()
cap.release()
cv2.destroyAllWindows()