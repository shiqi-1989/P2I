# -*- coding: UTF-8 -*-
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QAction, QMenu, QSystemTrayIcon, QMessageBox

from P2G import Ui_mainWindow, BASE_DIR
from PdfTheard import PdfThead


class MyMainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.tray_config()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        file_name, file_Type = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                           "All Files (*);;PDF Files (*.pdf)")
        self.lineEdit_3.setText(file_name)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        file_name, file_Type = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                           "All Files (*);;PDF Files (*.pdf)")
        self.lineEdit_7.setText(file_name)

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        directory = QFileDialog.getExistingDirectory(self,
                                                     "选取文件夹",
                                                     "./")
        self.lineEdit_4.setText(directory)

    # png 转 pdf op 2
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        file_name = self.lineEdit_4.text()
        op = 2
        if file_name == '':
            self.call_back('请选择文件')
            return
        self.pushButton_5.setText("转换中...")
        self.pushButton_5.setEnabled(False)
        self.thread = PdfThead(op, file_name, self.pushButton_5)
        self.thread.signal.connect(self.call_back)
        self.thread.start()  # 启动线程

    # pdf 转 png op 1
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        file_name = self.lineEdit_3.text()
        home_page = ''
        back_page = ''
        op = 1
        if file_name == '':
            self.call_back('请选择文件')
            return
        if self.radioButton_3.isChecked():
            home_page = self.lineEdit.text()
            back_page = self.lineEdit_2.text()
            if home_page == '0' or back_page == '0':
                self.call_back('请输入正整数')
                return
            elif not self.is_number(home_page) or not self.is_number(back_page):
                self.call_back('请输入正整数')
                return
        self.pushButton_7.setText("转换中...")
        self.pushButton_7.setEnabled(False)
        self.thread = PdfThead(op, file_name, home_page, back_page, self.pushButton_7)
        self.thread.signal.connect(self.call_back)
        self.thread.start()  # 启动线程

    # pdf 拆分 op 3
    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        file_name = self.lineEdit_7.text()
        op = 3
        if file_name == '':
            self.call_back('请选择文件')
            return
        elif self.radioButton.isChecked():
            av_num = self.lineEdit_5.text()
            print("平均拆分")
            if not self.is_number(av_num):
                self.call_back('正确输入：空（单页拆分）或正整数（平均拆分为N份）')
                return
            self.pushButton_8.setText("拆分中...")
            self.pushButton_8.setEnabled(False)
            mode = 0
            print(op, file_name, mode, av_num, self.pushButton_8)
            self.thread = PdfThead(op, file_name, mode, av_num, self.pushButton_8)
            self.thread.signal.connect(self.call_back)
            self.thread.start()  # 启动线程
        elif self.radioButton_2.isChecked():
            cus_num = self.lineEdit_6.text()
            print(cus_num)
            if cus_num == '':
                self.call_back('缺少参数')
                return
            self.pushButton_8.setText("拆分中...")
            self.pushButton_8.setEnabled(False)
            mode = 1
            self.thread = PdfThead(op, file_name, mode, cus_num, self.pushButton_8)
            self.thread.signal.connect(self.call_back)
            self.thread.start()  # 启动线程
        else:
            self.call_back('请选择拆分方式')
            return

    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        self.textBrowser.setText('')

    def call_back(self, msg):
        self.textBrowser.append(msg)

    @staticmethod
    def is_number(num):
        if num:
            try:
                a = int(num)
                if a > 0:
                    return True
            except ValueError:
                pass

            return False
        else:
            return True

    # # 重写 关闭事件
    def closeEvent(self, event):
        reply = QMessageBox(QMessageBox.Question, self.tr("提示"),
                            self.tr("确定退出程序\n 还是最小化到系统托盘？"), QMessageBox.NoButton,
                            self)
        yr_btn = reply.addButton(self.tr("是的我要退出"), QMessageBox.YesRole)
        reply.addButton(self.tr("最小化到托盘"), QMessageBox.NoRole)
        reply.exec_()
        if reply.clickedButton() == yr_btn:
            event.accept()
            self.quit()
            # QApplication.quit()
            # sys.exit(app.exec_())
        else:
            event.ignore()
            # 最小化到托盘
            self.showMinimized()
            self.setWindowFlags(Qt.SplashScreen)

    # 托盘配置
    def tray_config(self):
        self.openAction = QAction("打开", self)
        self.openAction.triggered.connect(self.showNormal)
        self.quitAction = QAction("退出", self)
        self.quitAction.triggered.connect(self.quit)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.setWindowFlag(Qt.FramelessWindowHint)
        self.trayIconMenu.setAttribute(Qt.WA_TranslucentBackground)
        self.trayIconMenu.setStyleSheet('border-radius: 4px;')
        self.trayIconMenu.addAction(self.openAction)
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)
        # self.trayIcon.setIcon(self.icon)
        self.trayIcon.setIcon(QIcon(f"{BASE_DIR / 'logo48.png'}"))
        self.trayIcon.setToolTip("PDFTools")
        self.trayIcon.show()
        self.trayIcon.activated.connect(self.act)

    # 系统托盘左键单机或者双击 显示/隐藏 UI
    def act(self, reason):
        if reason == 3:
            if self.isHidden():
                self.activateWindow()
                self.setWindowFlags(Qt.Window)
                self.show()
            else:
                self.hide()

    # 退出
    def quit(self):
        QApplication.quit()
