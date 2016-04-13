from PyQt4 import QtGui, QtCore
from network import Network
from networkAttr import networkAttr
from drawAttr import drawAttr
from CoreExploded import CoreExploded
from CoreInformation import CoreInfo
from generateGarnet import Ui_GenerateGarnetNetworkWindow
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


class Ui_GuiMainWindow(object):
    def setupUi(self, GuiMainWindow):
        self.garnetUi = None
        GuiMainWindow.setObjectName(_fromUtf8("GuiMainWindow"))
        GuiMainWindow.resize(1290, 890)
        self.centralwidget = QtGui.QWidget(GuiMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.GuiNetwork = Network(self.centralwidget, "Mesh", 16, 4, 8, 5000)
        networkSize = self.calculateNetworkSize(16, 4)
        self.GuiNetwork.setMinimumSize(networkSize)
        self.GuiNetwork.setObjectName(_fromUtf8("GuiNetworkFrame"))
        self.horizontalLayout.addWidget(self.GuiNetwork)

        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.GuiCoreSelectorCombo = QtGui.QComboBox(self.centralwidget)
        self.GuiCoreSelectorCombo.setObjectName(_fromUtf8("GuiCoreSelectorCombo"))
        self.GuiCoreSelectorCombo.activated.connect(self.closeViewCore)
        self.coreSelectorSetup(networkAttr.ATTR_CORE_CORES)
        self.verticalLayout.addWidget(self.GuiCoreSelectorCombo)

        self.explodedCoreView = CoreExploded(self.centralwidget, self.GuiNetwork.cores[0])
        self.explodedCoreView.setMinimumSize(QtCore.QSize(drawAttr.DRAW_CORE_SIZE_EXP + 50,
                                                          drawAttr.DRAW_CORE_SIZE_EXP + 50))
        self.explodedCoreView.setObjectName(_fromUtf8("explodedCoreView"))
        self.verticalLayout.addWidget(self.explodedCoreView)

        self.GuiCoreInfo = CoreInfo(self.centralwidget, self.GuiNetwork.cores[0])
        self.GuiCoreInfo.setObjectName(_fromUtf8("GuiCoreInfo"))
        self.verticalLayout.addWidget(self.GuiCoreInfo)

        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        #Pushbuttons
        self.GuiPreviousCyclePb = QtGui.QPushButton(self.centralwidget)
        self.GuiPreviousCyclePb.setObjectName(_fromUtf8("GuiPreviousCyclePb"))
        self.GuiPreviousCyclePb.clicked.connect(self.previous_cycle)
        self.horizontalLayout_2.addWidget(self.GuiPreviousCyclePb)
        self.GuiNextCyclePb = QtGui.QPushButton(self.centralwidget)
        self.GuiNextCyclePb.setObjectName(_fromUtf8("GuiNextCyclePb"))
        self.GuiNextCyclePb.clicked.connect(self.next_cycle)
        self.horizontalLayout_2.addWidget(self.GuiNextCyclePb)

        #LCD Cycle Counter
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.GuiCycleCounter = QtGui.QLCDNumber(self.centralwidget)
        self.GuiCycleCounter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.GuiCycleCounter.setObjectName(_fromUtf8("GuiCycleCounter"))
        self.verticalLayout.addWidget(self.GuiCycleCounter)

        #Cycle Progress Bar
        self.GuiCycleProgressBar = QtGui.QProgressBar(self.centralwidget)
        self.GuiCycleProgressBar.setProperty("value", 0)
        self.GuiCycleProgressBar.setObjectName(_fromUtf8("GuiCycleProgressBar"))
        self.verticalLayout.addWidget(self.GuiCycleProgressBar)
        self.horizontalLayout.addLayout(self.verticalLayout)
        GuiMainWindow.setCentralWidget(self.centralwidget)

        #Menu Bar
        self.GuiMenuBar = QtGui.QMenuBar(GuiMainWindow)
        self.GuiMenuBar.setGeometry(QtCore.QRect(0, 0, 1290, 21))
        self.GuiMenuBar.setObjectName(_fromUtf8("GuiMenuBar"))
        self.GuiFileMenu = QtGui.QMenu(self.GuiMenuBar)
        self.GuiFileMenu.setObjectName(_fromUtf8("GuiFileMenu"))
        self.GuiGoToMenu = QtGui.QMenu(self.GuiMenuBar)
        self.GuiGoToMenu.setObjectName(_fromUtf8("GuiGoToMenu"))
        self.GuiGarnetMenu = QtGui.QMenu(self.GuiMenuBar)
        self.GuiGarnetMenu.setObjectName(_fromUtf8("GuiGarnetMenu"))
        GuiMainWindow.setMenuBar(self.GuiMenuBar)

        #Status Bar
        self.statusbar = QtGui.QStatusBar(GuiMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GuiMainWindow.setStatusBar(self.statusbar)

        #Menu Bar Items
        self.actionGo_To_Cycle = QtGui.QAction(GuiMainWindow)
        self.actionGo_To_Cycle.setObjectName(_fromUtf8("actionGo_To_Cycle"))
        self.GuiGoTo0MenuAction = QtGui.QAction(GuiMainWindow)
        self.GuiGoTo0MenuAction.triggered.connect(self.go_to_cycle_0)
        self.GuiGoTo0MenuAction.setObjectName(_fromUtf8("GuiGoTo0MenuAction"))
        self.GuiGoTo500MenuAction = QtGui.QAction(GuiMainWindow)
        self.GuiGoTo500MenuAction.triggered.connect(self.go_to_cycle_500)
        self.GuiGoTo500MenuAction.setObjectName(_fromUtf8("GuiGoTo500MenuAction"))
        self.GuiGoToCycleMenuAction = QtGui.QAction(GuiMainWindow)
        self.GuiGoToCycleMenuAction.triggered.connect(self.got_to_cycle_X)
        self.GuiGoToCycleMenuAction.setObjectName(_fromUtf8("GuiGoToCycleMenuAction"))
        self.GuiGarnetGenerateMenuAction = QtGui.QAction(GuiMainWindow)
        self.GuiGarnetGenerateMenuAction.triggered.connect(self.garnet_generator)
        self.GuiGarnetGenerateMenuAction.setObjectName(_fromUtf8("GuiGarnetGenerateMenuAction"))
        self.GuiGarnetHelpMenuAction = QtGui.QAction(GuiMainWindow)
        self.GuiGarnetHelpMenuAction.setShortcut("Ctrl+H")
        self.GuiGarnetHelpMenuAction.triggered.connect(self.garnet_help)
        self.GuiGarnetHelpMenuAction.setObjectName(_fromUtf8("GuiGarnetHelpMenuAction"))
        self.GuiFileOpenTraceMenuAction = QtGui.QAction(GuiMainWindow)
        self.GuiFileOpenTraceMenuAction.setShortcut("Ctrl+O")
        self.GuiFileOpenTraceMenuAction.triggered.connect(self.file_open_trace)
        self.GuiFileOpenTraceMenuAction.setObjectName(_fromUtf8("GuiFileOpenTraceMenuAction"))
        self.GuiFileExitMenuAction = QtGui.QAction(GuiMainWindow)
        self.GuiFileExitMenuAction.setShortcut("Ctrl+Q")
        self.GuiFileExitMenuAction.triggered.connect(self.quit_application)
        self.GuiFileExitMenuAction.setObjectName(_fromUtf8("GuiFileExitMenuAction"))


        self.GuiFileMenu.addAction(self.GuiFileOpenTraceMenuAction)
        self.GuiFileMenu.addAction(self.GuiFileExitMenuAction)
        self.GuiGoToMenu.addAction(self.GuiGoTo0MenuAction)
        self.GuiGoToMenu.addAction(self.GuiGoTo500MenuAction)
        self.GuiGoToMenu.addAction(self.GuiGoToCycleMenuAction)
        self.GuiGarnetMenu.addAction(self.GuiGarnetGenerateMenuAction)
        self.GuiGarnetMenu.addAction(self.GuiGarnetHelpMenuAction)
        self.GuiMenuBar.addAction(self.GuiFileMenu.menuAction())
        self.GuiMenuBar.addAction(self.GuiGoToMenu.menuAction())
        self.GuiMenuBar.addAction(self.GuiGarnetMenu.menuAction())

        self.retranslateUi(GuiMainWindow)
        QtCore.QMetaObject.connectSlotsByName(GuiMainWindow)


    def retranslateUi(self, GuiMainWindow):
        GuiMainWindow.setWindowTitle(_translate("GuiMainWindow", "Loupe", None))
        self.GuiPreviousCyclePb.setText(_translate("GuiMainWindow", "Previous Cycle", None))
        self.GuiNextCyclePb.setText(_translate("GuiMainWindow", "Next Cycle", None))
        self.GuiFileMenu.setTitle(_translate("GuiMainWindow", "File", None))
        self.GuiGoToMenu.setTitle(_translate("GuiMainWindow", "Go To", None))
        self.GuiGarnetMenu.setTitle(_translate("GuiMainWindow", "Garnet", None))
        self.actionGo_To_Cycle.setText(_translate("GuiMainWindow", "Go To Cycle...", None))
        self.GuiGoTo0MenuAction.setText(_translate("GuiMainWindow", "Cycle 0", None))
        self.GuiGoTo500MenuAction.setText(_translate("GuiMainWindow", "Cycle 500", None))
        self.GuiGoToCycleMenuAction.setText(_translate("GuiMainWindow", "Cycle ...", None))
        self.GuiGarnetGenerateMenuAction.setText(_translate("GuiMainWindow", "Generate Garnet Run Command", None))
        self.GuiGarnetHelpMenuAction.setText(_translate("GuiMainWindow", "Help", None))
        self.GuiFileOpenTraceMenuAction.setText(_translate("GuiMainWindow", "Open Trace...", None))
        self.GuiFileExitMenuAction.setText(_translate("GuiMainWindow", "Quit", None))

    def calculateNetworkSize(self, cores, rows):
        width = networkAttr.ATTR_CORE_COLS * drawAttr.DRAW_CORE_SIZE\
                + (networkAttr.ATTR_CORE_COLS - 1) * drawAttr.DRAW_LINK_LENGTH + 10
        height = width - 8
        return QtCore.QSize(width, height)

    def next_cycle(self):
        print ("next cycle")
        cycle_num = self.GuiNetwork.nextCycle()
        self.GuiCycleProgressBar.setValue(cycle_num/networkAttr.ATTR_NET_TOTCYCLES * 100)
        self.GuiCycleCounter.display(cycle_num)

    def previous_cycle(self):
        print ("previous cycle")
        cycle_num = self.GuiNetwork.prevCycle()
        if cycle_num == None:
            pass
        else:
            self.GuiCycleProgressBar.setValue(cycle_num/networkAttr.ATTR_NET_TOTCYCLES * 100)
            self.GuiCycleCounter.display(cycle_num)

    def coreSelectorSetup(self, core_num):
        for index in range(core_num):
            self.GuiCoreSelectorCombo.addItem(_fromUtf8(""))
            coreSelectText = "Core " + str(index)
            self.GuiCoreSelectorCombo.setItemText(index, _translate("GuiMainWindow", coreSelectText, None))

    def closeViewCore(self):
        core_num = self.GuiCoreSelectorCombo.currentIndex()
        print(core_num)
        self.explodedCoreView.updateCore(self.GuiNetwork.cores[core_num])
        #self.explodedCoreView.repaint()
        self.explodedCoreView.update()
        self.GuiCoreInfo.updateCoreInfo(self.GuiNetwork.cores[core_num])
        self.GuiCoreInfo.update()

    def file_open_trace(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')


    def quit_application(self):
        print("Closing App...")
        sys.exit()

    def garnet_generator(self):
        print("Garnet")
        self.garnetUi = Ui_GenerateGarnetNetworkWindow()
        self.garnetUi.show()


    def garnet_help(self):
        print("Garnet Help")

    def go_to_cycle_0(self):
        cycle_num = self.GuiNetwork.goToCycle(0)
        if cycle_num is not None:
            self.GuiCycleProgressBar.setValue(cycle_num/networkAttr.ATTR_NET_TOTCYCLES * 100)
            self.GuiCycleCounter.display(cycle_num)

    def go_to_cycle_500(self):
        cycle_num = self.GuiNetwork.goToCycle(500)
        if cycle_num is not None:
            self.GuiCycleProgressBar.setValue(cycle_num/networkAttr.ATTR_NET_TOTCYCLES * 100)
            self.GuiCycleCounter.display(cycle_num)

    def got_to_cycle_X(self):
        inputDialog = QtGui.QWidget()
        text, ok = QtGui.QInputDialog.getText(inputDialog, 'Input Cycle Number', 'Enter Cycle:')
        if ok and int(text) >= 0:
            cycle_num = self.GuiNetwork.goToCycle(int(text))
            print (cycle_num)
            if cycle_num is not None:
                self.GuiCycleProgressBar.setValue(cycle_num / networkAttr.ATTR_NET_TOTCYCLES * 100)
                self.GuiCycleCounter.display(cycle_num)
