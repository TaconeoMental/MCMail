from PyQt5.QtWidgets import QDialog
from Ui.conf import *
import smtplib

class DialogoPrimeraVez(QDialog, Ui_primera_vez):
    def __init__(self):
        QDialog.__init__(self)

        self.setupUi(self)
        self.retranslateUi(self)

        self.aceptar.clicked.connect(self.aceptarClicked)

    def aceptarClicked(self):

        email = self.mail.text()
        # TODO: Añadir validación de dirección de correo
        passwrd = self.password.text()

        servidor = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        servidor.ehlo()

        try:
            servidor.login(email, passwrd)
            servidor.close()
            self.close()
        except Exception:
            self.msje_error.setText("La dirección de correo o la contraseña no son válidos")
            # self.mail.clear()
            self.password.clear()


    def closeEvent(self, event):
        if self.mail.text().split() != []: 
            event.accept()
        else:
            event.ignore()
