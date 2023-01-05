import cv2
import numpy as np
import sqlite3
import os 

def insertandupdate(id,password):
	con = sqlite3.connect('D:\\python\\pjck\\gdata.db')
	query = 'SELECT * FROM customer WHERE id=' +str(id)
	cusror = con.execute(query)

	isRecordExist = 0

	for row in cusror:
		isRecordExist = 1
	if(isRecordExist==0):
		query = "INSERT INTO customer(id, password) VALUES("+str(id)+",'"+str(password)+"')"
	else:
		query = "UPDATE customer SET password='"+str(password)+"'WHERE id ="+str(id)
	con.execute(query)
	con.commit()
	con.close()


