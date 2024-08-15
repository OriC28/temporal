from spire.pdf.common import *
from spire.pdf import *
from PyQt6.QtWidgets import QApplication, QMessageBox, QFileDialog
from PyQt6 import uic
import os

class MainWindow:
	def __init__(self):
		self.file_path = None
		self.main = uic.loadUi("main.ui")
		self.init_gui()

		self.label = self.main.label
		self.button1 = self.main.pushButton1
		self.button2 = self.main.pushButton2
		self.message = QMessageBox()
		self.doc = PdfDocument()

	def init_gui(self):
		self.main.pushButton1.clicked.connect(self.pdf_to_docx)
		self.main.pushButton2.clicked.connect(self.convert)
		self.main.show()

	def pdf_to_docx(self):
		try:
			file_path, filter = QFileDialog.getOpenFileName(self.main, 'Open file', 
										'./files', 'PDF files (*.pdf)')
			if file_path:
				file_name = os.path.basename(file_path)
				self.doc.LoadFromFile(file_path)
				self.file_path = file_path
				self.label.setText(f"File selected: {file_name}")

			else:
				self.label.setText(f"File selected: Not selected")
				self.message.warning(self.main, "Warning", "Please, select a file and try again.",
									QMessageBox.StandardButton.Ok)

		except Exception as e:
			self.message.warning(self.main, "Error", f"Opps! An error has occurred.\n {e}",
								QMessageBox.StandardButton.Ok)
	
	def convert(self):
		name_file = os.path.basename(self.file_path)[:-4]
		self.doc.SaveToFile(f"files/{name_file}.docx", FileFormat.DOCX)
		self.doc.Close()

		self.message.information(self.main, "Success", "The file has converted successfully.",
								QMessageBox.StandardButton.Ok)

if __name__ == '__main__':
	app = QApplication([])
	window = MainWindow()
	app.exec()