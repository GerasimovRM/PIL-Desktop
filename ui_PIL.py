# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PIL.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PILDesktop(object):
    def setupUi(self, PILDesktop):
        PILDesktop.setObjectName("PILDesktop")
        PILDesktop.resize(900, 600)
        PILDesktop.setMinimumSize(QtCore.QSize(800, 500))
        PILDesktop.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(PILDesktop)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_left = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left.setObjectName("pushButton_left")
        self.horizontalLayout.addWidget(self.pushButton_left)
        self.pushButton_right = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_right.setObjectName("pushButton_right")
        self.horizontalLayout.addWidget(self.pushButton_right)
        self.pushButton_zoom_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_zoom_minus.setObjectName("pushButton_zoom_minus")
        self.horizontalLayout.addWidget(self.pushButton_zoom_minus)
        self.pushButton_zoom_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_zoom_plus.setObjectName("pushButton_zoom_plus")
        self.horizontalLayout.addWidget(self.pushButton_zoom_plus)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(124)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.horizontalLayout_7.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_change_parameters = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_change_parameters.setObjectName("pushButton_change_parameters")
        self.verticalLayout.addWidget(self.pushButton_change_parameters)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)
        self.pushButton_save_as = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_as.setObjectName("pushButton_save_as")
        self.verticalLayout.addWidget(self.pushButton_save_as)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_undo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_undo.setObjectName("pushButton_undo")
        self.horizontalLayout_3.addWidget(self.pushButton_undo)
        self.pushButton_redo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_redo.setObjectName("pushButton_redo")
        self.horizontalLayout_3.addWidget(self.pushButton_redo)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.horizontalLayout_4.addWidget(self.pushButton_reset)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        PILDesktop.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PILDesktop)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFilters = QtWidgets.QMenu(self.menubar)
        self.menuFilters.setObjectName("menuFilters")
        PILDesktop.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(PILDesktop)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew_Tab = QtWidgets.QAction(PILDesktop)
        self.actionNew_Tab.setObjectName("actionNew_Tab")
        self.actionSave = QtWidgets.QAction(PILDesktop)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(PILDesktop)
        self.actionExit.setObjectName("actionExit")
        self.actionDefault_size = QtWidgets.QAction(PILDesktop)
        self.actionDefault_size.setObjectName("actionDefault_size")
        self.actionZoom_plus = QtWidgets.QAction(PILDesktop)
        self.actionZoom_plus.setObjectName("actionZoom_plus")
        self.actionZoom_minus = QtWidgets.QAction(PILDesktop)
        self.actionZoom_minus.setObjectName("actionZoom_minus")
        self.actionHelp = QtWidgets.QAction(PILDesktop)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAdd_Filter = QtWidgets.QAction(PILDesktop)
        self.actionAdd_Filter.setObjectName("actionAdd_Filter")
        self.actionFilters_settings = QtWidgets.QAction(PILDesktop)
        self.actionFilters_settings.setObjectName("actionFilters_settings")
        self.actionSave_as = QtWidgets.QAction(PILDesktop)
        self.actionSave_as.setObjectName("actionSave_as")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionDefault_size)
        self.menuView.addAction(self.actionZoom_plus)
        self.menuView.addAction(self.actionZoom_minus)
        self.menuHelp.addAction(self.actionHelp)
        self.menuFilters.addAction(self.actionAdd_Filter)
        self.menuFilters.addAction(self.actionFilters_settings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuFilters.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(PILDesktop)
        QtCore.QMetaObject.connectSlotsByName(PILDesktop)

    def retranslateUi(self, PILDesktop):
        _translate = QtCore.QCoreApplication.translate
        PILDesktop.setWindowTitle(_translate("PILDesktop", "PIL Desktop "))
        self.pushButton_left.setText(_translate("PILDesktop", "Left"))
        self.pushButton_right.setText(_translate("PILDesktop", "Right"))
        self.pushButton_zoom_minus.setText(_translate("PILDesktop", "Zoom -"))
        self.pushButton_zoom_plus.setText(_translate("PILDesktop", "Zoom +"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PILDesktop", "Filters:"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PILDesktop", "Args:"))
        self.pushButton_change_parameters.setText(_translate("PILDesktop", "Change Parameters"))
        self.pushButton_save.setText(_translate("PILDesktop", "Save"))
        self.pushButton_save_as.setText(_translate("PILDesktop", "Save as"))
        self.pushButton_undo.setText(_translate("PILDesktop", "<-- Undo"))
        self.pushButton_redo.setText(_translate("PILDesktop", "Redo -->"))
        self.pushButton_reset.setText(_translate("PILDesktop", "Reset All"))
        self.menuFile.setTitle(_translate("PILDesktop", "File"))
        self.menuView.setTitle(_translate("PILDesktop", "View"))
        self.menuHelp.setTitle(_translate("PILDesktop", "Help"))
        self.menuFilters.setTitle(_translate("PILDesktop", "Filters"))
        self.actionOpen.setText(_translate("PILDesktop", "Open"))
        self.actionOpen.setShortcut(_translate("PILDesktop", "Ctrl+O"))
        self.actionNew_Tab.setText(_translate("PILDesktop", "New Tab"))
        self.actionSave.setText(_translate("PILDesktop", "Save"))
        self.actionSave.setShortcut(_translate("PILDesktop", "Ctrl+S"))
        self.actionExit.setText(_translate("PILDesktop", "Exit"))
        self.actionDefault_size.setText(_translate("PILDesktop", "Default size"))
        self.actionDefault_size.setShortcut(_translate("PILDesktop", "Home"))
        self.actionZoom_plus.setText(_translate("PILDesktop", "Zoom +"))
        self.actionZoom_plus.setShortcut(_translate("PILDesktop", "PgUp"))
        self.actionZoom_minus.setText(_translate("PILDesktop", "Zoom -"))
        self.actionZoom_minus.setShortcut(_translate("PILDesktop", "PgDown"))
        self.actionHelp.setText(_translate("PILDesktop", "***CLICK HERE***"))
        self.actionAdd_Filter.setText(_translate("PILDesktop", "Add Filter"))
        self.actionFilters_settings.setText(_translate("PILDesktop", "Filters settings"))
        self.actionSave_as.setText(_translate("PILDesktop", "Save as"))
        self.actionSave_as.setShortcut(_translate("PILDesktop", "F12"))
