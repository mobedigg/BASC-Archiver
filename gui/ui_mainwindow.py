# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Dec 11 07:42:00 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 468)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.threadList = QtGui.QListView(self.centralWidget)
        self.threadList.setObjectName("threadList")
        self.verticalLayout_2.addWidget(self.threadList)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.threadUrl = QtGui.QLineEdit(self.centralWidget)
        self.threadUrl.setObjectName("threadUrl")
        self.horizontalLayout.addWidget(self.threadUrl)
        self.addThread = QtGui.QToolButton(self.centralWidget)
        self.addThread.setObjectName("addThread")
        self.horizontalLayout.addWidget(self.addThread)
        self.addFromClipboard = QtGui.QToolButton(self.centralWidget)
        self.addFromClipboard.setObjectName("addFromClipboard")
        self.horizontalLayout.addWidget(self.addFromClipboard)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.settingsBox = QtGui.QGroupBox(self.centralWidget)
        self.settingsBox.setObjectName("settingsBox")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.settingsBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.downloadImages = QtGui.QCheckBox(self.settingsBox)
        self.downloadImages.setObjectName("downloadImages")
        self.verticalLayout_5.addWidget(self.downloadImages)
        self.downloadThumbs = QtGui.QCheckBox(self.settingsBox)
        self.downloadThumbs.setObjectName("downloadThumbs")
        self.verticalLayout_5.addWidget(self.downloadThumbs)
        self.saveWarc = QtGui.QCheckBox(self.settingsBox)
        self.saveWarc.setObjectName("saveWarc")
        self.verticalLayout_5.addWidget(self.saveWarc)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.followChildren = QtGui.QCheckBox(self.settingsBox)
        self.followChildren.setObjectName("followChildren")
        self.verticalLayout_6.addWidget(self.followChildren)
        self.followExternalBoards = QtGui.QCheckBox(self.settingsBox)
        self.followExternalBoards.setObjectName("followExternalBoards")
        self.verticalLayout_6.addWidget(self.followExternalBoards)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout_2.addWidget(self.settingsBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkMinutes = QtGui.QSpinBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkMinutes.sizePolicy().hasHeightForWidth())
        self.checkMinutes.setSizePolicy(sizePolicy)
        self.checkMinutes.setProperty("value", 1)
        self.checkMinutes.setObjectName("checkMinutes")
        self.verticalLayout_3.addWidget(self.checkMinutes)
        self.singleDownload = QtGui.QCheckBox(self.centralWidget)
        self.singleDownload.setObjectName("singleDownload")
        self.verticalLayout_3.addWidget(self.singleDownload)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar()
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 724, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionFd = QtGui.QAction(MainWindow)
        self.actionFd.setObjectName("actionFd")
        self.actionAdf = QtGui.QAction(MainWindow)
        self.actionAdf.setObjectName("actionAdf")
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.threadUrl.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Thread URL", None, QtGui.QApplication.UnicodeUTF8))
        self.addThread.setText(QtGui.QApplication.translate("MainWindow", "Add Thread", None, QtGui.QApplication.UnicodeUTF8))
        self.addFromClipboard.setText(QtGui.QApplication.translate("MainWindow", "Add From Clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsBox.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadImages.setText(QtGui.QApplication.translate("MainWindow", "Download Images", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadThumbs.setText(QtGui.QApplication.translate("MainWindow", "Download Thumbnails", None, QtGui.QApplication.UnicodeUTF8))
        self.saveWarc.setText(QtGui.QApplication.translate("MainWindow", "Save WARC Files (recommended)", None, QtGui.QApplication.UnicodeUTF8))
        self.followChildren.setText(QtGui.QApplication.translate("MainWindow", "Follow Child Threads", None, QtGui.QApplication.UnicodeUTF8))
        self.followExternalBoards.setText(QtGui.QApplication.translate("MainWindow", "Follow to other boards", None, QtGui.QApplication.UnicodeUTF8))
        self.checkMinutes.setSuffix(QtGui.QApplication.translate("MainWindow", " minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.checkMinutes.setPrefix(QtGui.QApplication.translate("MainWindow", "Check every ", None, QtGui.QApplication.UnicodeUTF8))
        self.singleDownload.setText(QtGui.QApplication.translate("MainWindow", "Don\'t watch (one time download)", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFd.setText(QtGui.QApplication.translate("MainWindow", "fd", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdf.setText(QtGui.QApplication.translate("MainWindow", "adf", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

