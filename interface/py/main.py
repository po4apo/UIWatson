# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ilyasu\PycharmProjects\UIWatson\interface\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WatsonUI(object):
    def setupUi(self, WatsonUI):
        WatsonUI.setObjectName("WatsonUI")
        WatsonUI.resize(533, 596)
        self.centralWidget = QtWidgets.QWidget(WatsonUI)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 181, 511))
        self.scrollArea.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 0, 331, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.mainGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.mainGridLayout.setContentsMargins(0, 0, 0, 0)
        self.mainGridLayout.setObjectName("mainGridLayout")
        self.projectControlGroupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.projectControlGroupBox.setObjectName("projectControlGroupBox")
        self.splitter_2 = QtWidgets.QSplitter(self.projectControlGroupBox)
        self.splitter_2.setGeometry(QtCore.QRect(10, 20, 111, 81))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.startProjectPushButton = QtWidgets.QPushButton(self.splitter_2)
        self.startProjectPushButton.setObjectName("startProjectPushButton")
        self.stopProjectPushButton = QtWidgets.QPushButton(self.splitter_2)
        self.stopProjectPushButton.setObjectName("stopProjectPushButton")
        self.statusProjectPushButton = QtWidgets.QPushButton(self.splitter_2)
        self.statusProjectPushButton.setObjectName("statusProjectPushButton")
        self.statusLabel = QtWidgets.QLabel(self.projectControlGroupBox)
        self.statusLabel.setGeometry(QtCore.QRect(130, 20, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel.setFont(font)
        self.statusLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.statusLabel.setObjectName("statusLabel")
        self.mainGridLayout.addWidget(self.projectControlGroupBox, 1, 0, 1, 1)
        self.tagsGroupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.tagsGroupBox.setObjectName("tagsGroupBox")
        self.splitter = QtWidgets.QSplitter(self.tagsGroupBox)
        self.splitter.setGeometry(QtCore.QRect(10, 210, 111, 53))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.addNewTagPushButton = QtWidgets.QPushButton(self.splitter)
        self.addNewTagPushButton.setObjectName("addNewTagPushButton")
        self.removeTagPushButton = QtWidgets.QPushButton(self.splitter)
        self.removeTagPushButton.setObjectName("removeTagPushButton")
        self.unselectedTagsScrollArea = QtWidgets.QScrollArea(self.tagsGroupBox)
        self.unselectedTagsScrollArea.setGeometry(QtCore.QRect(10, 20, 111, 181))
        self.unselectedTagsScrollArea.setWidgetResizable(True)
        self.unselectedTagsScrollArea.setObjectName("unselectedTagsScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 109, 179))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.unselectedTagsScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.selectedTagsScrollArea = QtWidgets.QScrollArea(self.tagsGroupBox)
        self.selectedTagsScrollArea.setGeometry(QtCore.QRect(170, 20, 111, 241))
        self.selectedTagsScrollArea.setWidgetResizable(True)
        self.selectedTagsScrollArea.setObjectName("selectedTagsScrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 109, 239))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.selectedTagsScrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.selectTagPushButton = QtWidgets.QPushButton(self.tagsGroupBox)
        self.selectTagPushButton.setGeometry(QtCore.QRect(130, 60, 23, 23))
        self.selectTagPushButton.setObjectName("selectTagPushButton")
        self.unselectTagPushButton = QtWidgets.QPushButton(self.tagsGroupBox)
        self.unselectTagPushButton.setGeometry(QtCore.QRect(130, 90, 23, 23))
        self.unselectTagPushButton.setObjectName("unselectTagPushButton")
        self.mainGridLayout.addWidget(self.tagsGroupBox, 0, 0, 1, 1)
        WatsonUI.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(WatsonUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 21))
        self.menubar.setObjectName("menubar")
        WatsonUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WatsonUI)
        self.statusbar.setObjectName("statusbar")
        WatsonUI.setStatusBar(self.statusbar)

        self.retranslateUi(WatsonUI)
        self.label.linkActivated['QString'].connect(WatsonUI.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(WatsonUI)

    def retranslateUi(self, WatsonUI):
        _translate = QtCore.QCoreApplication.translate
        WatsonUI.setWindowTitle(_translate("WatsonUI", "MainWindow"))
        self.label.setText(_translate("WatsonUI", "Projects"))
        self.pushButton.setText(_translate("WatsonUI", "PushButton"))
        self.pushButton_2.setText(_translate("WatsonUI", "PushButton"))
        self.pushButton_3.setText(_translate("WatsonUI", "PushButton"))
        self.projectControlGroupBox.setTitle(_translate("WatsonUI", "Project Name"))
        self.startProjectPushButton.setText(_translate("WatsonUI", "Start"))
        self.stopProjectPushButton.setText(_translate("WatsonUI", "Stop"))
        self.statusProjectPushButton.setText(_translate("WatsonUI", "Status"))
        self.statusLabel.setText(_translate("WatsonUI", "Status"))
        self.tagsGroupBox.setTitle(_translate("WatsonUI", "Tags"))
        self.addNewTagPushButton.setText(_translate("WatsonUI", "add"))
        self.removeTagPushButton.setText(_translate("WatsonUI", "remove"))
        self.pushButton_4.setText(_translate("WatsonUI", "PushButton"))
        self.pushButton_5.setText(_translate("WatsonUI", "PushButton"))
        self.selectTagPushButton.setText(_translate("WatsonUI", ">"))
        self.unselectTagPushButton.setText(_translate("WatsonUI", "<"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WatsonUI = QtWidgets.QMainWindow()
    ui = Ui_WatsonUI()
    ui.setupUi(WatsonUI)
    WatsonUI.show()
    sys.exit(app.exec_())
