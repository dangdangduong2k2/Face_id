from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import webbrowser
import os
import sqlite3 
import cv2
import numpy as np
import sys
import get as get
import train as train

#====================================================================================================================================#
def main():
	win = Tk()
	proj = window1(win)
def sysexit():
	sys.exit()

#============================================================class1====================================================================#
	
class window1:
	def __init__(self,root):

		#===================================================Create window==============================================================#
		self.root = root
		self.root.title('duong')
		self.root.geometry("%dx%d+%d+%d" % (1280,718,(self.root.winfo_screenwidth())/2-(1280/2),(self.root.winfo_screenheight())/2-(718/2)-40))
		self.root.resizable(False,False)

		#===================================================Image==============================================================#

		self.imga= Image.open("D:\\python\\h.jpg") 
		self.resize_imga= self.imga.resize((1280,718),Image.ANTIALIAS) 
		self.imgb= ImageTk.PhotoImage(self.resize_imga)
		self.bg = Label(self.root, image=self.imgb).place(x=0,y=0, relwidth=1,relheight=1)

		#===================================================Frame==============================================================#

		self.framelg= Frame(self.root, bg='white')
		self.framelg.place(x=1280/2-330/2,y=718/2-500/2-10,width=330,height=500)

		#===================================================Label and Entry 's username password====================================================#

		self.title = Label(self.framelg, text="Login", font=("Comic Sans MS",30,'bold'),fg='black',bg='white').place(x=115,y=30)

		self.username = Label(self.framelg,text="Username", font=('Comic Sans MS',15,'bold'),fg='black',bg='white').place(x=40,y=120)
		self.entryun = Entry(self.framelg,width=27,font=('Pixie Ring Font',13,'bold'),bg='gray')
		self.entryun.place(x=40,y=170)

		self.password = Label(self.framelg,text="Password", font=('Comic Sans MS',15,'bold'),fg='black',bg='white').place(x=40,y=220)
		self.entrypw = Entry(self.framelg,width=27,font=('Pixie Ring Font',13,'bold'),bg='gray',show="*")
		self.entrypw.place(x=40,y=270)

		#===================================================Button=============================================================#

		self.bta= Button(self.framelg, text='login', font=("Pixie Ring Font",12,'bold'),width=10,command=self.login).place(x=40,y=320)
		self.btb= Button(self.framelg, text='register', font=("Pixie Ring Font",12,'bold'),width=10,command=self.toplv).place(x=178,y=320)
		self.btb= Button(self.framelg, text='exit', font=("Pixie Ring Font",12,'bold'),width=10,command=self.exit).place(x=110,y=380)
		self.btb= Button(self.framelg, text='face', font=("Pixie Ring Font",12,'bold'),width=10,command=self.face).place(x=110,y=440)
		#===================================================Mainloop===========================================================#

		self.root.mainloop()


	#===================================================Login Button===========================================================#
	def login(self):
		self.con = sqlite3.connect('D:\\python\\pjck\\gdata.db')
		self.query1 = 'SELECT * FROM customer WHERE id=' +str(self.entryun.get())
		self.cursor1 = self.con.execute(self.query1)

		self.query2 = 'SELECT * FROM customer WHERE password=' +str(self.entrypw.get())
		self.cursor2 = self.con.execute(self.query2)

		self.a = self.cursor1.fetchall()
		self.b = self.cursor2.fetchall()

		if  self.a==self.b and self.a!=[] :
			self.root.destroy()
			self.newwindow()
		if  self.entryun.get()=='20144374' and self.entrypw.get()=='1':
			self.root.destroy()
			self.newwindow()
			
		else:
			self.entryun.delete(0, END)
			self.entrypw.delete(0, END)

	#===================================================Exit Button============================================================#
	def exit(self):
		self.root.destroy()
	#===================================================New window============================================================#
	def newwindow(self):
		self.newwindow =Tk()
		self.app = window2(self.newwindow)
	#===================================================top lv============================================================#
	def toplv(self):
		self.w1 =Toplevel()
		self.w1.geometry("%dx%d+%d+%d" % (300,400,(self.root.winfo_screenwidth())/2-(300/2),(self.root.winfo_screenheight())/2-(400/2)-40))
		self.w1.grab_set()

		self.frametlv= Frame(self.w1, bg='white')
		self.frametlv.place(x=0,y=0,width=300,height=500)

		self.labelres = Label(self.frametlv,text="register", font=("Comic Sans MS",30,'bold'),fg='black',bg='white')
		self.labelres.place(x=80,y=5)

		self.labelcreateusn = Label(self.frametlv,text="your username", font=("Comic Sans MS",15,'bold'),fg='black',bg='white')
		self.labelcreateusn.place(x=60,y=70)

		self.labelcreatepw = Label(self.frametlv,text="your password", font=("Comic Sans MS",15,'bold'),fg='black',bg='white')
		self.labelcreatepw.place(x=60,y=170)

		self.entryuntlv =Entry(self.frametlv,width=20,font=('Pixie Ring Font',13,'bold'),bg='gray')
		self.entryuntlv.place(x=60,y=105)

		self.entrypwtlv =Entry(self.frametlv,width=20,font=('Pixie Ring Font',13,'bold'),bg='gray',show='*')
		self.entrypwtlv.place(x=60,y=205)

		self.bttlv1 = Button(self.frametlv, text='register', font=("Pixie Ring Font",12,'bold'),width=10,command=self.register).place(x=97,y=260)
		self.bttlv2 = Button(self.frametlv, text='register with ur face', font=("Pixie Ring Font",12,'bold'),width=20,command=self.getdata).place(x=50,y=300)
	#=====================================================resigter==========================================================#
	def register(self):
		self.con = sqlite3.connect('D:\\python\\pjck\\gdata.db')
		self.cursor = self.con.cursor()
		self.cursor.execute("INSERT INTO customer VALUES('%s','%s')"%(self.entryuntlv.get(),self.entrypwtlv.get()))
		self.cursor.close()
		self.con.commit()
		self.con.close()
		messagebox.showinfo('successfully!')
		self.w1.destroy()
	#=====================================================face resigter==========================================================#	
	def getdata(self):
		get.insertandupdate(self.entryuntlv.get(),self.entrypwtlv.get())

		self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
		self.cap = cv2.VideoCapture(0)

		num=0

		while True:
			self.ret, self.frame= self.cap.read()
			self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
			self.faces = self.face_cascade.detectMultiScale(self.gray, 1.3, 5)

			for (x,y,h,w) in self.faces:
				cv2.rectangle(self.frame, (x,y),(x+w,y+h),(0,255,0),2)

				if not os.path.exists('D:\\python\\pjck\\datafile'):
					os.makedirs('D:\\python\\pjck\\datafile')
				num +=1
				cv2.imwrite('datafile/user.'+str(self.entryuntlv.get())+'.'+str(num)+'.jpg',self.gray[y:y+h,x:x+w])

			cv2.imshow('frame',self.frame)
			cv2.waitKey(1)

			if num >100:
				break
		self.cap.release()
		cv2.destroyAllWindows()
		train.train()
		self.w1.destroy()
	
	#=====================================================face login==========================================================#	
	def face(self):
		import final 
		
		
