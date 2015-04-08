# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\PycharmProjects\Checker\Checker.ui'
#
# Created: Tue Apr 07 17:31:59 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setEnabled(True)
        Dialog.resize(676, 527)
        Dialog.setMinimumSize(QtCore.QSize(676, 527))
        Dialog.setMaximumSize(QtCore.QSize(676, 527))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./picture/favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(3.0)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 220, 651, 301))
        self.textBrowser.setStyleSheet(_fromUtf8("background:url(./picture/MainForm.jpg)"))
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 651, 171))
        self.tabWidget.setStyleSheet(_fromUtf8("background:url(./picture/banner.png) no-repeat"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.check = QtGui.QPushButton(self.tab)
        self.check.setGeometry(QtCore.QRect(450, 20, 75, 23))
        self.check.setObjectName(_fromUtf8("check"))
        self.splitter_4 = QtGui.QSplitter(self.tab)
        self.splitter_4.setGeometry(QtCore.QRect(20, 20, 291, 23))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.label_5 = QtGui.QLabel(self.splitter_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_4 = QtGui.QLineEdit(self.splitter_4)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.file_2 = QtGui.QPushButton(self.splitter_4)
        self.file_2.setObjectName(_fromUtf8("file_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.pick = QtGui.QPushButton(self.tab_2)
        self.pick.setGeometry(QtCore.QRect(450, 20, 75, 23))
        self.pick.setObjectName(_fromUtf8("pick"))
        self.splitter_2 = QtGui.QSplitter(self.tab_2)
        self.splitter_2.setGeometry(QtCore.QRect(20, 60, 301, 23))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_3 = QtGui.QLabel(self.splitter_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.splitter_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.desfile = QtGui.QPushButton(self.splitter_2)
        self.desfile.setObjectName(_fromUtf8("desfile"))
        self.splitter_3 = QtGui.QSplitter(self.tab_2)
        self.splitter_3.setGeometry(QtCore.QRect(20, 100, 301, 23))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_4 = QtGui.QLabel(self.splitter_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_3 = QtGui.QLineEdit(self.splitter_3)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.excelfile = QtGui.QPushButton(self.splitter_3)
        self.excelfile.setObjectName(_fromUtf8("excelfile"))
        self.splitter = QtGui.QSplitter(self.tab_2)
        self.splitter.setGeometry(QtCore.QRect(20, 20, 301, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.splitter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.file = QtGui.QPushButton(self.splitter)
        self.file.setObjectName(_fromUtf8("file"))
        self.copy = QtGui.QRadioButton(self.tab_2)
        self.copy.setGeometry(QtCore.QRect(350, 40, 51, 21))
        self.copy.setChecked(True)
        self.copy.setObjectName(_fromUtf8("copy"))
        self.buttonGroup = QtGui.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.copy)
        self.move = QtGui.QRadioButton(self.tab_2)
        self.move.setGeometry(QtCore.QRect(350, 80, 51, 21))
        self.move.setObjectName(_fromUtf8("move"))
        self.buttonGroup.addButton(self.move)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(460, 10, 191, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "韩都衣舍活动管理图片筛选器", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "检测结果", None))
        self.check.setText(_translate("Dialog", "检测图片", None))
        self.label_5.setText(_translate("Dialog", "文件目录", None))
        self.lineEdit_4.setText(_translate("Dialog", "请选择图片目录", None))
        self.file_2.setText(_translate("Dialog", "选择文件夹", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "检测图片", None))
        self.pick.setText(_translate("Dialog", "图片挑选", None))
        self.label_3.setText(_translate("Dialog", "文件目录", None))
        self.lineEdit_2.setText(_translate("Dialog", "请选择保存文件夹", None))
        self.desfile.setText(_translate("Dialog", "选择文件夹", None))
        self.label_4.setText(_translate("Dialog", "选择Excel", None))
        self.lineEdit_3.setText(_translate("Dialog", "请选择货号文件夹", None))
        self.excelfile.setText(_translate("Dialog", "选择文件", None))
        self.label.setText(_translate("Dialog", "文件目录", None))
        self.lineEdit.setText(_translate("Dialog", "请选择图片文件夹", None))
        self.file.setText(_translate("Dialog", "选择文件夹", None))
        self.copy.setText(_translate("Dialog", "复制", None))
        self.move.setText(_translate("Dialog", "移动", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "挑选图片", None))
        self.label_6.setText(_translate("Dialog", "Gana项目组制作 ，请给红心哈 ^_^！", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

