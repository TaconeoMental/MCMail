# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\msge_error.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Msge_error(object):
    def setupUi(self, Msge_error):
        Msge_error.setObjectName("Msge_error")
        Msge_error.resize(242, 81)
        Msge_error.setMinimumSize(QtCore.QSize(242, 81))
        Msge_error.setMaximumSize(QtCore.QSize(242, 81))
        Msge_error.setSizeGripEnabled(False)
        self.aceptar = QtWidgets.QPushButton(Msge_error)
        self.aceptar.setGeometry(QtCore.QRect(120, 50, 75, 23))
        self.aceptar.setObjectName("aceptar")
        self.msge = QtWidgets.QPlainTextEdit(Msge_error)
        self.msge.setGeometry(QtCore.QRect(20, 0, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.msge.setFont(font)
        self.msge.setAutoFillBackground(False)
        self.msge.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.msge.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.msge.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.msge.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.msge.setReadOnly(True)
        self.msge.setBackgroundVisible(False)
        self.msge.setCenterOnScroll(False)
        self.msge.setObjectName("msge")
        self.retry = QtWidgets.QPushButton(Msge_error)
        self.retry.setGeometry(QtCore.QRect(40, 50, 75, 23))
        self.retry.setAutoDefault(False)
        self.retry.setDefault(True)
        self.retry.setObjectName("retry")

        self.retranslateUi(Msge_error)
        QtCore.QMetaObject.connectSlotsByName(Msge_error)

    def retranslateUi(self, Msge_error):
        _translate = QtCore.QCoreApplication.translate
        Msge_error.setWindowTitle(_translate("Msge_error", "Error"))
        Msge_error.setWhatsThis(_translate("Msge_error", "<html><head/><body><p>Ha ocurrido un error en el envío del mensaje. Esto se puede deber a múltiples razones tales como mala conexión a internet o un error por mi parte en el código :\'v</p></body></html>"))
        self.aceptar.setText(_translate("Msge_error", "Aceptar"))
        self.msge.setPlainText(_translate("Msge_error", "No se ha podido enviar el \n"
"            mensaje"))
        self.retry.setText(_translate("Msge_error", "Reintentar"))

