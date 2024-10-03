from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QFileDialog, QTableWidgetItem
from PyQt6 import uic, QtGui, QtCore
from PyQt6.QtCore import pyqtSignal, QUrl, Qt
from movies_genres import movie_genres
from db_process import DB
import re

class App_Movie:
	def __init__(self):
		self.message = QMessageBox()
		self.main = uic.loadUi("main.ui")
		self.row_selected = []
		self.row_double_clicked = []
		self.init_gui()
		
	def init_gui(self):
		self.rate = uic.loadUi("rate.ui")
		self.search = uic.loadUi("search.ui")
		self.main.cb_genres.addItems(movie_genres)
		self.show_movies()
		self.main.btn_save.clicked.connect(self.add_movies_field)
		self.main.btn_rate.clicked.connect(self.open_rate_window)
		self.rate.btn_rate_movie_seen.clicked.connect(self.rate_movie)
		self.main.table.cellDoubleClicked.connect(self.edit_movie_selected)
		self.main.btn_edit.clicked.connect(self.edit_movie)
		self.main.btn_search.clicked.connect(self.open_search_window)
		self.search.btn_search_filter.clicked.connect(self.search_movie)
		self.search.cb_fields.currentIndexChanged.connect(self.get_label)
		self.main.btn_delete.clicked.connect(self.delete_movie)
		self.main.move(160, 0)
		self.main.show()

	def open_rate_window(self):
		self.rate.rate_entry.setText("")
		self.item_selected()
		if self.row_selected:
			title = self.row_selected[1]
			self.rate.label_movie.setText(title)
			self.rate.show()
		else:
			self.message.warning(self.main, "Warning", "Error. Please select a movie to continue.",
								QMessageBox.StandardButton.Ok)

	def open_search_window(self):
		self.main.lower()
		self.get_label()
		self.search.show()

	def get_label(self):
		field = self.search.cb_fields.currentText()
		self.search.label_to_search.setText(f"Enter the {field} you want to search for")

	def search_movie(self):
		field = self.search.cb_fields.currentText()
		data_search = self.search.search_filter.text()
		query = ""
		try:
			if data_search!="":
				if field == "Title" and re.search(r"\D+", data_search):
					query = "SELECT * FROM movies WHERE title_movie = %s"
				elif field == "Year" and re.search(r"^\d{4}$", data_search):
					query = "SELECT * FROM movies WHERE year_movie = %s"
				elif field == "Director" and not re.search(r"\d+", data_search):
					query = "SELECT * FROM movies WHERE director_movie = %s"
				elif field == "Genre" and not re.search(r"\d+", data_search):
					query = "SELECT * FROM movies WHERE genre_movie = %s"
				elif field == "Status" and not re.search(r"\d+", data_search) and data_search == "Seen" or data_search == "To see":
					query = "SELECT * FROM movies WHERE status_movie = %s"
				elif field == "Rate" and re.search(r"^\d+$", data_search):
					if float(data_search)>=0 and float(data_search)<=10:
						query = "SELECT * FROM movies WHERE rating_movie = %s"
				
				self.show_filter_data(query, data_search)
			else:
				self.message.warning(self.search, "Warning", "Error. Please fill in the field.",
								QMessageBox.StandardButton.Ok)

		except Exception as e:
			self.message.warning(self.search, "Warning", f"Error. {e}.",
								QMessageBox.StandardButton.Ok)

	def show_filter_data(self, query, data_search):
		data = DB().search_movie_to_db(query, data_search)
		if data is None:
			return
		self.search.table_filter.setRowCount(len(data))
		row = 0
		for i in range(len(data)):

			self.search.table_filter.setItem(row, 0, QTableWidgetItem(data[i][0]))
			self.search.table_filter.setItem(row, 1, QTableWidgetItem(data[i][1]))
			self.search.table_filter.setItem(row, 2, QTableWidgetItem(str(data[i][2])))
			self.search.table_filter.setItem(row, 3, QTableWidgetItem(data[i][3]))
			self.search.table_filter.setItem(row, 4, QTableWidgetItem(data[i][4]))
			self.search.table_filter.setItem(row, 5, QTableWidgetItem(data[i][5]))
			self.search.table_filter.setItem(row, 6, QTableWidgetItem(str(data[i][6])))

			QTableWidgetItem(data[i][0]).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			QTableWidgetItem(data[i][1]).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			QTableWidgetItem(str(data[i][2])).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			QTableWidgetItem(data[i][3]).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			QTableWidgetItem(data[i][4]).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			QTableWidgetItem(data[i][5]).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			QTableWidgetItem(str(data[i][6])).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			row+=1

	def item_selected(self):
		row = self.main.table.currentRow()
		row_selected = []
		for i in range(6):
			if self.main.table.item(row, i):
				row_selected.append(self.main.table.item(row, i).text())
		self.row_selected = row_selected

	def edit_movie(self):
		if self.main.table.item(self.main.table.currentRow(),0):
			id_movie = self.main.table.item(self.main.table.currentRow(),0).text()
			title = self.main.title_entry.text()
			year = self.main.year_entry.text()
			director = self.main.director_entry.text()
			genre = self.main.cb_genres.currentText()
			status = self.main.cb_status.currentText()
			
			index_genre = self.main.cb_genres.findText(genre, Qt.MatchFlag.MatchExactly)
			index_status = self.main.cb_status.findText(status, Qt.MatchFlag.MatchExactly)

			if re.search(r"\D+", title) and re.search(r"^\d{4}$", year) and not re.search(r"\d+", director) and index_status!=0 and index_genre!=0:
					DB().edit_movie_in_db(id_movie, title, year, genre, status, director)
					self.clean_fields()
					self.show_movies()
			else:
				self.message.warning(self.rate, "Warning", "Error. Please enter valid data for the movie.",
									QMessageBox.StandardButton.Ok)
		else:
			self.message.warning(self.rate, "Warning", "Please double-click on a row to select it and edit its items.",
									QMessageBox.StandardButton.Ok)

	def delete_movie(self):
		if self.main.table.item(self.main.table.currentRow(),0):
			id_movie = self.main.table.item(self.main.table.currentRow(),0).text()
			DB().remove_movie(id_movie)
			self.main.table.removeRow(self.main.table.currentRow())
		else:
			self.message.warning(self.rate, "Warning", "Please, select a movie to delete.",
									QMessageBox.StandardButton.Ok)

	def edit_movie_selected(self, row, column):
		row_double_clicked = []
		for i in range(6):
			if self.main.table.item(row, i):
				row_double_clicked.append(self.main.table.item(row, i).text())

		self.main.title_entry.setText(row_double_clicked[1])
		self.main.year_entry.setText(row_double_clicked[2])
		self.main.director_entry.setText(row_double_clicked[3])
		self.main.cb_genres.setCurrentIndex(movie_genres.index(row_double_clicked[4])+1)
		index_status = self.main.cb_status.findText(row_double_clicked[5], Qt.MatchFlag.MatchExactly)
		self.main.cb_status.setCurrentIndex(index_status)

	def rate_movie(self):
		rate = self.rate.rate_entry.text()
		title = self.row_selected[1]

		if rate!="" and self.row_selected[5]=="Seen":
			rate = float(self.rate.rate_entry.text())
			if rate>=0 and rate<=10:
				DB().add_rate(title, rate)
				self.rate.rate_entry.setText("")
				self.message.information(self.rate, "Success", "Success. You have rated your movie!",
									QMessageBox.StandardButton.Ok)
				self.show_movies()
		else:
			self.message.warning(self.rate, "Warning", "Please, check the fields or select a movie that you seen.",
								QMessageBox.StandardButton.Ok)
			self.rate.rate_entry.setFocus()
	
	def clean_fields(self):
		self.main.title_entry.setText("")
		self.main.year_entry.setText("")
		self.main.director_entry.setText("")
		self.main.cb_genres.setCurrentIndex(0)
		self.main.cb_status.setCurrentIndex(0)

	def add_movies_field(self):
		title = self.main.title_entry.text()
		year = self.main.year_entry.text()
		director = self.main.director_entry.text()
		genre = self.main.cb_genres.currentText()
		status = self.main.cb_status.currentText()

		index_genre = self.main.cb_genres.findText(genre, Qt.MatchFlag.MatchExactly)
		index_status = self.main.cb_status.findText(status, Qt.MatchFlag.MatchExactly)

		if re.search(r"\D+", title) and re.search(r"^\d{4}$", year) and not re.search(r"\d+", director) and index_status!=0 and index_genre!=0:
			pass
			DB().insert_movie(title, year, genre, status, None, director)
			self.clean_fields()
			self.message.information(self.main, "Success", "The movie has been added successfully.",
								QMessageBox.StandardButton.Ok)
			self.show_movies()
		else:
			self.message.warning(self.main, "Warning", "Invalid data, please check the fields.",
								QMessageBox.StandardButton.Ok)
		self.main.title_entry.setFocus()

	def show_movies(self):
		movies = DB().get_movies()
		self.main.table.setRowCount(len(movies))
		row = 0
		for i in range(len(movies)):
			id_item = QTableWidgetItem(movies[i][0])
			title_item = QTableWidgetItem(movies[i][1])
			year_item = QTableWidgetItem(str(movies[i][2]))
			director_item = QTableWidgetItem(movies[i][3])
			genre_item = QTableWidgetItem(movies[i][4])
			status_item = QTableWidgetItem(movies[i][5])
			rate_item = QTableWidgetItem(str(movies[i][6]))

			id_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			title_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			year_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			director_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			genre_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			rate_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)


			self.main.table.setItem(row, 0, id_item)
			self.main.table.setItem(row, 1, title_item)
			self.main.table.setItem(row, 2, year_item)
			self.main.table.setItem(row, 3, director_item)
			self.main.table.setItem(row, 4, genre_item)
			self.main.table.setItem(row, 5, status_item)
			self.main.table.setItem(row, 6, rate_item)
			row+=1
def main():
	app_object = QApplication([])
	app = App_Movie()
	app_object.exec()

if __name__ == '__main__':
	main()