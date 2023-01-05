import cv2
import numpy as np
import os 
from PIL import Image 

recognizer = cv2.face.LBPHFaceRecognizer_create()

path='D:\\python\\pjck\\datafile'

def getImagewithid(path):
	imagepaths = [os.path.join(path,f) for f in os.listdir(path)]

	faces=[]
	ids=[]
	

	for imagepath in imagepaths:
		faceimg= Image.open(imagepath).convert('L')
		faceNp =np.array(faceimg,'uint8')
		
		Id=int(imagepath.split('\\')[4].split('.')[1])
		

		faces.append(faceNp)
		ids.append(Id)

		cv2.imshow('sss',faceNp)
		cv2.waitKey(10)
	return faces,ids
def train():
	faces,ids =getImagewithid(path)

	recognizer.train(faces, np.array(ids))

	if not os.path.exists('D:\\python\\pjck\\recognizer'):
		os.makedirs('D:\\python\\pjck\\recognizer')

	recognizer.save('D:\\python\\pjck\\recognizer\\traimd.yml')

	cv2.destroyAllWindows()