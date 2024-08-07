from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QFileDialog
from PyQt6 import uic, QtGui
import qrcode

class Application:
	def __init__(self):
		self.main = uic.loadUi("main.ui")
		self.init_gui()

		self.content = self.main.lineEdit
		self.button = self.main.pushButton
		self.message = QMessageBox()

		imagen = QtGui.QPixmap("./icon/qr-code.png")
		self.main.logo.setPixmap(imagen)

	def init_gui(self):
		self.main.pushButton.clicked.connect(self.show_dialog)
		self.main.show()

	def create_qr_code(self):
		if not self.content.text() == '':
			img = qrcode.make(self.content.text())
			try:
				file_name, filter = QFileDialog.getSaveFileName(self.main, 'Save file', 
									'./QR Codes', 'Image files (*.png)')
				with open(file_name, "wb") as file:
					img.save(file)
				self.message.information(self.main, "Information", "The QRCode has saved.",
										QMessageBox.StandardButton.Ok)
			except Exception as e:
				self.message.warning(self.main, "Warning", f"{e}",
										QMessageBox.StandardButton.Ok)
		else:
			self.message.warning(self.main, "Warning", f"The field is empty, please insert a message.",
										QMessageBox.StandardButton.Ok)
			self.content.setFocus()

	def show_dialog(self):
		option : bool
		answer = self.message.question(self.main, "Question", "Are you sure to save this QR Code?",
					QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Cancel)
		option = True if answer == 2048 else False
		
		if option:
			self.create_qr_code()
			return
		
if __name__ == '__main__':
	app = QApplication([])
	window = Application()
	app.exec()
