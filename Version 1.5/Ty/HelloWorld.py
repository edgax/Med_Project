import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
	app = QApplication(sys.argv)
	widget = QWidget()
	
	textLabel =  QLabel(widget)
	textLabel.setText("Hello World")
	textLabel.move(110,85)

	widget.setGeometry(50,50,320,200)
	widget.setWindowTitle("PyQt5 example")
	widget.show()
	sys.exit(app.exec_())
#if _name_ == '_main_':
window()

