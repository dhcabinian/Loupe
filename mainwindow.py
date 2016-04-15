from PyQt4 import QtGui, QtCore
from network import Network
from networkAttr import networkAttr
from drawAttr import drawAttr
from CoreExploded import CoreExploded
from CoreInformation import CoreInfo
from generateGarnet import GuiGenerateGarnet
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


class GuiMainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(GuiMainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('Loupe_icon.png'))
        # def setupUi(self, self):
        self.GuiGarnet = None
        self.setObjectName(_fromUtf8("GuiMainWindow"))
        self.resize(1290, 890)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.GuiNetwork = Network(self.centralwidget, "Mesh", 9, 3, 8, 5000)
        network_size = self.calc_network_size()
        self.GuiNetwork.setMinimumSize(network_size)
        self.GuiNetwork.setObjectName(_fromUtf8("GuiNetworkFrame"))
        self.horizontalLayout.addWidget(self.GuiNetwork)

        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.GuiCoreSelectorCombo = QtGui.QComboBox(self.centralwidget)
        self.GuiCoreSelectorCombo.setObjectName(_fromUtf8("GuiCoreSelectorCombo"))
        self.GuiCoreSelectorCombo.activated.connect(self.close_view_core)
        self.core_selector_setup(networkAttr.CORE_CORES)
        self.verticalLayout.addWidget(self.GuiCoreSelectorCombo)

        self.GuiCoreExplodedView = CoreExploded(self.centralwidget, self.GuiNetwork.cores[0])
        self.GuiCoreExplodedView.setMinimumSize(QtCore.QSize(drawAttr.CORE_SIZE_EXP + 50,
                                                             drawAttr.CORE_SIZE_EXP + 50))
        self.GuiCoreExplodedView.setObjectName(_fromUtf8("GuiCoreExplodedView"))
        self.verticalLayout.addWidget(self.GuiCoreExplodedView)

        self.GuiCoreInfo = CoreInfo(self.centralwidget, self.GuiNetwork.cores[0])
        self.GuiCoreInfo.setObjectName(_fromUtf8("GuiCoreInfo"))
        self.verticalLayout.addWidget(self.GuiCoreInfo)

        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        # Pushbuttons
        self.GuiPreviousCyclePb = QtGui.QPushButton(self.centralwidget)
        self.GuiPreviousCyclePb.setObjectName(_fromUtf8("GuiPreviousCyclePb"))
        self.GuiPreviousCyclePb.clicked.connect(self.previous_cycle)
        self.horizontalLayout_2.addWidget(self.GuiPreviousCyclePb)
        self.GuiNextCyclePb = QtGui.QPushButton(self.centralwidget)
        self.GuiNextCyclePb.setObjectName(_fromUtf8("GuiNextCyclePb"))
        self.GuiNextCyclePb.clicked.connect(self.next_cycle)
        self.horizontalLayout_2.addWidget(self.GuiNextCyclePb)

        # LCD Cycle Counter
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.GuiCycleCounter = QtGui.QLCDNumber(self.centralwidget)
        self.GuiCycleCounter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.GuiCycleCounter.setObjectName(_fromUtf8("GuiCycleCounter"))
        self.verticalLayout.addWidget(self.GuiCycleCounter)

        # Cycle Progress Bar
        self.GuiCycleProgressBar = QtGui.QProgressBar(self.centralwidget)
        self.GuiCycleProgressBar.setProperty("value", 0)
        self.GuiCycleProgressBar.setObjectName(_fromUtf8("GuiCycleProgressBar"))
        self.verticalLayout.addWidget(self.GuiCycleProgressBar)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)

        # Menu Bar
        self.GuiMenuBar = QtGui.QMenuBar(self)
        self.GuiMenuBar.setGeometry(QtCore.QRect(0, 0, 1290, 21))
        self.GuiMenuBar.setObjectName(_fromUtf8("GuiMenuBar"))
        self.GuiFileMenu = QtGui.QMenu(self.GuiMenuBar)
        self.GuiFileMenu.setObjectName(_fromUtf8("GuiFileMenu"))
        self.GuiGoToMenu = QtGui.QMenu(self.GuiMenuBar)
        self.GuiGoToMenu.setObjectName(_fromUtf8("GuiGoToMenu"))
        self.GuiGarnetMenu = QtGui.QMenu(self.GuiMenuBar)
        self.GuiGarnetMenu.setObjectName(_fromUtf8("GuiGarnetMenu"))
        self.setMenuBar(self.GuiMenuBar)

        # Status Bar
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        # Menu Bar Items
        self.actionGo_To_Cycle = QtGui.QAction(self)
        self.actionGo_To_Cycle.setObjectName(_fromUtf8("actionGo_To_Cycle"))
        self.GuiGoTo0MenuAction = QtGui.QAction(self)
        self.GuiGoTo0MenuAction.triggered.connect(self.go_to_cycle_0)
        self.GuiGoTo0MenuAction.setObjectName(_fromUtf8("GuiGoTo0MenuAction"))
        self.GuiGoTo500MenuAction = QtGui.QAction(self)
        self.GuiGoTo500MenuAction.triggered.connect(self.go_to_cycle_500)
        self.GuiGoTo500MenuAction.setObjectName(_fromUtf8("GuiGoTo500MenuAction"))
        self.GuiGoToCycleMenuAction = QtGui.QAction(self)
        self.GuiGoToCycleMenuAction.triggered.connect(self.got_to_cycle_x)
        self.GuiGoToCycleMenuAction.setObjectName(_fromUtf8("GuiGoToCycleMenuAction"))
        self.GuiGarnetGenerateMenuAction = QtGui.QAction(self)
        self.GuiGarnetGenerateMenuAction.triggered.connect(self.garnet_generator)
        self.GuiGarnetGenerateMenuAction.setObjectName(_fromUtf8("GuiGarnetGenerateMenuAction"))
        self.GuiGarnetHelpMenuAction = QtGui.QAction(self)
        self.GuiGarnetHelpMenuAction.setShortcut("Ctrl+H")
        self.GuiGarnetHelpMenuAction.triggered.connect(self.garnet_help)
        self.GuiGarnetHelpMenuAction.setObjectName(_fromUtf8("GuiGarnetHelpMenuAction"))
        self.GuiFileOpenTraceMenuAction = QtGui.QAction(self)
        self.GuiFileOpenTraceMenuAction.setShortcut("Ctrl+O")
        self.GuiFileOpenTraceMenuAction.triggered.connect(self.file_open_trace)
        self.GuiFileOpenTraceMenuAction.setObjectName(_fromUtf8("GuiFileOpenTraceMenuAction"))
        self.GuiFileExitMenuAction = QtGui.QAction(self)
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

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "Loupe", None))
        self.GuiPreviousCyclePb.setText(_translate("self", "Previous Cycle", None))
        self.GuiNextCyclePb.setText(_translate("self", "Next Cycle", None))
        self.GuiFileMenu.setTitle(_translate("self", "File", None))
        self.GuiGoToMenu.setTitle(_translate("self", "Go To", None))
        self.GuiGarnetMenu.setTitle(_translate("self", "Garnet", None))
        self.actionGo_To_Cycle.setText(_translate("self", "Go To Cycle...", None))
        self.GuiGoTo0MenuAction.setText(_translate("self", "Cycle 0", None))
        self.GuiGoTo500MenuAction.setText(_translate("self", "Cycle 500", None))
        self.GuiGoToCycleMenuAction.setText(_translate("self", "Cycle ...", None))
        self.GuiGarnetGenerateMenuAction.setText(_translate("self", "Generate Garnet Run Command", None))
        self.GuiGarnetHelpMenuAction.setText(_translate("self", "Help", None))
        self.GuiFileOpenTraceMenuAction.setText(_translate("self", "Open Trace...", None))
        self.GuiFileExitMenuAction.setText(_translate("self", "Quit", None))

    def calc_network_size(self):
        width = networkAttr.CORE_COLS * drawAttr.CORE_SIZE \
                + (networkAttr.CORE_COLS - 1) * drawAttr.LINK_LENGTH + 10
        height = width - 8
        return QtCore.QSize(width, height)

    def next_cycle(self):
        print("next cycle")
        cycle_num = self.GuiNetwork.next_cycle()
        self.GuiCycleProgressBar.setValue(cycle_num / networkAttr.NET_TOTCYCLES * 100)
        self.GuiCycleCounter.display(cycle_num)

    def previous_cycle(self):
        print("previous cycle")
        cycle_num = self.GuiNetwork.prev_cycle()
        if cycle_num is None:
            pass
        else:
            self.GuiCycleProgressBar.setValue(cycle_num / networkAttr.NET_TOTCYCLES * 100)
            self.GuiCycleCounter.display(cycle_num)

    def core_selector_setup(self, core_num):
        for index in range(core_num):
            self.GuiCoreSelectorCombo.addItem(_fromUtf8(""))
            core_select_text = "Core " + str(index)
            self.GuiCoreSelectorCombo.setItemText(index, _translate("self", core_select_text, None))

    def close_view_core(self):
        core_num = self.GuiCoreSelectorCombo.currentIndex()
        print(core_num)
        self.GuiCoreExplodedView.update_core(self.GuiNetwork.cores[core_num])
        self.GuiCoreExplodedView.update()
        self.GuiCoreInfo.update_core_info(self.GuiNetwork.cores[core_num])
        self.GuiCoreInfo.update()

    def file_open_trace(self):
        dialog = QtGui.QFileDialog()
        name = QtGui.QFileDialog.getOpenFileName(dialog, 'Open File')
        file = open(name, 'r')

    def quit_application(self):
        print("Closing App...")
        sys.exit()

    def garnet_generator(self):
        print("Garnet")
        self.GuiGarnet = GuiGenerateGarnet()
        self.GuiGarnet.show()

    def garnet_help(self):
        print("Garnet Help")

    def go_to_cycle_0(self):
        cycle_num = self.GuiNetwork.go_to_cycle(0)
        if cycle_num is not None:
            self.GuiCycleProgressBar.setValue(cycle_num / networkAttr.NET_TOTCYCLES * 100)
            self.GuiCycleCounter.display(cycle_num)

    def go_to_cycle_500(self):
        cycle_num = self.GuiNetwork.go_to_cycle(500)
        if cycle_num is not None:
            self.GuiCycleProgressBar.setValue(cycle_num / networkAttr.NET_TOTCYCLES * 100)
            self.GuiCycleCounter.display(cycle_num)

    def got_to_cycle_x(self):
        input_dialog = QtGui.QInputDialog()
        text, ok = QtGui.QInputDialog.getText(input_dialog, 'Input Cycle Number', 'Enter Cycle:')
        if ok and int(text) >= 0:
            cycle_num = self.GuiNetwork.go_to_cycle(int(text))
            print(cycle_num)
            if cycle_num is not None:
                self.GuiCycleProgressBar.setValue(cycle_num / networkAttr.NET_TOTCYCLES * 100)
                self.GuiCycleCounter.display(cycle_num)

    def update_gui(self):
        self.GuiNetwork.update_network()
        core_num = self.GuiCoreSelectorCombo.currentIndex()
        self.GuiCoreInfo.update_core_info(self.GuiNetwork.cores[core_num])
        self.GuiCoreExplodedView.update_core(self.GuiNetwork.cores[core_num])

        self.GuiNetwork.update()
        self.GuiCoreExplodedView.update()
        self.GuiCoreInfo.update()
