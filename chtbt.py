#import files for Chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr
import pyaudio
#import files for GUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QPushButton, QLineEdit
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class Ui_MainWindow(object):
	chatbot = ChatBot('APSIT')
	# Create a new trainer for the chatbot
	#trainer = ChatterBotCorpusTrainer(chatbot)
	#trainer.train("chatterbot.corpus.english")
	#conv1=open('college_detail1.yml','r').readlines()
	#conv2=open('faculty_detail1.yml','r').readlines()
	#conv3=open('navigation_detail1.yml','r').readlines()
	#conv4=open('chatbot_detail1.yml','r').readlines()
	#trainer=ListTrainer(chatbot)
	#trainer.train(conv1)
	#trainer.train(conv2)
	#trainer.train(conv3)
	#trainer.train(conv4)
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1027, 815)
		MainWindow.setStyleSheet("")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.widget = QtWidgets.QWidget(self.centralwidget)
		self.widget.setGeometry(QtCore.QRect(-10, -30, 1091, 891))
		self.widget.setObjectName("widget")
		self.listView = QtWidgets.QListView(self.widget)
		self.listView.setGeometry(QtCore.QRect(595, 41, 421, 711))
		self.listView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.listView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.listView.setAlternatingRowColors(True)
		self.listView.setMovement(QtWidgets.QListView.Static)
		self.listView.setViewMode(QtWidgets.QListView.ListMode)
		self.listView.setUniformItemSizes(False)
		self.listView.setObjectName("listView")
		self.lineEdit = QtWidgets.QLineEdit(self.widget)
		self.lineEdit.setGeometry(QtCore.QRect(592, 760, 311, 51))
		self.lineEdit.setObjectName("lineEdit")
		self.pushButton = QtWidgets.QPushButton(self.widget)
		self.pushButton.setGeometry(QtCore.QRect(970, 760, 51, 51))
		self.pushButton.setText("")
		self.pushButton.setObjectName("pushButton")
		self.pushButton_2 = QtWidgets.QPushButton(self.widget)
		self.pushButton_2.setGeometry(QtCore.QRect(910, 760, 51, 51))
		self.pushButton_2.setText("")
		self.pushButton_2.setObjectName("pushButton_2")
		self.label_2 = QtWidgets.QLabel(self.widget)
		self.label_2.setGeometry(QtCore.QRect(60, 170, 281, 211))
		self.label_2.setStyleSheet("background-image: url(apsit.PNG);")
		self.label_2.setText("")
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.widget)
		self.label_3.setGeometry(QtCore.QRect(80, 400, 311, 171))
		font = QtGui.QFont()
		font.setFamily("Tibetan Machine Uni")
		font.setPointSize(65)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_3.setAutoFillBackground(False)
		self.label_3.setObjectName("label_3")
		self.label = QtWidgets.QLabel(self.widget)
		self.label.setGeometry(QtCore.QRect(-460, 30, 1831, 1241))
		self.label.setStyleSheet("background-image: url(123.png);")
		self.label.setText("")
		self.label.setObjectName("label")
		self.listWidget = QtWidgets.QListWidget(self.widget)
		self.listWidget.setGeometry(QtCore.QRect(540, 50, 481, 651))
		self.listWidget.setStyleSheet("background-color: rgb(171, 227, 250);\n"
"font: 57 italic 15pt \"Ubuntu\";\n"
"")
		self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.listWidget.setAlternatingRowColors(True)
		self.listWidget.setObjectName("listWidget")
		self.label_4 = QtWidgets.QLabel(self.widget)
		self.label_4.setGeometry(QtCore.QRect(470, 40, 51, 71))
		self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);")
		self.label_4.setText("")
		self.label_4.setObjectName("label_4")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
		self.lineEdit_2.setGeometry(QtCore.QRect(540, 720, 361, 71))
		self.lineEdit_2.setStyleSheet("background-color: rgb(171, 227, 250);\n"
"font: 57 italic 15pt \"Ubuntu\";\n"
"")
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.pushButton_3 = QtWidgets.QPushButton(self.widget)
		self.pushButton_3.setGeometry(QtCore.QRect(910, 720, 51, 71))
		self.pushButton_3.setStyleSheet("background-color: rgb(171, 227, 250);\n"
		"border-image: url(mic.png);")
		self.pushButton_3.setText("")
		self.pushButton_3.setObjectName("pushButton_3")
		# Onclick_1 function Call
		self.pushButton_3.clicked.connect(self.onClick_2)

		self.pushButton_4 = QtWidgets.QPushButton(self.widget)
		self.pushButton_4.setGeometry(QtCore.QRect(970, 720, 51, 71))
		self.pushButton_4.setStyleSheet("background-color: rgb(171, 227, 250);\n"
		"border-image: url(Send-Icon-PNG-715x657.png);")
		self.pushButton_4.setText("")
		self.pushButton_4.setObjectName("pushButton_4")
		# Onclick_1 function Call
		self.pushButton_4.clicked.connect(self.onClick_1)

		self.label_5 = QtWidgets.QLabel(self.widget)
		self.label_5.setGeometry(QtCore.QRect(20, 60, 101, 81))
		#self.label_5.setStyleSheet("background-image: url(:/Image/apsit1.png);")
		self.label_5.setPixmap(QtGui.QPixmap("apsit1.png"))


		self.label_5.setText("")
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(self.widget)
		self.label_6.setGeometry(QtCore.QRect(140, 50, 271, 101))
		font = QtGui.QFont()
		font.setFamily("Tibetan Machine Uni")
		font.setPointSize(34)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.label_6.setFont(font)
		self.label_6.setAutoFillBackground(False)
		self.label_6.setStyleSheet("font: 75 34pt \"Tibetan Machine Uni\";\n"
		"color: rgb(255, 255, 255);")
		self.label_6.setObjectName("label_6")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1027, 22))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		#Adding intro to List
		self.y=[]
		x="APSIT_BOT : "
		myinfo="Welcome to AP SHAH INSTITUTE OF TECHNOLOGY !!. APSIT BOT at your service. How can I help ?"
		z=x+myinfo
		self.y.append(z)
		self.listWidget.addItems(self.y)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "APSIT BOT"))
		self.label_3.setText(_translate("MainWindow", "APSIT "))
		self.label_6.setText(_translate("MainWindow", "APSIT BOT"))
	def onClick_1(self):
		chatbot = ChatBot('APSIT')
		#user input 
		textValue = self.lineEdit_2.text()
		#clearing the lineEdit
		self.lineEdit_2.clear()
		#converting it into Lower
		message=textValue.lower()
		self.y=[]
		x="YOU : "
		z=x+textValue
		self.y.append(z)
		self.listWidget.addItems(self.y)
		if message.strip() != 'bye':
			reply=chatbot.get_response(message)
			print(reply)
			self.y=[]
			x="APSIT_BOT :"
			reply=str(reply)
			z=x+reply
			self.y.append(z)
			self.listWidget.addItems(self.y)
			reply=str(reply)
			tts=gTTS(reply)
			tts.save('hello.mp3')
			playsound('hello.mp3')
		if message.strip() == 'bye':
			self.y=[]
			x="APSIT_BOT : "
			reply="Bye!!!!"
			z=x+reply
			self.y.append(z)
			self.listWidget.addItems(self.y)
			tts=gTTS(reply)
			tts.save('hello.mp3')
			playsound('hello.mp3')
			quit()
	def onClick_2(self):
		chatbot = ChatBot('APSIT')
		#user input 
		
		#textValue = self.lineEdit_2.text()
		#clearing the lineEdit
		self.lineEdit.clear()
		r = sr.Recognizer()
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			print('Say Something')
			audio = r.listen(source)
			print('Time Over')
		try:
			text=r.recognize_google(audio)
			message =format(text)
			self.y=[]
			x="YOU : "
			z=x+message
			message=message.lower()
			self.y.append(z)
			self.listWidget.addItems(self.y)
			#print('You: {}'.format(text))
		except:
			print("Error")
			pass;
		if message.strip() != 'bye':
			reply=chatbot.get_response(message)
			print(reply)
			self.y=[]
			x="APSIT_BOT :"
			reply=str(reply)
			z=x+reply
			self.y.append(z)
			self.listWidget.addItems(self.y)
			reply=str(reply)
			tts=gTTS(reply)
			tts.save('hello.mp3')
			playsound('hello.mp3')
		if message.strip() == 'bye':
			self.y=[]
			x="APSIT_BOT : "
			reply="Bye!!!!"
			z=x+reply
			self.y.append(z)
			self.listWidget.addItems(self.y)
			tts=gTTS(reply)
			tts.save('hello.mp3')
			playsound('hello.mp3')
			quit()


#import gui1_rc


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	playsound('intro.mp3')
	sys.exit(app.exec_())
