from PyQt5.QtWidgets import QDialog
from Ui.exito import *

class Dialogo_exito(QDialog, Ui_Msge_exito):
    def __init__(self):
        QDialog.__init__(self)

        self.setupUi(self)
        self.retranslateUi(self)

        self.aceptar.clicked.connect(self.aceptarClicked)

    def aceptarClicked(self):
        self.close()
