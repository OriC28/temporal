from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QFileDialog
from PyQt6 import uic, QtGui
from PyQt6.QtCore import pyqtSignal, QUrl

from threading import Thread
from pygame import mixer
import pygame
import time
import os

class App:
	def __init__(self):
		self.main = uic.loadUi("main.ui")
		self.songs = []
		self.status = True
		self.is_paused = False
		self.dir_path = None
		self.dir_song = None
		self.item = None
		self.message = QMessageBox()
		self.init_components()
		mixer.init()

	def init_components(self):
		self.main.volume_slider.setValue(50)
		self.main.volume_slider.setMaximum(100)
		self.main.label_volume.setText("50%")
		self.main.volume_slider.valueChanged.connect(self.set_volume)

		self.main.btn_select_directory.clicked.connect(self.select_directory)
		self.main.btn_select_directory.setToolTip("Select directory")

		self.main.list_songs.itemDoubleClicked.connect(self.show_item)

		self.main.btn_back.clicked.connect(self.back_button)
		self.main.btn_back.setToolTip("Back")

		self.main.btn_next.clicked.connect(self.next_button)
		self.main.btn_next.setToolTip("Next")

		self.main.btn_play.clicked.connect(self.pause_avent)
		self.main.btn_play.setToolTip("Play")

		self.main.show()

	def set_volume(self, volume):
		mixer.music.set_volume(volume*0.01)
		self.main.volume_slider.setValue(volume)
		self.main.volume_slider.setToolTip(str(volume))
		self.main.label_volume.setText(str(volume) + "%")
		if volume>0 and volume<=65:
			self.main.btn_volume.setIcon(QtGui.QIcon("icons/volume-1.svg"))
		elif volume>65 and volume<=100:
			self.main.btn_volume.setIcon(QtGui.QIcon("icons/volume-2.svg"))
		elif volume == 0:
			self.main.btn_volume.setIcon(QtGui.QIcon("icons/volume-x.svg"))

	def select_directory(self):
		try:
			dir_path = QFileDialog.getExistingDirectory(parent=self.main, caption="Select directory",
														directory=os.path.expanduser('~'),
														options=QFileDialog.Option.DontUseNativeDialog)
			if dir_path!='':
				self.status = False
				self.main.list_songs.clear()
				self.dir_path = dir_path

				self.songs = [i for i in os.listdir(dir_path) if i.endswith(".mp3")]
				self.main.list_songs.addItems(self.songs)
			
		except Exception as e:
			print(e)

	def play_thread(self):
		thread = Thread(target=self.play, args=(), daemon=True)
		thread.start()

	def show_item(self, item):
		self.item = item.text()
		dir_song = os.path.join(self.dir_path + f"/{self.item}")
		self.dir_song = dir_song
		self.play_thread()

	def back_button(self):
		index_song = self.main.list_songs.row(self.main.list_songs.currentItem())
		index_back_song = index_song - 1
		if index_back_song>=0:
			self.main.list_songs.setCurrentRow(index_back_song)
			dir_back_song = os.path.join(self.dir_path + f"/{self.songs[index_back_song]}")
			self.dir_song = dir_back_song
			mixer.music.stop()
			self.play_thread()

	def next_button(self):
		try:
			index_song = self.main.list_songs.row(self.main.list_songs.currentItem())
			end_song_index = self.main.list_songs.count() - 1
			if index_song<end_song_index:
				index_next_song = index_song + 1
			else:
				index_next_song = 0
			
			self.main.list_songs.setCurrentRow(index_next_song)
			dir_next_song = os.path.join(self.dir_path + f"/{self.songs[index_next_song]}")
			self.dir_song = dir_next_song
			mixer.music.stop()
			self.play_thread()
		except:
			pass

	def play(self):
		self.status = True
		try:
			mixer.music.load(self.dir_song)
			mixer.music.play()

			while True:
				if not self.status:
					mixer.music.stop()
					break
				if self.is_paused:
					mixer.music.pause()
					while self.is_paused and self.status:
						time.sleep(0.1)
				else:
					self.main.btn_play.setIcon(QtGui.QIcon('icons/pause.svg'))
					self.main.btn_play.setToolTip("Pause")
					mixer.music.unpause()
					time.sleep(0.1)
	
		except Exception as e:
			print(e)

	def pause_avent(self):
		if not mixer.music.get_busy():  
			self.status = True
			self.is_paused = False
			self.main.btn_play.setIcon(QtGui.QIcon('icons/pause.svg'))
			self.main.btn_play.setToolTip("Pause")
		else:
			self.is_paused = not self.is_paused
			if self.is_paused:
				self.main.btn_play.setIcon(QtGui.QIcon('icons/play.svg'))
				self.main.btn_play.setToolTip("Play")
			else:
				self.main.btn_play.setIcon(QtGui.QIcon('icons/pause.svg'))
				self.main.btn_play.setToolTip("Pause")
				time.sleep(0.1)

	def stop_play(self):
		self.status = False
		mixer.music.stop()


if __name__ == '__main__':
	app_objet = QApplication([])
	app = App()
	app_objet.exec()