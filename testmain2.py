from PyQt5 import QtWidgets,QtGui
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
import qrcode
import json
from io import BytesIO
#import MySQLdb as mdb
import pymysql


ui = None
json_array = []
def OnClicked():
    print(ui.NameTextBox.toPlainText())
    print(ui.DOBTextBOX.toPlainText())
    print(ui.MedicineTextBox.toPlainText())
    print(ui.InstructionBox.toPlainText())
    
    #Generating the QR Code
    qr = qrcode.QRCode(version= 1, error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=3,border=3)
    qr.add_data(json.dumps(json_array, indent = 4))
    qr.make(fit=True)

	#Creating the Image and Save into the buffer
    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf,"PNG")
    
    #Setting the PNG Image from the buffer
    qt_pixmap = QtGui.QPixmap()
    qt_pixmap.loadFromData(buf.getvalue(), "PNG")
    ui.qrcodeimage.setPixmap(qt_pixmap)
    
    #Connecting and INSERTING data into DATABASE
    #try:
    db = pymysql.connect('localhost', 'root', '', 'Medication')
    print("Connect Successfuly")
     
    cursor = db.cursor()
    sql = "INSERT INTO PatientList(PPSN,NAME,DOB,Medication_Name,Dosage,Frequency,Instruction) VALUES (%s, %s,%s,%s,%s,%s,%s)"
    val = (ui.PPSNBOX.toPlainText(),ui.NameTextBox.toPlainText(),ui.DOBTextBOX.toPlainText(),ui.MedicineTextBox.toPlainText(),ui.DosageBox.toPlainText(),ui.FrequencyBox.toPlainText(),ui.InstructionBox.toPlainText())
     
    cursor.execute(sql,val)
    db.commit()  
   
def ButtonClear():
    
    print('Clear')
    del json_array[:]
    
def Load():

    print('Load')
    patient = {}
     
    patient['name'] = ui.NameTextBox.toPlainText()
    patient['DOB'] = ui.DOBTextBOX.toPlainText()
    patient['PPSN'] = ui.PPSNBOX.toPlainText()
    patient['Medictation_Name'] = ui.MedicineTextBox.toPlainText()
    patient['Dosage'] = ui.DosageBox.toPlainText()
    patient['Frequency'] = ui.FrequencyBox.toPlainText()
    patient['Duration'] = ui.DurationBox.toPlainText()
    patient['Instructions'] = ui.InstructionBox.toPlainText()
   
    json_array.append(patient)
    print(json_array)
      
    #with open('mydata.json', 'w') as f:	
     #json.dumps(json_array, f)
     
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Send.clicked.connect(OnClicked)
    ui.ButtonClear.clicked.connect(ButtonClear)
    ui.Load.clicked.connect(Load)
    MainWindow.show()
    sys.exit(app.exec_())

