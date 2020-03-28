# Name : Ty Van Nguyen
# Student Number: C16371061
# Application:Medcation Monitoring Generating Qr code

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
import qrcode
import json
from io import BytesIO
#import MySQLdb as mdb
import pymysql
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 595)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.Send = QtWidgets.QPushButton(self.centralWidget)
        self.Send.setGeometry(QtCore.QRect(550, 190, 171, 51))
        self.Send.setObjectName("Send")
        self.Name = QtWidgets.QLabel(self.centralWidget)
        self.Name.setGeometry(QtCore.QRect(0, 6, 111, 41))
        self.Name.setObjectName("Name")
        self.DOB = QtWidgets.QLabel(self.centralWidget)
        self.DOB.setGeometry(QtCore.QRect(160, 6, 111, 41))
        self.DOB.setObjectName("DOB")
        self.Medicine = QtWidgets.QLabel(self.centralWidget)
        self.Medicine.setGeometry(QtCore.QRect(0, 106, 151, 41))
        self.Medicine.setObjectName("Medicine")
        self.NameTextBox = QtWidgets.QTextEdit(self.centralWidget)
        self.NameTextBox.setGeometry(QtCore.QRect(0, 50, 111, 31))
        self.NameTextBox.setObjectName("NameTextBox")
        self.DOBTextBOX = QtWidgets.QTextEdit(self.centralWidget)
        self.DOBTextBOX.setGeometry(QtCore.QRect(160, 50, 111, 31))
        self.DOBTextBOX.setObjectName("DOBTextBOX")
        self.InstructionBox = QtWidgets.QTextEdit(self.centralWidget)
        self.InstructionBox.setGeometry(QtCore.QRect(0, 230, 391, 201))
        self.InstructionBox.setObjectName("InstructionBox")
        self.Description = QtWidgets.QLabel(self.centralWidget)
        self.Description.setGeometry(QtCore.QRect(0, 196, 391, 31))
        self.Description.setObjectName("Description")
        self.Time = QtWidgets.QLabel(self.centralWidget)
        self.Time.setGeometry(QtCore.QRect(320, 106, 151, 41))
        self.Time.setObjectName("Time")
        self.DosageBox = QtWidgets.QTextEdit(self.centralWidget)
        self.DosageBox.setGeometry(QtCore.QRect(160, 150, 151, 31))
        self.DosageBox.setObjectName("DosageBox")
        self.Medicine_2 = QtWidgets.QLabel(self.centralWidget)
        self.Medicine_2.setGeometry(QtCore.QRect(160, 106, 141, 41))
        self.Medicine_2.setObjectName("Medicine_2")
        self.FrequencyBox = QtWidgets.QTextEdit(self.centralWidget)
        self.FrequencyBox.setGeometry(QtCore.QRect(320, 150, 151, 31))
        self.FrequencyBox.setObjectName("FrequencyBox")
        self.DOB_2 = QtWidgets.QLabel(self.centralWidget)
        self.DOB_2.setGeometry(QtCore.QRect(320, 6, 111, 41))
        self.DOB_2.setObjectName("DOB_2")
        self.PPSNBOX = QtWidgets.QTextEdit(self.centralWidget)
        self.PPSNBOX.setGeometry(QtCore.QRect(320, 50, 111, 31))
        self.PPSNBOX.setObjectName("PPSNBOX")
        self.qrcodeimage = QtWidgets.QLabel(self.centralWidget)
        self.qrcodeimage.setGeometry(QtCore.QRect(410, 260, 341, 271))
        self.qrcodeimage.setText("")
        self.qrcodeimage.setObjectName("qrcodeimage")
        self.Duration = QtWidgets.QLabel(self.centralWidget)
        self.Duration.setGeometry(QtCore.QRect(490, 106, 151, 41))
        self.Duration.setObjectName("Duration")
        self.DurationBox = QtWidgets.QTextEdit(self.centralWidget)
        self.DurationBox.setGeometry(QtCore.QRect(490, 150, 151, 31))
        self.DurationBox.setObjectName("DurationBox")
        self.MedicineTextBox = QtWidgets.QTextEdit(self.centralWidget)
        self.MedicineTextBox.setGeometry(QtCore.QRect(0, 150, 151, 31))
        self.MedicineTextBox.setObjectName("MedicineTextBox")
        self.Load = QtWidgets.QPushButton(self.centralWidget)
        self.Load.setGeometry(QtCore.QRect(200, 460, 171, 51))
        self.Load.setObjectName("Load")
        self.ButtonClear = QtWidgets.QPushButton(self.centralWidget)
        self.ButtonClear.setGeometry(QtCore.QRect(10, 460, 171, 51))
        self.ButtonClear.setObjectName("ButtonClear")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 758, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuCareTaker = QtWidgets.QMenu(self.menuBar)
        self.menuCareTaker.setObjectName("menuCareTaker")
        self.menuQR_Reader = QtWidgets.QMenu(self.menuBar)
        self.menuQR_Reader.setObjectName("menuQR_Reader")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuQR_Reader.addSeparator()
        self.menuBar.addAction(self.menuCareTaker.menuAction())
        self.menuBar.addAction(self.menuQR_Reader.menuAction())

        self.retranslateUi(MainWindow)
        self.Send.clicked.connect(self.InstructionBox.selectAll)
        self.Send.clicked['bool'].connect(self.DOBTextBOX.selectAll)
        self.Send.clicked['bool'].connect(self.NameTextBox.selectAll)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Send.setText(_translate("MainWindow", "Generate QR Code"))
        self.Name.setText(_translate("MainWindow", "Name"))
        self.DOB.setText(_translate("MainWindow", "DOB"))
        self.Medicine.setText(_translate("MainWindow", "Medication Name"))
        self.Description.setText(_translate("MainWindow", "Instruction"))
        self.Time.setText(_translate("MainWindow", "Frequency "))
        self.Medicine_2.setText(_translate("MainWindow", "Dosage"))
        self.DOB_2.setText(_translate("MainWindow", "PPSN"))
        self.Duration.setText(_translate("MainWindow", "Duration"))
        self.Load.setText(_translate("MainWindow", "Load into Array"))
        self.ButtonClear.setText(_translate("MainWindow", "Clear"))
        self.menuCareTaker.setTitle(_translate("MainWindow", "TakingCare"))
        self.menuQR_Reader.setTitle(_translate("MainWindow", "QR Reader"))


     #Setting background Image 
        #oImage = QImage("test.jpg")
        #sImage = oImage.scaled(QSize(300,200))
        #palette = QPalette()
        #palette.setBrush(10, QBrush(sImage))
        #self.setPalette(palette)
        #self.show()
