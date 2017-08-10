from PyQt5.QtWidgets import QDialog
from Ui.error import *

class Dialogo_error(QDialog, Ui_Msge_error):
    def __init__(self):
        QDialog.__init__(self)

        self.setupUi(self)
        self.retranslateUi(self)
        
        # Agregar función para evento de click en botón "reintentar"      