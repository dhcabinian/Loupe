import sys

# from mainwindow import Window
from mainwindow import Ui_GuiMainWindow
from PyQt4 import QtCore, QtGui

# if __name__ == '__main__':
#     print("Hello")
#     app = QtGui.QApplication(sys.argv)
#     GUI = Window()
#     sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    GuiMainWindow = QtGui.QMainWindow()
    ui = Ui_GuiMainWindow()
    ui.setupUi(GuiMainWindow)
    GuiMainWindow.show()
    sys.exit(app.exec_())