stylesheet = """
     MainWindow {
     background-image:url("Test.jpg");
     background-repeat: no-repeat;
     background-position center;
     }
"""        

ui = None
json_array = []
        
def OnClicked():
    #Save the JsonObject to a json file 
    #with open('mydata.json', 'w') as f:
    #json.dump(patient, f)
    
     bytes_Json = json.dumps(json_array).encode('utf-8')
     print(bytes_Json)
     
    
    #Encrypting A simple Message
     key ='This is a Key123' 
     IV = 'This is an IV456'
      
     message ="This is a KeyGay"
      
     obj = AES.new(key,AES.MODE_CFB,IV)
     ciphertext = obj.encrypt(bytes_Json)
     print(ciphertext)
    
    #Decrypting a Simple Message
     obj2 = AES.new(key,AES.MODE_CFB,IV)
     decrytoText = obj2.decrypt(ciphertext)
     print(decrytoText)
     
    #Generating the QR Code
     qr = qrcode.QRCode(version= 1, error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=3,border=3)
     #qr.add_data(json.dumps(json_array))
     qr.add_data(ciphertext)
     qr.make(fit=True)

	#Creating the Image and Save into the buffer
     img = qr.make_image(fill_color="black", back_color="white")
     buf = BytesIO()
     img.save(buf,"PNG")
    
    #Setting the PNG Image from the buffer
     qt_pixmap = QtGui.QPixmap()
     qt_pixmap.loadFromData(buf.getvalue(), "PNG")
     ui.qrcodeimage.setPixmap(qt_pixmap)
 
def ButtonClear():
    
    print('Clear')
    del json_array[:]
    
