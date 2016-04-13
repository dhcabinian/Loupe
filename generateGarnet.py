from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GenerateGarnetNetworkWindow(object):
    def setupUi(self, GenerateGarnetNetworkWindow):
        GenerateGarnetNetworkWindow.setObjectName(_fromUtf8("GenerateGarnetNetworkWindow"))
        GenerateGarnetNetworkWindow.resize(513, 500)
        GenerateGarnetNetworkWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtGui.QWidget(GenerateGarnetNetworkWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_topology_options = QtGui.QLabel(self.centralwidget)
        self.label_topology_options.setAlignment(QtCore.Qt.AlignCenter)
        self.label_topology_options.setObjectName(_fromUtf8("label_topology_options"))
        self.verticalLayout.addWidget(self.label_topology_options)
        self.combo_topology = QtGui.QComboBox(self.centralwidget)
        self.combo_topology.setObjectName(_fromUtf8("combo_topology"))
        self.combo_topology.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.combo_topology)
        self.sld_numcpus = QtGui.QSlider(self.centralwidget)
        self.sld_numcpus.setMaximum(64)
        self.sld_numcpus.setSliderPosition(16)
        self.sld_numcpus.setOrientation(QtCore.Qt.Horizontal)
        self.sld_numcpus.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sld_numcpus.setTickInterval(2)
        self.sld_numcpus.setObjectName(_fromUtf8("sld_numcpus"))
        self.verticalLayout.addWidget(self.sld_numcpus)
        self.sld_numrows = QtGui.QSlider(self.centralwidget)
        self.sld_numrows.setMaximum(8)
        self.sld_numrows.setProperty("value", 4)
        self.sld_numrows.setOrientation(QtCore.Qt.Horizontal)
        self.sld_numrows.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sld_numrows.setTickInterval(1)
        self.sld_numrows.setObjectName(_fromUtf8("sld_numrows"))
        self.verticalLayout.addWidget(self.sld_numrows)
        self.sld_vcspervnet = QtGui.QSlider(self.centralwidget)
        self.sld_vcspervnet.setMaximum(8)
        self.sld_vcspervnet.setSliderPosition(8)
        self.sld_vcspervnet.setOrientation(QtCore.Qt.Horizontal)
        self.sld_vcspervnet.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sld_vcspervnet.setTickInterval(1)
        self.sld_vcspervnet.setObjectName(_fromUtf8("sld_vcspervnet"))
        self.verticalLayout.addWidget(self.sld_vcspervnet)
        self.label_simulation_options = QtGui.QLabel(self.centralwidget)
        self.label_simulation_options.setAlignment(QtCore.Qt.AlignCenter)
        self.label_simulation_options.setObjectName(_fromUtf8("label_simulation_options"))
        self.verticalLayout.addWidget(self.label_simulation_options)
        self.sld_simcycles = QtGui.QSlider(self.centralwidget)
        self.sld_simcycles.setMaximum(5000)
        self.sld_simcycles.setSingleStep(500)
        self.sld_simcycles.setSliderPosition(2500)
        self.sld_simcycles.setOrientation(QtCore.Qt.Horizontal)
        self.sld_simcycles.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sld_simcycles.setTickInterval(500)
        self.sld_simcycles.setObjectName(_fromUtf8("sld_simcycles"))
        self.verticalLayout.addWidget(self.sld_simcycles)
        self.sld_injectionrate = QtGui.QSlider(self.centralwidget)
        self.sld_injectionrate.setMaximum(100)
        self.sld_injectionrate.setSingleStep(2)
        self.sld_injectionrate.setProperty("value", 24)
        self.sld_injectionrate.setOrientation(QtCore.Qt.Horizontal)
        self.sld_injectionrate.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sld_injectionrate.setTickInterval(10)
        self.sld_injectionrate.setObjectName(_fromUtf8("sld_injectionrate"))
        self.verticalLayout.addWidget(self.sld_injectionrate)
        self.combo_traffic = QtGui.QComboBox(self.centralwidget)
        self.combo_traffic.setObjectName(_fromUtf8("combo_traffic"))
        self.combo_traffic.addItem(_fromUtf8(""))
        self.combo_traffic.addItem(_fromUtf8(""))
        self.combo_traffic.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.combo_traffic)
        self.combo_algorithm = QtGui.QComboBox(self.centralwidget)
        self.combo_algorithm.setObjectName(_fromUtf8("combo_algorithm"))
        self.combo_algorithm.addItem(_fromUtf8(""))
        self.combo_algorithm.addItem(_fromUtf8(""))
        self.combo_algorithm.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.combo_algorithm)

        self.pb_createRunCommand = QtGui.QPushButton(self.centralwidget)
        self.pb_createRunCommand.setObjectName(_fromUtf8("pb_createRunCommand"))
        self.pb_createRunCommand.clicked.connect(self.showGarnetCmd)
        self.verticalLayout.addWidget(self.pb_createRunCommand)


        self.horizontalLayout.addLayout(self.verticalLayout)
        GenerateGarnetNetworkWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GenerateGarnetNetworkWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        GenerateGarnetNetworkWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GenerateGarnetNetworkWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GenerateGarnetNetworkWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GenerateGarnetNetworkWindow)
        QtCore.QMetaObject.connectSlotsByName(GenerateGarnetNetworkWindow)

    def retranslateUi(self, GenerateGarnetNetworkWindow):
        GenerateGarnetNetworkWindow.setWindowTitle(_translate("GenerateGarnetNetworkWindow", "Generate Garnet Network", None))
        self.label_topology_options.setText(_translate("GenerateGarnetNetworkWindow", "Topology Options", None))
        self.combo_topology.setItemText(0, _translate("GenerateGarnetNetworkWindow", "Mesh", None))
        self.label_simulation_options.setText(_translate("GenerateGarnetNetworkWindow", "Simulation Options", None))
        self.combo_traffic.setItemText(0, _translate("GenerateGarnetNetworkWindow", "Uniform Random Traffic", None))
        self.combo_traffic.setItemText(1, _translate("GenerateGarnetNetworkWindow", "Tornado Traffic", None))
        self.combo_traffic.setItemText(2, _translate("GenerateGarnetNetworkWindow", "Bit Complement Traffic", None))
        self.combo_algorithm.setItemText(0, _translate("GenerateGarnetNetworkWindow", "XY Routing", None))
        self.combo_algorithm.setItemText(1, _translate("GenerateGarnetNetworkWindow", "George Routing", None))
        self.combo_algorithm.setItemText(2, _translate("GenerateGarnetNetworkWindow", "Escape VC Routing", None))
        self.pb_createRunCommand.setText(_translate("GenerateGarnetNetworkWindow", "Create Run Command", None))


    def showGarnetCmd(self):
        garnetDialog = QtGui.QMessageBox()
        runCmd = self.generateRunCmd()
        garnetDialog.setWindowTitle("Generated Garnet Command")
        garnetDialog.setText("Here is the generated Garnet Command:")
        garnetDialog.setDetailedText(runCmd)
        garnetDialog.exec_()

    def generateRunCmd(self):
        runCommand = "./build/ALPHA_Network_test/gem5.debug configs/example/ruby_network_test.py \\"
        runCommand += " --network=garnet2.0 \\"
        runCommand += " --num-cpus=" + str(self.sld_numcpus.value()) + " \\"
        runCommand += " --num-dirs=" + str(self.sld_numcpus.value()) + " \\"
        runCommand += " --topology=" + str(self.combo_topology.currentText()) + " \\"
        runCommand += " --num-rows=" + str(self.sld_numrows.value()) + " \\"
        runCommand += " --sim-cycles=" + str(self.sld_simcycles.value()) + " \\"
        runCommand += " --injectionrate=" + str(self.sld_injectionrate.value()/100) + " \\"
        if (self.combo_traffic.currentText() == "Uniform Random Traffic"):
            runCommand += " --synthetic=" + str(0) + " \\"
        elif (self.combo_traffic.currentText() == "Tornado Traffic"):
            runCommand += " --synthetic=" + str(1) + " \\"
        elif (self.combo_traffic.currentText() == "Bit Complement Traffic"):
            runCommand += " --synthetic=" + str(2) + " \\"
        else:
            print("Invalid traffic type")
        runCommand += " --vcs-per-vnet=" + str(self.sld_vcspervnet.value()) + " \\"
        if (self.combo_algorithm.currentText() == "XY Routing"):
            runCommand += " --routing-algorithm=" + str(0) + " \\"
        elif (self.combo_algorithm.currentText() == "George Routing"):
            runCommand += " --routing-algorithm=" + str(1) + " \\"
        elif (self.combo_algorithm.currentText() == "Escape VC Routing"):
            runCommand += " --routing-algorithm=" + str(2) + " \\"
        else:
            print("Invalid algorithm")
        print(runCommand)
        return runCommand


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    GenerateGarnetNetworkWindow = QtGui.QMainWindow()
    ui = Ui_GenerateGarnetNetworkWindow()
    ui.setupUi(GenerateGarnetNetworkWindow)
    GenerateGarnetNetworkWindow.show()
    sys.exit(app.exec_())

