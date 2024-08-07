from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from data.usuario import UsuarioData
from model.usuario import Usuario
from GUI.main import MainWindow

class Login:
	def __init__(self):
		self.login = uic.loadUi("GUI/login.ui")
		self.iniciar_gui()
		self.login.lblMensaje.setText("")
		self.login.show()

	def ingresar(self):
		if len(self.login.txtUsuario.text())<2:
			self.login.lblMensaje.setText("Ingrese un usuario válido")
			self.login.txtUsuario.setFocus()
		elif len(self.login.txtClave.text())<2:
			self.login.lblMensaje.setText("Ingrese una contraseña válida")
			self.login.txtClave.setFocus()
		else:
			self.login.lblMensaje.setText("")
			usuario = Usuario(usuario=self.login.txtUsuario.text(), clave=self.login.txtClave.text())
			usuarioData = UsuarioData()
			respuesta = usuarioData.login(usuario)
			if respuesta:
				self.main = MainWindow()
				self.login.hide()
			else:
				self.login.lblMensaje.setText("Todo mal")

	def iniciar_gui(self):
		self.login.btnAcceder.clicked.connect(self.ingresar)
		