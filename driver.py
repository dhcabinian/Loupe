from mainwindow import UI_Network_Main_Window
from PyQt4 import QtCore, QtGui

# if __name__ == '__main__':
#     print("Hello")
#     app = QtGui.QApplication(sys.argv)
#     GUI = Window()
#     sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    GuiMainWindow = UI_Network_Main_Window()
    # GuiMainWindow = QtGui.QMainWindow()
    # ui = Ui_GuiMainWindow()
    # ui.setupUi(GuiMainWindow)
    GuiMainWindow.show()
    sys.exit(app.exec_())
