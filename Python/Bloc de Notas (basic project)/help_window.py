from tkinter import *
from customtkinter import set_appearance_mode
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

class Help:
	def __init__(self, window):
		# ********** CONFIG WINDOW 'HELP'
		self.window = window
		self.window.config(bg="#222222")
		self.window.geometry("600x200")
		self.window.title("Acerca de Bloc de Notas")
		self.window.resizable(0,0)
		self.window.iconbitmap("icon/logo.ico")

		# ********* IMAGE LOGO
		image = Image.open("images/logo_help.png")
		image = image.resize((70,70), Image.LANCZOS)
		self.photo = ImageTk.PhotoImage(image)
		label_img = Label(self.window, image=self.photo, bg="#222222")
		label_img.place(relx=0.1, rely=0.05)

		# ********* TITLE LABEL 
		label_title = Label(self.window, text="BLOC DE NOTAS", bg="#222222", fg="#fff")
		label_title.config(font=("Consolas", 30, 'bold'))
		label_title.place(relx=0.3, rely=0.1)

		# ********* SEPARATOR
		separator = Frame(self.window, bg="gray", height=1, bd=0)
		separator.pack(fill=X, pady=95)
		
		text = Label(self.window, text="Versión 1.0\nCopyright © 2024 Oriana Colina. Reservados todos los derechos.",
					bg="#222222",  fg="#fff")
		text.configure(font=("Consolas", 12))
		text.place(relx=0.035, rely=0.55)

