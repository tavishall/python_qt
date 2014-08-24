from PyQt4 import QtCore
from PyQt4 import QtGui

import sys

import UIchar_gen

class MainWindow(QtGui.QMainWindow, UIchar_gen.Ui_MainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		self.makeConnections()

	def makeConnections(self):
		self.connect(
			self.treeWidget,
			QtCore.SIGNAL("itemClicked(QTreeWidgetItem*, int)"),
			self.itemClicked)

	def itemClicked(self, item, column):
		self.label.setText('Clicked!' + str(column))

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	form = MainWindow()
	form.show()
	app.exec_()
