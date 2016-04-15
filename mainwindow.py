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

        self.GuiGarnet = None
        # Main Layout
        self.setObjectName(_fromUtf8("GuiMainWindow"))
        self.resize(1260, 960)
        self.GuiWindowInternal = QtGui.QWidget(self)
        self.GuiWindowInternal.setObjectName(_fromUtf8("GuiWindowInternal"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.GuiWindowInternal)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        #Network and Progress Layout
        self.GuiFullNetworkLayout = QtGui.QVBoxLayout()
        self.GuiFullNetworkLayout.setObjectName(_fromUtf8("GuiFullNetworkLayout"))
        self.GuiCycleProgressLayout = QtGui.QHBoxLayout()
        self.GuiCycleProgressLayout.setObjectName(_fromUtf8("GuiCycleProgressLayout"))

        # LCD Cycle Counter
        self.GuiCycleCounter = QtGui.QLCDNumber(self.GuiWindowInternal)
        self.GuiCycleCounter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.GuiCycleCounter.setObjectName(_fromUtf8("GuiCycleCounter"))
        self.GuiCycleCounter.raise_()
        self.GuiCycleProgressLayout.addWidget(self.GuiCycleCounter)

        # Cycle Progress Bar
        self.GuiCycleProgressBar = QtGui.QProgressBar(self.GuiWindowInternal)
        self.GuiCycleProgressBar.setProperty("value", 0)
        self.GuiCycleProgressBar.setObjectName(_fromUtf8("GuiCycleProgressBar"))
        self.GuiCycleProgressLayout.addWidget(self.GuiCycleProgressBar)

        self.GuiFullNetworkLayout.addLayout(self.GuiCycleProgressLayout)
        #Network
        self.GuiNetwork = Network(self.GuiWindowInternal, "Mesh", 16, 4, 8, 5000)
        network_size = self.calc_network_size()
        self.GuiNetwork.setMinimumSize(network_size)
        self.GuiNetwork.setObjectName(_fromUtf8("GuiNetworkFrame"))
        self.GuiFullNetworkLayout.addWidget(self.GuiNetwork)
        self.horizontalLayout.addLayout(self.GuiFullNetworkLayout)
        #Side Bar Layout
        self.GuiSideBarMainLayout = QtGui.QVBoxLayout()
        self.GuiSideBarMainLayout.setObjectName(_fromUtf8("GuiSideBarMainLayout"))
        #Auto Cycle Label
        self.GuiAutoCycleLabel = QtGui.QLabel(self.GuiWindowInternal)
        self.GuiAutoCycleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuiAutoCycleLabel.setObjectName(_fromUtf8("GuiAutoCycleLabel"))
        self.GuiSideBarMainLayout.addWidget(self.GuiAutoCycleLabel)
        self.GuiAutoCycleLayout = QtGui.QHBoxLayout()
        self.GuiAutoCycleLayout.setObjectName(_fromUtf8("GuiAutoCycleLayout"))
        #Auto Cycle Text Entry
        self.GuiAutoCycleCycleEntry = QtGui.QLineEdit(self.GuiWindowInternal)
        self.GuiAutoCycleCycleEntry.setMaximumSize(QtCore.QSize(100, 16777215))
        self.GuiAutoCycleCycleEntry.setText(_fromUtf8(""))
        self.GuiAutoCycleCycleEntry.setObjectName(_fromUtf8("GuiAutoCycleCycleEntry"))
        self.GuiAutoCycleLayout.addWidget(self.GuiAutoCycleCycleEntry)
        #Auto Cycle Start
        self.GuiAutoCycleStart = QtGui.QPushButton(self.GuiWindowInternal)
        self.GuiAutoCycleStart.setObjectName(_fromUtf8("GuiAutoCycleStart"))
        self.GuiAutoCycleLayout.addWidget(self.GuiAutoCycleStart)
        self.GuiAutoCycleStop = QtGui.QPushButton(self.GuiWindowInternal)
        #Auto Cycle Stop
        self.GuiAutoCycleStop.setObjectName(_fromUtf8("GuiAutoCycleStop"))
        self.GuiAutoCycleLayout.addWidget(self.GuiAutoCycleStop)

        self.GuiSideBarMainLayout.addLayout(self.GuiAutoCycleLayout)
        #Manual Cycle Label
        self.GuiManualCycleLabel = QtGui.QLabel(self.GuiWindowInternal)
        self.GuiManualCycleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuiManualCycleLabel.setObjectName(_fromUtf8("GuiManualCycleLabel"))
        self.GuiSideBarMainLayout.addWidget(self.GuiManualCycleLabel)

        self.GuiManualCycleLayout = QtGui.QHBoxLayout()
        self.GuiManualCycleLayout.setObjectName(_fromUtf8("GuiManualCycleLayout"))
        # Manual Cycle Previous PB
        self.GuiPreviousCyclePb = QtGui.QPushButton(self.GuiWindowInternal)
        self.GuiPreviousCyclePb.setObjectName(_fromUtf8("GuiPreviousCyclePb"))
        self.GuiPreviousCyclePb.clicked.connect(self.previous_cycle)
        self.GuiManualCycleLayout.addWidget(self.GuiPreviousCyclePb)
        # Manual Cycle Next PB
        self.GuiNextCyclePb = QtGui.QPushButton(self.GuiWindowInternal)
        self.GuiNextCyclePb.setObjectName(_fromUtf8("GuiNextCyclePb"))
        self.GuiNextCyclePb.clicked.connect(self.next_cycle)
        self.GuiManualCycleLayout.addWidget(self.GuiNextCyclePb)

        self.GuiSideBarMainLayout.addLayout(self.GuiManualCycleLayout)
        #VN Select Label
        self.GuiVirtualNetworkSelectLabel = QtGui.QLabel(self.GuiWindowInternal)
        self.GuiVirtualNetworkSelectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuiVirtualNetworkSelectLabel.setObjectName(_fromUtf8("GuiVirtualNetworkSelectLabel"))
        self.GuiSideBarMainLayout.addWidget(self.GuiVirtualNetworkSelectLabel)

        #Virtual Network Select Box
        self.GuiVNSelectCombo = QtGui.QComboBox(self.GuiWindowInternal)
        self.GuiVNSelectCombo.setObjectName(_fromUtf8("GuiVNSelectCombo"))
        self.GuiVNSelectCombo.addItem(_fromUtf8(""))
        self.GuiVNSelectCombo.addItem(_fromUtf8(""))
        self.GuiSideBarMainLayout.addWidget(self.GuiVNSelectCombo)
        #Close Up Core LAbel
        self.GuiCloseUpCoreLabel = QtGui.QLabel(self.GuiWindowInternal)
        self.GuiCloseUpCoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuiCloseUpCoreLabel.setObjectName(_fromUtf8("GuiCloseUpCoreLabel"))
        self.GuiSideBarMainLayout.addWidget(self.GuiCloseUpCoreLabel)
        #Core Selection Box
        self.GuiCoreSelectorCombo = QtGui.QComboBox(self.GuiWindowInternal)
        self.GuiCoreSelectorCombo.setObjectName(_fromUtf8("GuiCoreSelectorCombo"))
        self.GuiCoreSelectorCombo.activated.connect(self.close_view_core)
        self.core_selector_setup(networkAttr.CORE_CORES)
        self.GuiSideBarMainLayout.addWidget(self.GuiCoreSelectorCombo)
        #Core Exploded View Box
        self.GuiCoreExplodedView = CoreExploded(self.GuiWindowInternal, self.GuiNetwork.cores[0])
        self.GuiCoreExplodedView.setMinimumSize(QtCore.QSize(drawAttr.CORE_SIZE_EXP + 50, drawAttr.CORE_SIZE_EXP + 50))
        self.GuiCoreExplodedView.setObjectName(_fromUtf8("GuiCoreExplodedView"))
        self.GuiSideBarMainLayout.addWidget(self.GuiCoreExplodedView)
        #Core Information
        self.GuiCoreInfo = CoreInfo(self.GuiWindowInternal, self.GuiNetwork.cores[0])
        self.GuiCoreInfo.setObjectName(_fromUtf8("GuiCoreInfo"))
        self.GuiSideBarMainLayout.addWidget(self.GuiCoreInfo)
        # Buffer Label
        self.GuiBufferLabel = QtGui.QLabel(self.GuiWindowInternal)
        self.GuiBufferLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuiBufferLabel.setObjectName(_fromUtf8("GuiBufferLabel"))
        self.GuiSideBarMainLayout.addWidget(self.GuiBufferLabel)
        #Buffer Select Combo Box
        self.GuiBufferSelectCombo = QtGui.QComboBox(self.GuiWindowInternal)
        self.GuiBufferSelectCombo.setObjectName(_fromUtf8("GuiBufferSelectCombo"))
        self.GuiBufferSelectCombo.addItem(_fromUtf8(""))
        self.GuiBufferSelectCombo.addItem(_fromUtf8(""))
        self.GuiBufferSelectCombo.addItem(_fromUtf8(""))
        self.GuiBufferSelectCombo.addItem(_fromUtf8(""))
        self.GuiBufferSelectCombo.addItem(_fromUtf8(""))
        self.GuiSideBarMainLayout.addWidget(self.GuiBufferSelectCombo)
        #VC Top Table
        self.GuiVCTopTable = QtGui.QTableWidget(self.GuiWindowInternal)
        self.GuiVCTopTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.GuiVCTopTable.setProperty("showDropIndicator", False)
        self.GuiVCTopTable.setDragDropOverwriteMode(False)
        self.GuiVCTopTable.setAlternatingRowColors(False)
        self.GuiVCTopTable.setShowGrid(True)
        self.GuiVCTopTable.setObjectName(_fromUtf8("GuiVCTopTable"))
        self.GuiVCTopTable.setColumnCount(4)
        self.GuiVCTopTable.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.GuiVCTopTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCTopTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCTopTable.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCTopTable.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCTopTable.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCTopTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCTopTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCTopTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCTopTable.setHorizontalHeaderItem(3, item)
        self.GuiSideBarMainLayout.addWidget(self.GuiVCTopTable)
        #VC Bottom Table
        self.GuiVCBottomTable = QtGui.QTableWidget(self.GuiWindowInternal)
        self.GuiVCBottomTable.setAutoScroll(True)
        self.GuiVCBottomTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.GuiVCBottomTable.setDragDropOverwriteMode(False)
        self.GuiVCBottomTable.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.GuiVCBottomTable.setAlternatingRowColors(False)
        self.GuiVCBottomTable.setShowGrid(True)
        self.GuiVCBottomTable.setObjectName(_fromUtf8("GuiVCBottomTable"))
        self.GuiVCBottomTable.setColumnCount(4)
        self.GuiVCBottomTable.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.GuiVCBottomTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCBottomTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCBottomTable.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCBottomTable.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCBottomTable.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCBottomTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCBottomTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCBottomTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.GuiVCBottomTable.setHorizontalHeaderItem(3, item)
        self.GuiSideBarMainLayout.addWidget(self.GuiVCBottomTable)

        self.horizontalLayout.addLayout(self.GuiSideBarMainLayout)
        self.setCentralWidget(self.GuiWindowInternal)

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
        self.GuiVirtualNetworkSelectLabel.setText(_translate("GuiMainWindow", "Virtual Network Select", None))
        self.GuiCloseUpCoreLabel.setText(_translate("GuiMainWindow", "Close-Up Core View", None))
        self.GuiBufferLabel.setText(_translate("GuiMainWindow", "Buffer Information", None))
        self.GuiVNSelectCombo.setItemText(0, _translate("GuiMainWindow", "Virtual Network 0", None))
        self.GuiVNSelectCombo.setItemText(1, _translate("GuiMainWindow", "Virtual Network 1", None))
        self.GuiCoreSelectorCombo.setItemText(0, _translate("GuiMainWindow", "Core 0", None))
        self.GuiCoreSelectorCombo.setItemText(1, _translate("GuiMainWindow", "Core 1", None))
        self.GuiBufferSelectCombo.setItemText(0, _translate("GuiMainWindow", "North Buffer", None))
        self.GuiBufferSelectCombo.setItemText(1, _translate("GuiMainWindow", "East Buffer", None))
        self.GuiBufferSelectCombo.setItemText(2, _translate("GuiMainWindow", "South Buffer", None))
        self.GuiBufferSelectCombo.setItemText(3, _translate("GuiMainWindow", "West Buffer", None))
        self.GuiBufferSelectCombo.setItemText(4, _translate("GuiMainWindow", "Core Buffer", None))
        item = self.GuiVCTopTable.verticalHeaderItem(0)
        item.setText(_translate("GuiMainWindow", "Flit Id", None))
        item = self.GuiVCTopTable.verticalHeaderItem(1)
        item.setText(_translate("GuiMainWindow", "Flit Type", None))
        item = self.GuiVCTopTable.verticalHeaderItem(2)
        item.setText(_translate("GuiMainWindow", "Flit Route", None))
        item = self.GuiVCTopTable.verticalHeaderItem(3)
        item.setText(_translate("GuiMainWindow", "Flit Outport", None))
        item = self.GuiVCTopTable.verticalHeaderItem(4)
        item.setText(_translate("GuiMainWindow", "Flit Src Delay", None))
        item = self.GuiVCTopTable.horizontalHeaderItem(0)
        item.setText(_translate("GuiMainWindow", "VC 0", None))
        item = self.GuiVCTopTable.horizontalHeaderItem(1)
        item.setText(_translate("GuiMainWindow", "VC 1", None))
        item = self.GuiVCTopTable.horizontalHeaderItem(2)
        item.setText(_translate("GuiMainWindow", "VC 2", None))
        item = self.GuiVCTopTable.horizontalHeaderItem(3)
        item.setText(_translate("GuiMainWindow", "VC 3", None))
        item = self.GuiVCBottomTable.verticalHeaderItem(0)
        item.setText(_translate("GuiMainWindow", "Flit Id", None))
        item = self.GuiVCBottomTable.verticalHeaderItem(1)
        item.setText(_translate("GuiMainWindow", "Flit Type", None))
        item = self.GuiVCBottomTable.verticalHeaderItem(2)
        item.setText(_translate("GuiMainWindow", "Flit Route", None))
        item = self.GuiVCBottomTable.verticalHeaderItem(3)
        item.setText(_translate("GuiMainWindow", "Flit Outport", None))
        item = self.GuiVCBottomTable.verticalHeaderItem(4)
        item.setText(_translate("GuiMainWindow", "Flit Src Delay", None))
        item = self.GuiVCBottomTable.horizontalHeaderItem(0)
        item.setText(_translate("GuiMainWindow", "VC 4", None))
        item = self.GuiVCBottomTable.horizontalHeaderItem(1)
        item.setText(_translate("GuiMainWindow", "VC 5", None))
        item = self.GuiVCBottomTable.horizontalHeaderItem(2)
        item.setText(_translate("GuiMainWindow", "VC 6", None))
        item = self.GuiVCBottomTable.horizontalHeaderItem(3)
        item.setText(_translate("GuiMainWindow", "VC 7", None))
        self.GuiAutoCycleLabel.setText(_translate("GuiMainWindow", "Animation/Auto Cycle", None))
        self.GuiAutoCycleStart.setText(_translate("GuiMainWindow", "Start", None))
        self.GuiAutoCycleStop.setText(_translate("GuiMainWindow", "Stop", None))
        self.GuiManualCycleLabel.setText(_translate("GuiMainWindow", "Manual Cycle", None))
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