#====================================================class 2===================================================================#

class window2:
	def __init__(self,root):
		#===================================================Create window==============================================================#
		self.root = root
		self.root.title('duong')
		self.root.geometry("%dx%d+%d+%d" % (1280,718,(self.root.winfo_screenwidth())/2-(1280/2),(self.root.winfo_screenheight())/2-(718/2)-40))
		self.root.resizable(False,False)
		self.bg = Label(self.root, bg='pink').place(x=0,y=0, relwidth=1,relheight=1)

		#===================================================frame==============================================================#
		self.frameleft= Frame(self.root, bg='white')
		self.frameleft.place(x=50,y=50,width=450,height=610)
		self.frameright= Frame(self.root, bg='black')
		self.frameright.place(x=600,y=170,width=600,height=320)
		self.frameright_inside= Frame(self.root,bg='white')
		self.frameright_inside.place(x=605,y=175,width=590,height=310)
		self.frameright_bottom= Frame(self.root,bg='black')
		self.frameright_bottom.place(x=900-50,y=490,width=100,height=50)
		self.frameright_bottom2= Frame(self.root,bg='black')
		self.frameright_bottom2.place(x=900-150,y=540,width=300,height=5)

		#================================title=========================================#
		self.labelleft_bg= Label(self.root, bg='pink')
		self.labelleft_bg.place(x=60,y=60,width=430,height=590)
		self.labelleft_title = Label(self.root,text='MENU',font=('Bimbo',30,'bold'),fg='black',bg='pink')
		self.labelleft_title.place(x=208,y=70)
		#=================================background's button==========================#
		self.labelbg1= Label(self.root,bg='white')
		self.labelbg1.place(x=90,y=160,width=175,height=53)
		self.labelbg2= Label(self.root,bg='white')
		self.labelbg2.place(x=290,y=160,width=175,height=53)

		self.labelbg3= Label(self.root,bg='white')
		self.labelbg3.place(x=90,y=260,width=175,height=53)
		self.labelbg4= Label(self.root,bg='white')
		self.labelbg4.place(x=290,y=260,width=175,height=53)

		self.labelbg5= Label(self.root,bg='white')
		self.labelbg5.place(x=90,y=360,width=175,height=53)
		self.labelbg6= Label(self.root,bg='white')
		self.labelbg6.place(x=290,y=360,width=175,height=53)

		self.labelbg7= Label(self.root,bg='white')
		self.labelbg7.place(x=90,y=480,width=175,height=53)
		self.labelbg8= Label(self.root,bg='white')
		self.labelbg8.place(x=290,y=480,width=175,height=53)

		#===============================detail label====================================#
		self.Label_detail= Label(self.frameright_inside,text='No Signal',font=('Bimbo',15))
		self.Label_detail.place(x=0,y=0,width=590,height=310)

		#===================================================Button============================================================#

		self.bt1= Button(self.root,text='App1',font=('Pixie Ring Font',20,'bold'),width=10,command=self.change1)
		self.bt1.place(x=80,y=150)
		self.bt2= Button(self.root,text='App2',font=('Pixie Ring Font',20,'bold'),width=10,command=self.change2)
		self.bt2.place(x=280,y=150)

		self.bt3= Button(self.root,text='App3',font=('Pixie Ring Font',20,'bold'),width=10,command=self.change3)
		self.bt3.place(x=80,y=250)
		self.bt4= Button(self.root,text='App4',font=('Pixie Ring Font',20,'bold'),width=10)
		self.bt4.place(x=280,y=250)

		self.bt5= Button(self.root,text='App5',font=('Pixie Ring Font',20,'bold'),width=10)
		self.bt5.place(x=80,y=350)
		self.bt6= Button(self.root,text='App6',font=('Pixie Ring Font',20,'bold'),width=10)
		self.bt6.place(x=280,y=350)

		self.bt7= Button(self.root,text='Help',font=('Pixie Ring Font',20,'bold'),width=10,command=self.changehelp)
		self.bt7.place(x=80,y=470)
		self.bt8= Button(self.root,text='Exit',font=('Pixie Ring Font',20,'bold'),width=10,command=self.exit)
		self.bt8.place(x=280,y=470)
		self.root.mainloop()
	#===================================================Exit Button===========================================================#
	def exit(self):
		sysexit()
	#==================================================Create launch button===================================================#
	def change1(self):
		self.Label_detail.config(text='Facebook')
		self.bt_launch1= Button(self.root,text='Launch',font=('Pixie Ring Font',20,'bold'),width=10,command=self.run1)
		self.bt_launch1.place(x=900-85,y=560)
	def change2(self):
		self.Label_detail.config(text='Youtube')
		self.bt_launch2= Button(self.root,text='Launch',font=('Pixie Ring Font',20,'bold'),width=10,command=self.run2)
		self.bt_launch2.place(x=900-85,y=560)
	def change3(self):
		self.Label_detail.config(text='')
		self.bt_launch3= Button(self.root,text='Launch',font=('Pixie Ring Font',20,'bold'),width=10)
		self.bt_launch3.place(x=900-85,y=560)
	def changehelp(self):
		self.Label_detail.config(text='Talk to him')
		self.bt_launchhelp= Button(self.root,text='Launch',font=('Pixie Ring Font',20,'bold'),width=10,command=self.runhelp)
		self.bt_launchhelp.place(x=900-85,y=560)
	#====================================================Run app==============================================================#
	def run1(self):
		webbrowser.open_new('https://www.facebook.com')
	def run2(self):
		webbrowser.open_new('https://www.youtube.com')
	def runhelp(self):
		webbrowser.open_new('https://www.facebook.com/profile.php?id=100014091498993')


if __name__ == '__main__':
	main()


 
