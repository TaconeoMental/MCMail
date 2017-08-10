# -*- coding: utf-8 -*-

# Archivo setup para utilizarse con el módulo cx_freeze para crear un ejecutable de esta aplicación

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ["sys", "atexit", "PyQt5.QtWidgets", "PyQt5.QtCore", "PyQt5.QtGui", "email.mime.multipart", "email.mime.text", "smtplib"]
    }
}

executables = [
    Executable('mcmail.pyw', base=base)
]

setup(name='Mcmail.pyw',
      version='0.1',
      description='MC Mail',
      options=options,
      executables=executables
      )