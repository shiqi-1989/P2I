# -*- coding: utf-8 -*-
from pathlib import Path

# Form implementation generated from reading ui file 'P2G.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

BASE_DIR = Path(__file__).resolve().parent


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(696, 644)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{BASE_DIR / 'logo48.png'}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("QWidget{\n"
                                 "    background-color: white;\n"
                                 "    color: rgb(106, 106, 106);\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "    color: rgb(106, 106, 106);\n"
                                 "    selection-color: rgb(201, 216, 255);\n"
                                 "    height:21px;\n"
                                 "    border:1px solid rgb(158, 158, 158);\n"
                                 "    border-radius:6px;\n"
                                 "    padding:0px 3px;\n"
                                 "    }\n"
                                 "QLineEdit{\n"
                                 "    border:1px solid gray;\n"
                                 "    height:21px;\n"
                                 "    border-radius:6px;\n"
                                 "    padding:0px 3px;\n"
                                 "    background: transparent;\n"
                                 "    }\n"
                                 "QPushButton:hover{\n"
                                 "    font-weight:700;\n"
                                 "    color:white;\n"
                                 "    border-color:rgb(188, 201, 244);\n"
                                 "    background-color: rgb(111, 172, 236);\n"
                                 "    }\n"
                                 "QPushButton:pressed{\n"
                                 "    font-weight:700;\n"
                                 "    border-color:rgb(188, 201, 200);\n"
                                 "    background-color: rgb(188, 201, 200);\n"
                                 "    }\n"
                                 "QScrollBar:vertical {\n"
                                 "    width: 8px;\n"
                                 "    background:rgba(0, 0, 0, 0%);\n"
                                 "    border-radius:4px;\n"
                                 "    border:none;\n"
                                 "}\n"
                                 "QScrollBar:handle:vertical{\n"
                                 "    border-radius:4px;\n"
                                 "    width: 8px;\n"
                                 "    background:rgba(0, 0, 0, 25%);\n"
                                 "}\n"
                                 "QScrollBar:handle:vertical:hover\n"
                                 "{\n"
                                 "    width:8px;\n"
                                 "    background:rgba(0, 0, 0, 50%);\n"
                                 "    border-radius:4px;\n"
                                 "    min-height:20;\n"
                                 "}\n"
                                 "QScrollBar:add-line:vertical\n"
                                 "{\n"
                                 "    height:0px;\n"
                                 "    width:0px;\n"
                                 "    subcontrol-position:bottom;\n"
                                 "}\n"
                                 "QScrollBar:sub-line:vertical\n"
                                 "{\n"
                                 "    height:0px;\n"
                                 "    width:0px;\n"
                                 "    subcontrol-position:top;\n"
                                 "}\n"
                                 " QMenu {\n"
                                 " }\n"
                                 "\n"
                                 " QMenu::item {\n"
                                 "    \n"
                                 "    background-color: transparent;\n"
                                 "    padding:5px 45px;\n"
                                 "    border-radius:6px;\n"
                                 "    margin:0px 0px;\n"
                                 "\n"
                                 " }\n"
                                 "\n"
                                 " QMenu::item:selected {\n"
                                 "     background-color: #e8e8e8;\n"
                                 "\n"
                                 " }")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_8.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.radioButton = QtWidgets.QRadioButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.radioButton.setObjectName("radioButton")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.radioButton_2 = QtWidgets.QRadioButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.radioButton_2.setToolTip("")
        self.radioButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(400, 0))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.splitter_2, 1, 0, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label = QtWidgets.QLabel(self.splitter_3)
        self.label.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_7 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_7.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.splitter_3, 2, 0, 1, 1)
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_2 = QtWidgets.QLabel(self.splitter_4)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        self.radioButton_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.radioButton_3.setObjectName("radioButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter_4)
        self.lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter_4)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.splitter_4, 3, 0, 1, 1)
        self.splitter_5 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_5 = QtWidgets.QLabel(self.splitter_5)
        self.label_5.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.splitter_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter_5)
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.splitter_5)
        self.pushButton_5.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.splitter_5, 4, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 5, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 20))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "PDF工具"))
        self.label_3.setText(_translate("mainWindow", "PDF-- 拆分"))
        self.lineEdit_7.setPlaceholderText(_translate("mainWindow", "选择pdf文件，选择拆分方式，输入拆分公式"))
        self.pushButton_2.setText(_translate("mainWindow", "选择PDF"))
        self.pushButton_8.setText(_translate("mainWindow", "开始拆分"))
        self.radioButton.setText(_translate("mainWindow", "平均拆分"))
        self.lineEdit_5.setPlaceholderText(_translate("mainWindow", "为空则单页拆分"))
        self.radioButton_2.setText(_translate("mainWindow", "自定义拆分"))
        self.lineEdit_6.setPlaceholderText(
            _translate("mainWindow", " 需要分割的页数之间用英文逗号分开，格式为: 1,2-4,5-8,9-20"))
        self.label.setText(_translate("mainWindow", "PDF转图片"))
        self.lineEdit_3.setPlaceholderText(_translate("mainWindow", "选择pdf文件，输入起至页（不选：默认单页转换）"))
        self.pushButton.setText(_translate("mainWindow", "选择PDF"))
        self.pushButton_7.setText(_translate("mainWindow", "开始转换"))
        self.radioButton_3.setText(_translate("mainWindow", "起至页"))
        self.lineEdit.setPlaceholderText(_translate("mainWindow", "开始"))
        self.lineEdit_2.setPlaceholderText(_translate("mainWindow", "结束"))
        self.label_5.setText(_translate("mainWindow", "图片转PDF"))
        self.lineEdit_4.setPlaceholderText(_translate("mainWindow", "选择图片所在文件夹（图片以数字命名，方便排序）"))
        self.pushButton_4.setText(_translate("mainWindow", "选择图片文件夹"))
        self.pushButton_5.setText(_translate("mainWindow", "开始转换"))
        self.textBrowser.setHtml(_translate("mainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_6.setText(_translate("mainWindow", "清空"))
