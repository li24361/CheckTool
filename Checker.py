# -*- coding: utf-8 -*-

"""
Author:lizhihao
"""
import sys, threading, xlrd, shutil, os, time
from PyQt4 import QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature, pyqtSignal, QObject

reload(sys)
sys.setdefaultencoding("utf-8")
from PIL import Image

from Ui_Checker import Ui_Dialog


class CheckTool(QDialog, Ui_Dialog, QObject):

    printSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.printSignal.connect(self.printLog)

    @pyqtSignature("")
    def on_check_clicked(self):
        self.textBrowser.setText("")
        rootDir = self.lineEdit_4.text()
        dir = unicode(rootDir, 'utf-8')
        if os.path.exists(dir):
            #self.checkDir(dir)
            thread = threading.Thread(target=self.checkDir, args=(dir,))
            thread.start()
        else:
            print rootDir
            self.printSignal.emit(u"--------------- 亲，未找到该文件夹，请瞅瞅路径是否选对了呗！！--------------")

    @pyqtSignature("")
    def on_pick_clicked(self):
        self.textBrowser.setText("")
        excelPath = unicode(self.lineEdit_3.text(), 'utf-8')
        src = unicode(self.lineEdit.text(), 'utf-8')
        des = unicode(self.lineEdit_2.text(), 'utf-8')
        if os.path.exists(src) and os.path.exists(excelPath) and os.path.exists(des):
            # self.importExcel(excelPath, src, des)
            thread = threading.Thread(target=self.importExcel, args=(excelPath, src, des))
            thread.start()
        else:
            msg = u"---------------亲，未找到该文件夹，请瞅瞅路径是否选对了呗！！----------------"
            self.printSignal.emit(msg)

    @pyqtSignature("")
    def on_file_clicked(self):
        s = QtGui.QFileDialog.getExistingDirectory(self, u"选择文件夹", "/")
        self.lineEdit.setText(unicode(s, "utf8"))

    @pyqtSignature("")
    def on_desfile_clicked(self):
        s = QtGui.QFileDialog.getExistingDirectory(self, u"选择文件夹", "/")
        self.lineEdit_2.setText(unicode(s, "utf8"))

    @pyqtSignature("")
    def on_excelfile_clicked(self):
        s = QtGui.QFileDialog.getOpenFileName(self, u"选择文件", "/", '*.xlsx')
        self.lineEdit_3.setText(unicode(s, "utf8"))


    @pyqtSignature("")
    def on_file_2_clicked(self):
        s = QtGui.QFileDialog.getExistingDirectory(self, u"选择文件夹", "/")
        self.lineEdit_4.setText(unicode(s, "utf8"))

    def importExcel(self, excelPath, src, des):
        self.printSignal.emit(u"--------------------- 亲，图片挑选开始了！---------------------")
        data = xlrd.open_workbook(excelPath)
        table = data.sheets()[0]
        for sku in table.col_values(0):
            count = 0
            for root, dirs, files in os.walk(src):
                for d in dirs:
                    if d.find(sku.strip()) != -1:
                        srcDir = os.path.join(root, d)
                        desDir = os.path.join(des, d)
                        count += self.moveDicAndFile(srcDir, desDir)
                for f in files:
                    if f.find(sku.strip()) != -1:
                        srcFile = os.path.join(root, f)
                        desFile = os.path.join(des, f)
                        count += self.moveDicAndFile(srcFile, desFile)
            if count == 0:
                self.printSignal.emit(u"警告：未找到[%s]对应的文件或文件夹，"
                                      u"请检查选择的路径[%s]是否正确！" % (sku, src))
        self.printSignal.emit(u"--------------------- 亲，图片挑选结束了，请查看！！---------------------")
        os.startfile(des)

    def moveDicAndFile(self, src, des):
        result = 0
        if os.path.isdir(src):
            if os.path.exists(des):
                shutil.rmtree(des)
            shutil.copytree(src, des)
            msg = u"信息：文件夹[%s] -> [%s] 复制成功！！" % (src, des)
            self.printSignal.emit(msg)
            result = 1
        elif os.path.isfile(src):
            shutil.copy2(src, des)
            msg = u"信息：文件[%s] -> [%s] 复制成功！！" % (src, des)
            self.printSignal.emit(msg)
            result = 1
        # else:
        #     msg = u"大亲啊，【%s】不存在，请瞅瞅Excel中数据是否正确呗！！！" % src
        #     self.printSignal.emit(msg)
        return result

    def checkDir(self, rootDir):
        self.printSignal.emit(u"--------------------- 亲，图片检测开始了！-----------------------")
        list_dirs = os.walk(rootDir)
        for root, dirs, files in list_dirs:
            # for d in dirs:
            #     print os.path.join(root, d)
            for f in files:
                if f.endswith('.jpg') or f.endswith('.png'):
                    self.checkPic(os.path.join(root, f))
                if f.endswith('.txt'):
                    self.checkTxt(os.path.join(root, f))
        self.printSignal.emit(u"--------------------- 亲，图片检测结束了！！---------------------")

    def checkPic(self, PicPath):
        file = os.path.basename(PicPath)
        size = os.path.getsize(PicPath)
        #返回图形对象
        im = Image.open(PicPath)
        #获取图片宽高
        iw, ih = im.size

        ##1-2-3-4-像素1100*1390（≤300KB）
        if file.startswith("1") or file.startswith("2") or file.startswith("3") or file.startswith(
                "4") or file.startswith("15"):
            if size > 300 * 1024:
                msg = u"%s 文件大小为%d，超出规定大小300KB " % (PicPath, size)
                self.printSignal.emit(msg)
            if iw > 1100 or ih > 1390:
                msg = u"%s 文件像素为%d*%d，不符合规定大小1100*1390！" % (PicPath, iw, ih)
                self.printSignal.emit(msg)

        ##5-7-像素235*297 （≤30KB）
        if file.startswith("5") or file.startswith("7"):
            if size > 30 * 1024:
                msg = u"%s文件大小为%d，超出规定大小300KB " % (PicPath, size)
                self.printSignal.emit(msg)
            if iw > 235 or ih > 297:
                msg = u"%s 文件像素为%d*%d，不符合规定大小235*297！" % (PicPath, iw, ih)
                self.printSignal.emit(msg)

        ##6-像素750*10000px，≤2MB
        if file.startswith("6"):
            if size > 2 * 1024 * 1024:
                msg = u"%s 文件大小为%d，超出规定大小2MB " % (PicPath, size)
                self.printSignal.emit(msg)
            if iw > 750 or ih > 10000:
                msg = u" %s 文件像素为%d*%d，不符合规定大小750*10000！" % (PicPath, iw, ih)
                self.printSignal.emit(msg)

    def checkTxt(self, TxtPath):
        file = open(TxtPath, 'r')
        for (num, line) in enumerate(file):
            if line.find("taobao.com") != -1 or line.find("tmall.com") != -1:
                msg = u"%s 文件中第%d行包含字符串 taobao.com或者tmall.com，请检查！" % (TxtPath, num)
                self.printSignal.emit(msg)
        file.close()

    def printLog(self, msg):
        self.textBrowser.append(msg)
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ck = CheckTool()
    ck.show()
    sys.exit(app.exec_())
    

