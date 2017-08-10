from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog
from PyQt5 import uic
import sys

from Ui.MCMail_main import Ui_MailMainWindow
from Ui.primera_vez import DialogoPrimeraVez
from Ui.Msge_exito import Dialogo_exito
from Ui.Msge_error import Dialogo_error

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class Aplicacion(QMainWindow, Ui_MailMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # QMainWindow.__init__(self)
        # uic.loadUi("MCMail.ui", self)
        self.setupUi(self)
        self.retranslateUi(self)

        self.mostrar_primera_vez()

        self.enviar.clicked.connect(self.enviar_mail)


    def mostrar_primera_vez(self):
        ventana_primera_vez = DialogoPrimeraVez()
        ventana_primera_vez.exec_()
        self.de.setText(ventana_primera_vez.mail.text())
        self.password = ventana_primera_vez.password.text()

    def mostrar_error(self):
        ventana_error = Dialogo_error()
        ventana_error.exec_()

    def mostrar_exito(self):
        ventana_exito = Dialogo_exito()
        ventana_exito.exec_()


    def closeEvent(self, event):
        msje = QMessageBox()
        msje.setWindowTitle("Salir")
        msje.setText("Seguro que quieres salir?")
        boton_si = msje.addButton("Si", QMessageBox.YesRole)
        boton_no = msje.addButton("No", QMessageBox.NoRole)
        msje.setDefaultButton(boton_no)
        msje.exec_()

        if msje.clickedButton() == boton_si:
            event.accept()
        else:
            event.ignore()


    def enviar_mail(self):
        msg = MIMEMultipart()
        msg["From"] = self.de.text()
        msg["to"] = self.para.text()
        msg["Subject"] = self.asunto.text()
        if self.prioridad.isChecked():
            msg['X-Priority'] = '1'

        msg.attach(MIMEText(self.mensaje.toPlainText(), "plain"))
        texto = msg.as_string()

        try:
            s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            s.ehlo()
            s.login(self.de.text(), self.password)
            s.sendmail(self.de.text(), self.para.text(), texto)

            self.mostrar_exito()
        except Exception as e:
            self.mostrar_error()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    _Ventana = Aplicacion()
    _Ventana.show()
    sys.exit(app.exec_())
