# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 356)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.Send = QtWidgets.QPushButton(self.centralWidget)
        self.Send.setGeometry(QtCore.QRect(140, 260, 89, 25))
        self.Send.setObjectName("Send")
        self.Name = QtWidgets.QLabel(self.centralWidget)
        self.Name.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.Name.setObjectName("Name")
        self.DOB = QtWidgets.QLabel(self.centralWidget)
        self.DOB.setGeometry(QtCore.QRect(170, 10, 67, 17))
        self.DOB.setObjectName("DOB")
        self.Medicine = QtWidgets.QLabel(self.centralWidget)
        self.Medicine.setGeometry(QtCore.QRect(10, 70, 67, 17))
        self.Medicine.setObjectName("Medicine")
        self.NameTextBox = QtWidgets.QTextEdit(self.centralWidget)
        self.NameTextBox.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.NameTextBox.setObjectName("NameTextBox")
        self.DOBTextBOX = QtWidgets.QTextEdit(self.centralWidget)
        self.DOBTextBOX.setGeometry(QtCore.QRect(170, 30, 111, 31))
        self.DOBTextBOX.setObjectName("DOBTextBOX")
        self.MedicineTextBox = QtWidgets.QTextEdit(self.centralWidget)
        self.MedicineTextBox.setGeometry(QtCore.QRect(10, 90, 151, 31))
        self.MedicineTextBox.setObjectName("MedicineTextBox")
        self.DescriptionTextBox = QtWidgets.QTextEdit(self.centralWidget)
        self.DescriptionTextBox.setGeometry(QtCore.QRect(10, 160, 361, 91))
        self.DescriptionTextBox.setObjectName("DescriptionTextBox")
        self.Description = QtWidgets.QLabel(self.centralWidget)
        self.Description.setGeometry(QtCore.QRect(10, 130, 91, 31))
        self.Description.setObjectName("Description")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralWidget)
        self.timeEdit.setGeometry(QtCore.QRect(250, 90, 118, 26))
        self.timeEdit.setObjectName("timeEdit")
        self.Time = QtWidgets.QLabel(self.centralWidget)
        self.Time.setGeometry(QtCore.QRect(250, 70, 67, 17))
        self.Time.setObjectName("Time")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 403, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuCareTaker = QtWidgets.QMenu(self.menuBar)
        self.menuCareTaker.setObjectName("menuCareTaker")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuCareTaker.menuAction())

        self.retranslateUi(MainWindow)
        self.Send.clicked.connect(self.DescriptionTextBox.selectAll)
        self.Send.clicked['bool'].connect(self.MedicineTextBox.selectAll)
        self.Send.clicked['bool'].connect(self.DOBTextBOX.selectAll)
        self.Send.clicked['bool'].connect(self.NameTextBox.selectAll)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Send.setText(_translate("MainWindow", "Send"))
        self.Name.setText(_translate("MainWindow", "Name"))
        self.DOB.setText(_translate("MainWindow", "DOB"))
        self.Medicine.setText(_translate("MainWindow", "Medicine"))
        self.Description.setText(_translate("MainWindow", "Description"))
        self.Time.setText(_translate("MainWindow", "Time"))
        self.menuCareTaker.setTitle(_translate("MainWindow", "TakingCare"))

