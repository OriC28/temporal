import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QFrame, QMessageBox, QTableWidgetItem
from PyQt6.QtGui import QIntValidator
from main_ui import Ui_Form
from connect_database import ConnectDatabase

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		self.db = ConnectDatabase()

		self.student_id = self.ui.txt_studentID
		#self.student_id.setValidator(QIntValidator)
		self.first_name = self.ui.txt_firstName
		self.last_name = self.ui.txt_lastName
		self.email_address = self.ui.txt_emailAddress
		self.state = self.ui.cb_state
		self.city = self.ui.cb_city

		self.add_btn = self.ui.add_button
		self.update_btn = self.ui.update_button
		self.select_btn = self.ui.select_button
		self.search_btn = self.ui.search_button
		self.clear_btn = self.ui.clear_button
		self.delete_btn = self.ui.delete_button

		self.table = self.ui.table
		self.table.setSortingEnabled(False)
		self.buttons_list = self.ui.frameBotones.findChildren(QPushButton)


if __name__ == '__main__':
	app = QApplication(sys.argv)

	w = MainWindow()
	w.show()
	sys.exit(app.exec())