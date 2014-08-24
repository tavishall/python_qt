from PyQt4 import QtCore
from PyQt4 import QtGui
import sys

import myApp

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	form = myApp.MainWindow()
	form.show()
	app.exec_()
