from PyQt4 import QtCore
from PyQt4 import QtGui

import UI

class MainWindow(QtGui.QMainWindow, UI.Ui_MainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		self.makeConnections()

	def makeConnections(self):
		self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.pushButtonClicked)

	def pushButtonClicked(self):
		self.label.setText("You clicked the button")

