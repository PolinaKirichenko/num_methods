# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(937, 550)
        MainWindow.setWindowTitle(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 169, 26))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 360, 68, 29))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_res = QtGui.QLabel(self.centralwidget)
        self.label_res.setGeometry(QtCore.QRect(30, 400, 411, 101))
        self.label_res.setMinimumSize(QtCore.QSize(411, 101))
        self.label_res.setObjectName(_fromUtf8("label_res"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 310, 85, 27))
        self.pushButton.setMaximumSize(QtCore.QSize(91, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.widget_plot = QtGui.QWidget(self.centralwidget)
        self.widget_plot.setGeometry(QtCore.QRect(450, 110, 471, 421))
        self.widget_plot.setObjectName(_fromUtf8("widget_plot"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(9, 78, 381, 221))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(148, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 2)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_a = QtGui.QLineEdit(self.widget)
        self.lineEdit_a.setObjectName(_fromUtf8("lineEdit_a"))
        self.gridLayout.addWidget(self.lineEdit_a, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.lineEdit_z = QtGui.QLineEdit(self.widget)
        self.lineEdit_z.setObjectName(_fromUtf8("lineEdit_z"))
        self.gridLayout.addWidget(self.lineEdit_z, 1, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_b = QtGui.QLineEdit(self.widget)
        self.lineEdit_b.setObjectName(_fromUtf8("lineEdit_b"))
        self.gridLayout.addWidget(self.lineEdit_b, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.lineEdit_s = QtGui.QLineEdit(self.widget)
        self.lineEdit_s.setObjectName(_fromUtf8("lineEdit_s"))
        self.gridLayout.addWidget(self.lineEdit_s, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.lineEdit_x0 = QtGui.QLineEdit(self.widget)
        self.lineEdit_x0.setObjectName(_fromUtf8("lineEdit_x0"))
        self.horizontalLayout.addWidget(self.lineEdit_x0)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout.addWidget(self.label_9)
        self.lineEdit_y0 = QtGui.QLineEdit(self.widget)
        self.lineEdit_y0.setObjectName(_fromUtf8("lineEdit_y0"))
        self.horizontalLayout.addWidget(self.lineEdit_y0)
        self.label_14 = QtGui.QLabel(self.widget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout.addWidget(self.label_14)
        self.lineEdit_T = QtGui.QLineEdit(self.widget)
        self.lineEdit_T.setObjectName(_fromUtf8("lineEdit_T"))
        self.horizontalLayout.addWidget(self.lineEdit_T)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(48, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.radioButton_man = QtGui.QRadioButton(self.widget)
        self.radioButton_man.setObjectName(_fromUtf8("radioButton_man"))
        self.gridLayout_2.addWidget(self.radioButton_man, 0, 2, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 4, 1, 1)
        self.radioButton_auto = QtGui.QRadioButton(self.widget)
        self.radioButton_auto.setObjectName(_fromUtf8("radioButton_auto"))
        self.gridLayout_2.addWidget(self.radioButton_auto, 0, 5, 1, 1)
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEdit_beta_from = QtGui.QLineEdit(self.widget)
        self.lineEdit_beta_from.setObjectName(_fromUtf8("lineEdit_beta_from"))
        self.gridLayout_2.addWidget(self.lineEdit_beta_from, 1, 1, 1, 2)
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 1, 3, 1, 1)
        self.lineEdit_beta_to = QtGui.QLineEdit(self.widget)
        self.lineEdit_beta_to.setObjectName(_fromUtf8("lineEdit_beta_to"))
        self.gridLayout_2.addWidget(self.lineEdit_beta_to, 1, 4, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label_2.raise_()
        self.label.raise_()
        self.lineEdit_b.raise_()
        self.label_5.raise_()
        self.lineEdit_y0.raise_()
        self.lineEdit_T.raise_()
        self.label_14.raise_()
        self.label_res.raise_()
        self.pushButton.raise_()
        self.widget_plot.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Input parameters</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Result</span></p></body></html>", None))
        self.label_res.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Solve", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">ρ(w) = aw(b - w)</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">a =</span></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">z(t) =</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">b =</span></p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">S(t) =</span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">X</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:12pt; font-weight:600;\"> =</span></p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Y</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">0 </span><span style=\" font-size:12pt; font-weight:600;\">=</span></p></body></html>", None))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">T</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\"/><span style=\" font-size:12pt; font-weight:600;\">=</span></p></body></html>", None))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Mode</span></p></body></html>", None))
        self.radioButton_man.setText(_translate("MainWindow", "Manual", None))
        self.radioButton_auto.setText(_translate("MainWindow", "Automatic", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">β:  from</span></p></body></html>", None))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">to</span></p></body></html>", None))

