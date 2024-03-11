# -*- coding: utf-8 -*-

import sys
from PyQt6 import QtWidgets
from SynAly import compile_main

from PyQt6 import QtCore, QtGui

class Ui_dialog(QtWidgets.QMainWindow):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(1063, 552)
        self.textEdit_Mediate = QtWidgets.QTextEdit(dialog)
        self.textEdit_Mediate.setGeometry(QtCore.QRect(30, 290, 271, 231))
        self.textEdit_Mediate.setObjectName("textEdit_Mediate")
        self.textEdit_Input = QtWidgets.QTextEdit(dialog)
        self.textEdit_Input.setGeometry(QtCore.QRect(30, 30, 271, 231))
        self.textEdit_Input.setObjectName("textEdit_Input")
        self.textEdit_Aimcode = QtWidgets.QTextEdit(dialog)
        self.textEdit_Aimcode.setGeometry(QtCore.QRect(400, 290, 271, 231))
        self.textEdit_Aimcode.setObjectName("textEdit_Aimcode")
        self.textEdit_Word = QtWidgets.QTextEdit(dialog)
        self.textEdit_Word.setGeometry(QtCore.QRect(400, 30, 271, 231))
        self.textEdit_Word.setObjectName("textEdit_word")
        self.Button_Open = QtWidgets.QPushButton(dialog)
        self.Button_Open.setGeometry(QtCore.QRect(310, 70, 81, 31))
        self.Button_Open.setObjectName("Button_Open")
        self.Button_Word = QtWidgets.QPushButton(dialog)
        self.Button_Word.setGeometry(QtCore.QRect(310, 160, 81, 31))
        self.Button_Word.setObjectName("Button_Word")
        self.Button_Mediate = QtWidgets.QPushButton(dialog)
        self.Button_Mediate.setGeometry(QtCore.QRect(310, 340, 81, 31))
        self.Button_Mediate.setObjectName("Button_Mediate")
        self.Button_Aimcode = QtWidgets.QPushButton(dialog)
        self.Button_Aimcode.setGeometry(QtCore.QRect(310, 440, 81, 31))
        self.Button_Aimcode.setObjectName("Button_Aimcode")
        self.textEdit_Syn = QtWidgets.QTextEdit(dialog)
        self.textEdit_Syn.setGeometry(QtCore.QRect(720, 30, 311, 491))
        self.textEdit_Syn.setObjectName("textEdit_Syn")
        self.Button_Syn = QtWidgets.QPushButton(dialog)
        self.Button_Syn.setGeometry(QtCore.QRect(310, 250, 81, 31))
        self.Button_Syn.setObjectName("Button_Syn")

        self.retranslateUi(dialog)
        self.Button_Word.clicked.connect(self.show_word)
        self.Button_Syn.clicked.connect(self.show_syn)
        self.Button_Mediate.clicked.connect(self.show_mediate)
        self.Button_Aimcode.clicked.connect(self.show_code)
        self.Button_Open.clicked.connect(self.open_files)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QtCore.QCoreApplication.translate("dialog", "类C编译器"))
        self.Button_Open.setText(QtCore.QCoreApplication.translate("dialog", "打开文件"))
        self.Button_Word.setText(QtCore.QCoreApplication.translate("dialog", "词法分析"))
        self.Button_Mediate.setText(QtCore.QCoreApplication.translate("dialog", "语义分析"))
        self.Button_Aimcode.setText(QtCore.QCoreApplication.translate("dialog", "目标代码"))
        self.Button_Syn.setText(QtCore.QCoreApplication.translate("dialog", "语法分析"))

    def open_files(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/')
        if filename:  # Check if a file was selected
            with open(filename, 'r',encoding='utf-8') as fname:
                data = fname.read()
            ret[0] = compile_main(filename)
            self.textEdit_Input.setPlainText(data)
            self.textEdit_Input.show()

    def show_word(self):
        if ret[0] is None:
            with open('测试结果/词法分析.txt', 'r') as f:
                data = f.read()
            self.textEdit_Word.clear()
            self.textEdit_Word.setPlainText(data)
            self.textEdit_Word.show()
        else:
            QtWidgets.QMessageBox.warning(self, "警告!", ret[0])

    def show_syn(self):
        if ret[0] is None:
            f = open(u'测试结果/语法分析.txt', 'r',encoding='utf-8')
            data = f.read()
            f.close()
            self.textEdit_Syn.clear()
            self.textEdit_Syn.setPlainText(data)
            self.textEdit_Syn.show()
        else:
            QtWidgets.QMessageBox.warning(self, "警告!", ret[0])

    def show_mediate(self):
        if ret[0] is None:
            f = open(u'测试结果/中间代码.txt', 'r',encoding='utf-8')
            data = f.read()
            f.close()
            self.textEdit_Mediate.clear()
            self.textEdit_Mediate.setPlainText(data)
            self.textEdit_Mediate.show()
        else:
            QtWidgets.QMessageBox.warning(self, "警告!", ret[0])

    def show_code(self):
        if ret[0] is None:
            f = open(u'测试结果/目标代码.txt', 'r',encoding='utf-8')
            data = f.read()
            f.close()
            self.textEdit_Aimcode.clear()
            self.textEdit_Aimcode.setPlainText(data)
            self.textEdit_Aimcode.show()
        else:
            QtWidgets.QMessageBox.warning(self, "警告!", ret[0])


if __name__ == "__main__":
    ret = [None]
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())