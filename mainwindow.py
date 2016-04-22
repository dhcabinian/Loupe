from PyQt4 import QtGui, QtCore
from network import Network
from networkAttr import networkAttr
from drawAttr import drawAttr
from CoreExploded import CoreExploded
from BuffInfo import BuffInfo
from generateGarnet import GuiGenerateGarnet
from traceParser import traceParser
import sys
import threading


# import time


class GuiMainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(GuiMainWindow, self).__init__()
        self.setup()

    def setup(self):
        self.GuiGarnet = None
        self.timer = None
        self.autoCycle = False
        self.trace_parser = traceParser()
        self.setup_main_window()
        self.setup_main_layout()
        self.setup_menu_bar()
        self.setup_status_bar()

        QtCore.QMetaObject.connectSlotsByName(self)

    def setup_main_window(self):
        # Main Layout
        self.setObjectName("GuiMainWindow")
        self.setWindowTitle("Loupe")
        self.setWindowIcon(QtGui.QIcon('Loupe_icon.png'))
        self.resize(1260, 960)

    def setup_main_layout(self):
        self.GuiWindowInternal = QtGui.QWidget(self)
        self.GuiWindowInternal.setObjectName("GuiWindowInternal")
        self.horizontalLayout = QtGui.QHBoxLayout(self.GuiWindowInternal)
        self.horizontalLayout.setObjectName("horizontalLayout")

    def setup_menu_bar(self):
        # Menu Bar
        self.GuiMenuBar = QtGui.QMenuBar(self)
        self.GuiMenuBar.setGeometry(QtCore.QRect(0, 0, 1290, 21))
        self.GuiMenuBar.setObjectName("GuiMenuBar")
        self.GuiFileMenu = QtGui.QMenu(self.GuiMenuBar)
        self.GuiFileMenu.setObjectName("GuiFileMenu")
        self.GuiFileMenu.setTitle("File")
        self.GuiGoToMenu = QtGui.QMenu(self.GuiMenuBar)
        self.GuiGoToMenu.setObjectName("GuiGoToMenu")
        self.GuiGoToMenu.setTitle("Go To")
        self.GuiGarnetMenu = QtGui.QMenu(self.GuiMenuBar)
        self.GuiGarnetMenu.setObjectName("GuiGarnetMenu")
        self.GuiGarnetMenu.setTitle("Garnet")
        self.setMenuBar(self.GuiMenuBar)

        # Menu Bar Items
        self.actionGo_To_Cycle = QtGui.QAction(self)
        self.actionGo_To_Cycle.setObjectName("actionGo_To_Cycle")
        self.actionGo_To_Cycle.setText("Go To Cycle...")
        self.GuiGoTo0MenuAction = QtGui.QAction(self)
        self.GuiGoTo0MenuAction.triggered.connect(self.go_to_cycle_0)
        self.GuiGoTo0MenuAction.setObjectName("GuiGoTo0MenuAction")
        self.GuiGoTo0MenuAction.setText("Cycle 0")
        self.GuiGoTo500MenuAction = QtGui.QAction(self)
        self.GuiGoTo500MenuAction.triggered.connect(self.go_to_cycle_500)
        self.GuiGoTo500MenuAction.setObjectName("GuiGoTo500MenuAction")
        self.GuiGoTo500MenuAction.setText("Cycle 500")
        self.GuiGoToCycleMenuAction = QtGui.QAction(self)
        self.GuiGoToCycleMenuAction.triggered.connect(self.go_to_cycle_x)
        self.GuiGoToCycleMenuAction.setObjectName("GuiGoToCycleMenuAction")
        self.GuiGoToCycleMenuAction.setText("Cycle ...")
        self.GuiGarnetGenerateMenuAction = QtGui.QAction(self)
        self.GuiGarnetGenerateMenuAction.triggered.connect(self.garnet_generator)
        self.GuiGarnetGenerateMenuAction.setObjectName("GuiGarnetGenerateMenuAction")
        self.GuiGarnetGenerateMenuAction.setText("Generate Garnet Run Command")
        self.GuiGarnetHelpMenuAction = QtGui.QAction(self)
        self.GuiGarnetHelpMenuAction.setShortcut("Ctrl+H")
        self.GuiGarnetHelpMenuAction.triggered.connect(self.garnet_help)
        self.GuiGarnetHelpMenuAction.setObjectName("GuiGarnetHelpMenuAction")
        self.GuiGarnetHelpMenuAction.setText("Help")
        self.GuiFileOpenTraceMenuAction = QtGui.QAction(self)
        self.GuiFileOpenTraceMenuAction.setShortcut("Ctrl+O")
        self.GuiFileOpenTraceMenuAction.triggered.connect(self.file_open_trace)
        self.GuiFileOpenTraceMenuAction.setObjectName("GuiFileOpenTraceMenuAction")
        self.GuiFileOpenTraceMenuAction.setText("Open Trace...")
        self.GuiFileExitMenuAction = QtGui.QAction(self)
        self.GuiFileExitMenuAction.setShortcut("Ctrl+Q")
        self.GuiFileExitMenuAction.triggered.connect(self.quit_application)
        self.GuiFileExitMenuAction.setObjectName("GuiFileExitMenuAction")
        self.GuiFileExitMenuAction.setText("Quit")

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

    def setup_status_bar(self):
        # Status Bar
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def inital_setup(self):
        net_info = self.trace_parser.get_network_info()
        self.setup_full_network_layout()
        self.setup_cycle_progress_layout()
        self.setup_lcd_cycle()
        self.setup_progress_bar_cycle()
        self.setup_network(net_info)
        self.setup_sidebar_layout()
        self.setup_auto_cycle_label()
        self.setup_auto_cycle_layout()
        self.setup_auto_cycle_text()
        self.setup_auto_cycle_start()
        self.setup_auto_cycle_stop()
        self.setup_manual_cycle_label()
        self.setup_manual_cycle_layout()
        self.setup_manual_cycle_prev()
        self.setup_manual_cycle_next()
        self.setup_vn_select_label()
        self.setup_vn_select_box(net_info)
        self.setup_close_core_label()
        self.setup_close_core_box()
        self.setup_close_core_view()
        self.setup_buffer_label()
        self.setup_buffer_box()
        self.setup_buffer_tables()

    def setup_full_network_layout(self):
        # Network and Progress Layout
        self.GuiFullNetworkLayout = QtGui.QVBoxLayout()
        self.GuiFullNetworkLayout.setObjectName("GuiFullNetworkLayout")
        self.horizontalLayout.addLayout(self.GuiFullNetworkLayout)

    def setup_cycle_progress_layout(self):
        self.GuiCycleProgressLayout = QtGui.QHBoxLayout()
        self.GuiCycleProgressLayout.setObjectName("GuiCycleProgressLayout")
        self.GuiFullNetworkLayout.addLayout(self.GuiCycleProgressLayout)

    def setup_lcd_cycle(self):
        # LCD Cycle Counter
        self.GuiCycleCounter = QtGui.QLCDNumber(self.GuiWindowInternal)
        self.GuiCycleCounter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.GuiCycleCounter.setObjectName("GuiCycleCounter")
        self.GuiCycleCounter.raise_()
        self.GuiCycleCounter.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.GuiCycleCounter.setPalette(QtGui.QPalette(QtGui.QColor("Black")))
        self.GuiCycleCounter.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.GuiCycleProgressLayout.addWidget(self.GuiCycleCounter)

    def setup_progress_bar_cycle(self):
        # Cycle Progress Bar
        self.GuiCycleProgressBar = QtGui.QProgressBar(self.GuiWindowInternal)
        self.GuiCycleProgressBar.setProperty("value", 0)
        self.GuiCycleProgressBar.setObjectName("GuiCycleProgressBar")
        self.GuiCycleProgressLayout.addWidget(self.GuiCycleProgressBar)

    def setup_network(self, net_info):
        # Network
        self.GuiNetwork = Network(self.GuiWindowInternal, "Mesh", net_info[0], net_info[1], net_info[2], net_info[4])
        network_size = self.init_calc_network_size()
        self.GuiNetwork.setMinimumSize(network_size)
        self.GuiNetwork.setObjectName("GuiNetworkFrame")
        self.GuiFullNetworkLayout.addWidget(self.GuiNetwork)

    def setup_sidebar_layout(self):
        # Side Bar Layout
        self.GuiSideBarMainLayout = QtGui.QVBoxLayout()
        self.GuiSideBarMainLayout.setObjectName("GuiSideBarMainLayout")
        self.horizontalLayout.addLayout(self.GuiSideBarMainLayout)
        self.setCentralWidget(self.GuiWindowInternal)

    def setup_auto_cycle_label(self):
        # Auto Cycle Label
        self.GuiAutoCycleLabel = QtGui.QLabel(self.GuiWindowInternal)
        self.GuiAutoCycleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuiAutoCycleLabel.setObjectName("GuiAutoCycleLabel")
        self.GuiSideBarMainLayout.addWidget(self.GuiAutoCycleLabel)
        self.GuiAutoCycleLabel.setText("Animation/Auto Cycle")

    def setup_auto_cycle_layout(self):
        self.GuiAutoCycleLayout = QtGui.QHBoxLayout()
        self.GuiAutoCycleLayout.setObjectName("GuiAutoCycleLayout")
        self.GuiSideBarMainLayout.addLayout(self.GuiAutoCycleLayout)

    def setup_auto_cycle_text(self):
        # Auto Cycle Text Entry
        self.GuiAutoCycleCycleEntry = QtGui.QLineEdit(self.GuiWindowInternal)
        self.GuiAutoCycleCycleEntry.setMaximumSize(QtCore.QSize(100, 16777215))
        self.GuiAutoCycleCycleEntry.setText("")
        self.GuiAutoCycleCycleEntry.setObjectName("GuiAutoCycleCycleEntry")
        self.GuiAutoCycleLayout.addWidget(self.GuiAutoCycleCycleEntry)

    def setup_auto_cycle_start(self):
        # Auto Cycle Start
        self.GuiAutoCycleStart = QtGui.QPushButton(self.GuiWindowInternal)
        self.GuiAutoCycleStart.setObjectName("GuiAutoCycleStart")
        self.GuiAutoCycleStart.clicked.connect(self.act_start_cycle)
        self.GuiAutoCycleLayout.addWidget(self.GuiAutoCycleStart)
        self.GuiAutoCycleStart.setText("Start")

    def setup_auto_cycle_stop(self):
        # Auto Cycle Stop
        self.GuiAutoCycleStop = QtGui.QPushButton(self.GuiWindowInternal)
        self.GuiAutoCycleStop.setObjectName("GuiAutoCycleStop")
        self.GuiAutoCycleStop.clicked.connect(self.act_stop_cycle)
        self.GuiAutoCycleLayout.addWidget(self.GuiAutoCycleStop)
        self.GuiAutoCycleStop.setText("Stop")

    def setup_manual_cycle_label(self):
        # Manual Cycle Label
        self.GuiManualCycleLabel = QtGui.QLabel(self.GuiWindowInternal)
        self.GuiManualCycleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuiManualCycleLabel.setObjectName("GuiManualCycleLabel")
        self.GuiSideBarMainLayout.addWidget(self.GuiManualCycleLabel)
        self.GuiManualCycleLabel.setText("Manual Cycle")

    def setup_manual_cycle_layout(self):
        self.GuiManualCycleLayout = QtGui.QHBoxLayout()
        self.GuiManualCycleLayout.setObjectName("GuiManualCycleLayout")
        self.GuiSideBarMainLayout.addLayout(self.GuiManualCycleLayout)

    def setup_manual_cycle_prev(self):
        # Manual Cycle Previous PB
        self.GuiPreviousCyclePb = QtGui.QPushButton(self.GuiWindowInternal)
        self.GuiPreviousCyclePb.setObjectName("GuiPreviousCyclePb")
        self.GuiPreviousCyclePb.clicked.connect(self.act_previous_cycle)
        self.GuiManualCycleLayout.addWidget(self.GuiPreviousCyclePb)
        self.GuiPreviousCyclePb.setText("Previous Cycle")

    def setup_manual_cycle_next(self):
        # Manual Cycle Next PB
        self.GuiNextCyclePb = QtGui.QPushButton(self.GuiWindowInternal)
        self.GuiNextCyclePb.setObjectName("GuiNextCyclePb")
        self.GuiNextCyclePb.clicked.connect(self.act_next_cycle)
        self.GuiManualCycleLayout.addWidget(self.GuiNextCyclePb)
        self.GuiNextCyclePb.setText("Next Cycle")

    def setup_vn_select_label(self):
        # VN Select Label
        self.GuiVirtualNetworkSelectLabel = QtGui.QLabel(self.GuiWindowInternal)
        self.GuiVirtualNetworkSelectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuiVirtualNetworkSelectLabel.setObjectName("GuiVirtualNetworkSelectLabel")
        self.GuiSideBarMainLayout.addWidget(self.GuiVirtualNetworkSelectLabel)
        self.GuiVirtualNetworkSelectLabel.setText("Virtual Network Select")

    def setup_vn_select_box(self, net_info):
        # Virtual Network Select Box
        self.GuiVNSelectCombo = QtGui.QComboBox(self.GuiWindowInternal)
        self.GuiVNSelectCombo.setObjectName("GuiVNSelectCombo")
        self.GuiVNSelectCombo.activated.connect(self.act_vn_select)
        self.GuiSideBarMainLayout.addWidget(self.GuiVNSelectCombo)
        self.init_vn_select_box(net_info[3])

    def setup_close_core_label(self):
        # Close Up Core LAbel
        self.GuiCloseUpCoreLabel = QtGui.QLabel(self.GuiWindowInternal)
        self.GuiCloseUpCoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuiCloseUpCoreLabel.setObjectName("GuiCloseUpCoreLabel")
        self.GuiSideBarMainLayout.addWidget(self.GuiCloseUpCoreLabel)
        self.GuiCloseUpCoreLabel.setText("Close-Up Core View")

    def setup_close_core_box(self):
        # Core Selection Box
        self.GuiCoreSelectorCombo = QtGui.QComboBox(self.GuiWindowInternal)
        self.GuiCoreSelectorCombo.setObjectName("GuiCoreSelectorCombo")
        self.GuiCoreSelectorCombo.activated.connect(self.act_close_view_core)
        self.init_close_core_box(networkAttr.CORE_CORES)
        self.GuiSideBarMainLayout.addWidget(self.GuiCoreSelectorCombo)

    def setup_close_core_view(self):
        # Core Exploded View Box
        self.GuiCoreExplodedView = CoreExploded(self.GuiWindowInternal, self.GuiNetwork.cores[0])
        self.GuiCoreExplodedView.setMinimumSize(QtCore.QSize(drawAttr.CORE_SIZE_EXP + 50, drawAttr.CORE_SIZE_EXP + 50))
        self.GuiCoreExplodedView.setObjectName("GuiCoreExplodedView")
        self.GuiSideBarMainLayout.addWidget(self.GuiCoreExplodedView)

    def setup_buffer_label(self):
        # Buffer Label
        self.GuiBufferLabel = QtGui.QLabel(self.GuiWindowInternal)
        self.GuiBufferLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuiBufferLabel.setObjectName("GuiBufferLabel")
        self.GuiSideBarMainLayout.addWidget(self.GuiBufferLabel)
        self.GuiBufferLabel.setText("Buffer Information")

    def setup_buffer_box(self):
        # Buffer Select Combo Box
        self.GuiBufferSelectCombo = QtGui.QComboBox(self.GuiWindowInternal)
        self.GuiBufferSelectCombo.setObjectName("GuiBufferSelectCombo")
        self.GuiBufferSelectCombo.activated.connect(self.act_buffer_select)
        self.init_buffer_box(self.GuiNetwork.cores[self.GuiCoreSelectorCombo.currentIndex()])
        self.GuiSideBarMainLayout.addWidget(self.GuiBufferSelectCombo)

    def setup_buffer_tables(self):
        self.BuffInfo = BuffInfo()
        if networkAttr.CORE_VCS > 0:
            # VC Top Table
            self.GuiVCTopTable = QtGui.QTableWidget(self.GuiWindowInternal)
            self.GuiVCTopTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            self.GuiVCTopTable.setProperty("showDropIndicator", False)
            self.GuiVCTopTable.setDragDropOverwriteMode(False)
            self.GuiVCTopTable.setAlternatingRowColors(False)
            self.GuiVCTopTable.setShowGrid(True)
            self.GuiVCTopTable.setObjectName("GuiVCTopTable")
            self.GuiSideBarMainLayout.addWidget(self.GuiVCTopTable)
            self.BuffInfo.set_top_table(self.GuiVCTopTable)
        if networkAttr.CORE_VCS > 4:
            # VC Bottom Table
            self.GuiVCBottomTable = QtGui.QTableWidget(self.GuiWindowInternal)
            self.GuiVCBottomTable.setAutoScroll(True)
            self.GuiVCBottomTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            self.GuiVCBottomTable.setDragDropOverwriteMode(False)
            self.GuiVCBottomTable.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
            self.GuiVCBottomTable.setAlternatingRowColors(False)
            self.GuiVCBottomTable.setShowGrid(True)
            self.GuiVCBottomTable.setObjectName("GuiVCBottomTable")
            self.GuiSideBarMainLayout.addWidget(self.GuiVCBottomTable)
            self.BuffInfo.set_bottom_table(self.GuiVCBottomTable)

        self.BuffInfo.setup_vc_tables(self.GuiVCTopTable, "Top")
        self.BuffInfo.setup_vc_tables(self.GuiVCBottomTable, "Bottom")

    def init_calc_network_size(self):
        width = networkAttr.CORE_COLS * drawAttr.CORE_SIZE \
                + (networkAttr.CORE_COLS - 1) * drawAttr.LINK_LENGTH + 10
        height = width - 8
        return QtCore.QSize(width, height)

    def init_close_core_box(self, core_num):
        for index in range(core_num):
            self.GuiCoreSelectorCombo.addItem("")
            core_select_text = "Core " + str(index)
            self.GuiCoreSelectorCombo.setItemText(index, core_select_text)

    def init_vn_select_box(self, vns):
        for index in range(vns):
            self.GuiVNSelectCombo.addItem("")
            vn_select_text = "Virtual Network " + str(index)
            self.GuiVNSelectCombo.setItemText(index, vn_select_text)

    def init_buffer_box(self, core):
        self.GuiBufferSelectCombo.clear()
        for index, buf in enumerate(core.get_buffers()):
            self.GuiBufferSelectCombo.addItem("")
            text = buf.link_dir.title() + " Buffer"
            self.GuiBufferSelectCombo.setItemText(index, text)

    # Update Gui Methods #
    def update_tables(self):
        # Get correct buffer info
        core = self.GuiNetwork.get_core(self.GuiCoreSelectorCombo.currentIndex())
        buffer = core.get_buffer(self.GuiBufferSelectCombo.currentText().split()[0])
        if buffer is not None:
            self.BuffInfo.update_tables(buffer)

    # # Updates the following: # #
    # # Cycle Progress Bar
    # # Cycle Counter
    # # Network
    # # Buffer Tables
    def update_cycle(self, cycle_num):
        updated_router_flits, updated_link_flits = self.trace_parser.get_cycle(cycle_num)
        self.GuiCycleProgressBar.setValue(cycle_num / networkAttr.NET_TOTCYCLES * 100)
        self.GuiCycleCounter.display(cycle_num)
        self.GuiNetwork.update_network(updated_router_flits, updated_link_flits)
        self.update_tables()

    # Action Methods

    # # Cycle Push Buttons # #

    def act_start_cycle(self):
        self.autoCycle = True
        if self.timer is None:
            self.timer = threading.Timer(2.0, self.act_next_cycle)
        while self.autoCycle:
            # self.timer.
            print("Start")

    # def printit():
    #     threading.Timer(5.0, printit).start()
    #     print
    #     "Hello, World!"
    #
    # printit()

    def act_stop_cycle(self):
        self.autoCycle = False
        if self.timer is None:
            pass
        else:
            self.timer.cancel()
        print("Stop")

    def act_previous_cycle(self):
        print("previous cycle")
        cycle_num = self.GuiNetwork.prev_cycle()
        if cycle_num is None:
            pass
        else:
            self.update_cycle(cycle_num)

    def act_next_cycle(self):
        cycle_num = self.GuiNetwork.next_cycle()
        if cycle_num is None:
            pass
        else:
            print("next cycle" + str(cycle_num))
            self.update_cycle(cycle_num)

    def act_vn_select(self):
        print(self.GuiVNSelectCombo.currentText())

    def act_close_view_core(self):
        core_num = self.GuiCoreSelectorCombo.currentIndex()
        print(core_num)
        self.GuiCoreExplodedView.update_core(self.GuiNetwork.cores[core_num])
        self.GuiCoreExplodedView.update()

    def act_buffer_select(self):
        buff_index = self.GuiCoreSelectorCombo.currentIndex()
        buff_text = self.GuiBufferSelectCombo.currentText()
        print(buff_text)
        self.BuffInfo.update_tables(buff_index)

    # Menu Bar Methods #

    # # File Methods # #
    def quit_application(self):
        print("Closing App...")
        sys.exit()

    def file_open_trace(self):
        dialog = QtGui.QFileDialog()
        name = QtGui.QFileDialog.getOpenFileName(dialog, 'Open File')
        if name.endswith('.csv'):
            self.file_loading_message()
            self.trace_parser.open_trace(name)
            self.file_loaded_message()
            self.inital_setup()
        else:
            self.file_open_error_message()

    def file_open_error_message(self):
        message = QtGui.QMessageBox()
        message.setWindowTitle("Error opening file")
        message.setText("File selected must be a .csv")
        message.setIcon(QtGui.QMessageBox.Warning)
        message.exec_()

    def file_loading_message(self):
        message = QtGui.QMessageBox()
        message.setWindowTitle("Loading Trace....")
        message.setText("Please wait a moment while indexing of the trace occurs")
        message.setIcon(QtGui.QMessageBox.Information)
        message.exec_()

    def file_loaded_message(self):
        message = QtGui.QMessageBox()
        message.setWindowTitle("Trace Loaded!")
        message.setText("Trace was succesfully loaded!")
        message.setIcon(QtGui.QMessageBox.Information)
        message.exec_()

    # # Garnet Methods # #
    def garnet_generator(self):
        print("Garnet")
        self.GuiGarnet = GuiGenerateGarnet()
        self.GuiGarnet.show()

    def garnet_help(self):
        print("Garnet Help")

    # # Cycle Methods # #
    def go_to_cycle_0(self):
        cycle_num = self.GuiNetwork.go_to_cycle(0)
        if cycle_num is not None:
            self.update_cycle(cycle_num)
        else:
            self.go_to_cycle_error()

    def go_to_cycle_500(self):
        cycle_num = self.GuiNetwork.go_to_cycle(500)
        if cycle_num is not None:
            self.update_cycle(cycle_num)
        else:
            self.go_to_cycle_error()

    def go_to_cycle_x(self):
        input_dialog = QtGui.QInputDialog()
        text, ok = QtGui.QInputDialog.getText(input_dialog, 'Input Cycle Number', 'Enter Cycle:')
        if ok and int(text) >= 0:
            cycle_num = self.GuiNetwork.go_to_cycle(int(text))
            print(cycle_num)
            if cycle_num is not None:
                self.update_cycle(cycle_num)
            else:
                self.go_to_cycle_error()

    def go_to_cycle_error(self):
        message = QtGui.QMessageBox()
        message.setWindowTitle("Invalid Cycle Number")
        string = "Cycle number must be in between 0 - " + str(networkAttr.NET_TOTCYCLES) + "\n"
        message.setText(string)
        message.setIcon(QtGui.QMessageBox.Warning)
        message.exec_()
