# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\msge_exito.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Msge_exito(object):
    def setupUi(self, Msge_exito):
        Msge_exito.setObjectName("Msge_exito")
        Msge_exito.resize(242, 81)
        self.msge = QtWidgets.QLabel(Msge_exito)
        self.msge.setGeometry(QtCore.QRect(10, 10, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.msge.setFont(font)
        self.msge.setObjectName("msge")
        self.aceptar = QtWidgets.QPushButton(Msge_exito)
        self.aceptar.setGeometry(QtCore.QRect(80, 50, 75, 23))
        self.aceptar.setObjectName("aceptar")

        self.retranslateUi(Msge_exito)
        QtCore.QMetaObject.connectSlotsByName(Msge_exito)

    def retranslateUi(self, Msge_exito):
        _translate = QtCore.QCoreApplication.translate
        Msge_exito.setWindowTitle(_translate("Msge_exito", "Mensaje enviado"))
        Msge_exito.setWhatsThis(_translate("Msge_exito", "<html><head/><body><p>El mensaje se envió de forma exitosa, ¿Acaso no lees?</p></body></html>"))
        self.msge.setText(_translate("Msge_exito", "Mensaje enviado exitosamente"))
        self.aceptar.setText(_translate("Msge_exito", "Aceptar"))

