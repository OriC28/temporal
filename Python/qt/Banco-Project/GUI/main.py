from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from data.transferencia import TransferenciaData
from data.deposito import DepositoData
from model.movimientos import Transferencia, DepositoInternacional
from data.ciudad import CiudadData

class MainWindow:
	def __init__(self):
		self.main = uic.loadUi("GUI/main.ui")
		self.iniciar_gui()
		self.main.showMaximized()

	def iniciar_gui(self):
		self.main.btnRegistrarTransferencias.triggered.connect(self.abrir_registro)
		self.main.btnReportarTransferencia.triggered.connect(self.abrir_deposito)
		self.registro = uic.loadUi("GUI/registro.ui")
		self.deposito = uic.loadUi("GUI/DBI.ui")

	def limpiar_campos(self):
		self.registro.cbTipo.setCurrentIndex(0)
		self.registro.cbMotivo.setCurrentIndex(0)
		self.registro.txtDocumento.setText("")
		self.registro.txtMonto.setText("")
		self.registro.checkDolares.setChecked(False)
		self.registro.checkInternacional.setChecked(False)
		self.registro.txtDocumento.setFocus()


	################### TRANSFERENCIAS ####################

	def abrir_registro(self):
		self.registro.btnRegistrar.clicked.connect(self.registrar_transferencia)
		self.registro.show()

	def registrar_transferencia(self):
		if self.registro.cbTipo.currentText() == "---Seleccione una opción":
			mensaje = QMessageBox()
			mensaje.setText("Debe seleccionar un tipo de documento.")
			mensaje.exec()
			self.registro.cbTipo.setFocus()

		elif len(self.registro.txtDocumento.text())<4:
			mensaje = QMessageBox()
			mensaje.setText("Debe ingresar un documento válido.")
			mensaje.exec()
			self.registro.txtDocumento.setFocus()

		elif self.registro.cbMotivo.currentText() == "---Seleccione una opción":
			mensaje = QMessageBox()
			mensaje.setText("Debe seleccionar el motivo.")
			mensaje.exec()
			self.registro.cbMotivo.setFocus()

		elif not self.registro.txtMonto.text().isnumeric():
			mensaje = QMessageBox()
			mensaje.setText("Debe ingresar un monto válido.")
			mensaje.exec()
			self.registro.txtMonto.setText("0")
			self.registro.txtMonto.setFocus()

		else:
			transferencia = Transferencia(tipo=self.registro.cbTipo.currentText(),
										documento=self.registro.txtDocumento.text(),
										motivo=self.registro.cbMotivo.currentText(),
										monto=int(self.registro.txtMonto.text()),
										dolares=self.registro.checkDolares.isChecked(),
										internacional=self.registro.checkInternacional.isChecked())

			objData = TransferenciaData()
			mensaje = QMessageBox()
			if objData.registrar(transferencia):
				mensaje.setText("Transferencia registrada.")
				self.limpiar_campos()
			else:
				mensaje.setText("Transferencia no registrada.")
			mensaje.exec()

	################### DEPÓSITO ####################

	def abrir_deposito(self):
		self.deposito.btnRegistrarDBI.clicked.connect(self.registrar_deposito)
		self.obtener_ciudades()
		self.deposito.show()

	def obtener_ciudades(self):
		data = CiudadData()
		ciudades = data.listado()
		for ciudad in ciudades:
			self.deposito.cbLugarNacimiento.addItem(ciudad[1])

	def validar_campos_obligatorios(self)->bool:
		if (not self.deposito.txtDocumento.text() or not self.deposito.txtPrimerNombre.text()
			or not self.deposito.txtPrimerApellido.text() or not self.deposito.txtMonto.text()
			or self.registro.cbTipo.currentText() == "---Seleccione una opción"
			or self.registro.cbMotivo.currentText() == "---Seleccione una opción"
			or self.registro.cbLugarNacimiento.currentText() == "---Seleccione una opción"
			or self.registro.cbSexo.currentText() == "---Seleccione"):
			return False
		else:
			return True

	def registrar_deposito(self):
		mensaje = QMessageBox()
		if not self.validar_campos_obligatorios():
			mensaje.setText("Debe llenar los campos obligatorios (*).")
			mensaje.exec()
			self.deposito.cbTipo.setFocus()
		elif self.deposito.checkCondiciones.isChecked() == False:
			mensaje.setText("Debe aceptar los términos y condiciones para continuar.")
			mensaje.exec()
			self.deposito.checkCondiciones.setFocus()
		elif not int(self.deposito.txtMonto.text())>0 or not self.deposito.txtMonto.text().isnumeric():
			mensaje.setText("El ingresado monto es inválido.")
			mensaje.exec()
			self.deposito.txtMonto.setText("0")
			self.deposito.txtMonto.setFocus()
		else:
			fecha_nacimiento = self.deposito.cbFechaNacimiento.date().toPyDate()
			deposito = DepositoInternacional(tipo=self.deposito.cbTipo.currentText(),
										documento=self.deposito.txtDocumento.text(),
										motivo=self.deposito.cbMotivo.currentText(),
										monto=int(self.deposito.txtMonto.text()),
										primer_nombre=self.deposito.txtPrimerNombre.text(),
										segundo_nombre=self.deposito.txtSegundoNombre.text(),
										primer_apellido=self.deposito.txtPrimerApellido.text(),
										segundo_apellido=self.deposito.txtSegundoApellido.text(),
										sexo=self.deposito.cbSexo.currentText(),
										fecha_nacimiento=fecha_nacimiento,
										lugar_nacimiento=self.deposito.cbLugarNacimiento.currentText(),
										dolares=True,
										internacional=True,
										terminos=self.deposito.checkCondiciones.isChecked())

			objData = DepositoData()
			mensaje = QMessageBox()
			if objData.registrar(deposito):
				mensaje.setText("Deposito registrado correctamente.")
				#self.limpiar_campos()
			else:
				mensaje.setText("El deposito no pudo ser registrado.")
			mensaje.exec()