def Load():
      patient = {}
      alert = QMessageBox()
      name = ui.NameTextBox.toPlainText()
      DOB = ui.DOBTextBOX.toPlainText()
      PPSN = ui.PPSNBOX.toPlainText()
      Medication = ui.MedicineTextBox.toPlainText()
      Dosage = ui.DosageBox.toPlainText()
      Frequency = ui.FrequencyBox.toPlainText()
      Instruction = ui.InstructionBox.toPlainText()
      Duration = ui.DurationBox.toPlainText()
     
      if name is '':
         alert.setText('Fill in your Name Please')
         alert.exec_()
      else:
         patient['name'] = name 
         
      if DOB is '':
         alert.setText('Fill in your DOB Please')
         alert.exec_()
      else:
         patient['DOB'] = DOB
         
      if PPSN is '':
         alert.setText('Fill in your PPSN Please')
         alert.exec_()
      else:
         patient['PPSN'] = PPSN
            
      if Medication is '':
         alert.setText('Fill in your Medication Please')
         alert.exec_()
      else:
         patient['Medictation_Name'] = Medication
		 
      if Dosage is '':
         alert.setText('Fill in your Dosage Please')
         alert.exec_()
      else:
         patient['Dosage'] = Dosage
		 
      if Frequency is '':
         alert.setText('Fill in your Frequency Please')
         alert.exec_()
      else:
         patient['Frequency'] = Frequency
           
      if Instruction is '':
         alert.setText('Fill in your Instruction Please')
         alert.exec_()
      else:
         patient['Instructions'] = Instruction
		 
      if Duration is '':
         alert.setText('Fill in your Duration Please')
         alert.exec_()    
      else:
         patient['Duration'] = Duration           
    
      print('Load')
      
      json_array.append(patient)
      
      print(json_array)
      
       #Connecting and INSERTING data into DATABASE
      try:
       db = pymysql.connect('localhost', 'root', '', 'Medication')
       print("Connect Successfuly")
     
       cursor = db.cursor()
       sql = "INSERT INTO PatientList(PPSN,NAME,DOB,Medication_Name,Dosage,Frequency,Instruction) VALUES (%s, %s,%s,%s,%s,%s,%s)"
       val = (ui.PPSNBOX.toPlainText(),ui.NameTextBox.toPlainText(),ui.DOBTextBOX.toPlainText(),
       ui.MedicineTextBox.toPlainText(),ui.DosageBox.toPlainText(),ui.FrequencyBox.toPlainText(),ui.InstructionBox.toPlainText())
     
       cursor.execute(sql,val)
       db.commit()  
       db.close()
      except pymysql.Error as e:
       print("Fail Connect") 
      
    #with open('mydata.json', 'w') as f:	
     #json.dumps(json_array, f)
      #Encrypting the Json Object 
      #crypter = objcrypt.Crypter('key', 'cbc')
      #encrypted_dict = crypter.encrypt_object(patient)
      
      #Encrpyting from a file  
      #json_dict = json.load(patient)
      #enc_json = crypter.encrypt_json(json_dict)0
      
      #print(encrypted_dict)
      #dec_dict = crypter.decrypt_object(encrypted_dict)
   
      #Different way of encrpytion 
      #encryptedString = AES.encrypt(patient)
      #objectEncrypted = b64encode(encryptedString)
           
class LoginForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Login TakingCare')
		self.resize(500, 120)
		layout = QGridLayout()
		label_name = QLabel('<font size="4"> Username </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('Please enter your username')
		layout.addWidget(label_name, 0, 0)
		username = self.lineEdit_username.text()
		layout.addWidget(self.lineEdit_username, 0, 1)
		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setPlaceholderText('Please enter your password')
		password = self.lineEdit_password.text()
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)

		button_login = QPushButton('Login')
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)
		
		oImage = QImage ("Test2.jpg")
		sImage = oImage.scaled(QSize(500,160))
		palette = QPalette()
		palette.setBrush(QPalette.Window, QBrush(sImage))
		self.setPalette(palette)
		
		
		self.setLayout(layout)

	def check_password(self):
		msg = QMessageBox()
		username = self.lineEdit_username.text()
		password = self.lineEdit_password.text()
		db = pymysql.connect('localhost', 'root', '', 'Medication')
		cursor = db.cursor()
		query = ("SELECT * FROM Pharamcist WHERE name =%s and Password =%s")
		data=cursor.execute(query,(username,password))
		rs = len(cursor.fetchall())
		if (rs > 0):
			msg.setText('Login Success')
			msg.exec_()
			MainWindow.show()
			self.hide()	
		else:
			msg.setText('Incorrect Password')
			msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    form = LoginForm()
    form.show()
    app.setStyleSheet(stylesheet)
    ui.Send.clicked.connect(OnClicked)
    ui.ButtonClear.clicked.connect(ButtonClear)
    ui.Load.clicked.connect(Load)
    #MainWindow.show()
    sys.exit(app.exec_())


