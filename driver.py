import sys
from PyQt4 import QtGui

from mainwindow import Window

if __name__ == '__main__':
    print("Hello")
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
