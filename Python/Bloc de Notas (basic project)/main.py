from tkinter import *
from customtkinter import set_appearance_mode, CTkFont, CTkTextbox
from tkinter import ttk, messagebox, filedialog
import win32api
from PIL import Image
from PIL import ImageTk
from help_window import Help
import os

class Notes:
	def __init__(self, window):
		set_appearance_mode("dark") # MODE DARK
		self.path_open = None # PATH OF FILE OPENED
		self.window = window # MAIN WINDOW
		self.window.iconbitmap("icon/logo.ico")
		self.original_size = 18 # INITIAL FONT SIZE
		self.font = CTkFont(family="Consolas", size=self.original_size)  # SET PROGRAM FONT
		self.title = window.title("Sin título: Bloc de Notas") # TITLE OF MAIN WINDOW
		self.menu = Menu(self.window) # MENU BAR
		self.text = CTkTextbox(self.window, font=self.font) # TEXT WIDGET
		self.text.pack(expand=True, fill=BOTH)
		self.create_menu()
		self.text.focus_set()
		
	def create_menu(self):
		# ******************** MAIN OPTIONS TO MENU BAR
		self.file = Menu(self.menu, tearoff=False, bg="#222222", fg="#ffffff", activeborderwidth=5)
		self.edit = Menu(self.menu, tearoff=False, bg="#222222", fg="#ffffff", activeborderwidth=5)
		self.format = Menu(self.menu, tearoff=False, bg="#222222", fg="#ffffff", activeborderwidth=5)
		self.view = Menu(self.menu, tearoff=False, bg="#222222", fg="#ffffff", activeborderwidth=5)
		self.help = Menu(self.menu, tearoff=False, bg="#222222", fg="#ffffff", activeborderwidth=5)
		
		self.menu.add_cascade(menu=self.file, label="Archivo")
		self.menu.add_cascade(menu=self.edit, label="Edición")
		self.menu.add_cascade(menu=self.format, label="Formato")
		self.menu.add_cascade(menu=self.view, label="Ver")
		self.menu.add_cascade(menu=self.help, label="Ayuda")
		# ****************** SUB OPTIONS FOR MENU BAR
		self.sub_menu_file()
		self.sub_menu_view()
		self.sub_menu_help()

	def sub_menu_file(self):
		# ***************** SUB OPTIONS IN FILE OPTION
		self.file.add_command(label="Nuevo", accelerator="Ctrl + N", command=self.new_file)
		self.file.add_command(label="Abrir...", accelerator="Ctrl + A", command=self.open_file)
		self.file.add_command(label="Guardar", accelerator="Ctrl + G", command=self.save_file)
		self.file.add_command(label="Guardar como...",command=self.save_as_file)


		self.file.add_separator() # SEPARATOR

		self.file.add_command(label="Imprimir...", command=self.print_file)
		
		self.file.add_separator() # SEPARATOR

		self.file.add_command(label="Exit", command=self.window.destroy)

		# ******************* COMBINATIONS OF KEYS (EVENTS)
		self.window.bind_all("<Control-n>", self.new_file)
		self.window.bind_all("<Control-a>", self.open_file)
		self.window.bind_all("<Control-g>", self.save_file)
		self.window.bind_all("<Control-+>", self.size_max)
		self.window.bind_all("<Control-minus>", self.size_min)
		
		self.window.configure(menu=self.menu)

	def sub_menu_view(self):
		# ******************* SUB OPTIONS IN VIEW OPTION
		self.view.add_command(label="Acercar", accelerator="Ctrl++", command=self.size_max)
		self.view.add_command(label="Alejar ", accelerator="Ctrl+-", command=self.size_min)
		
		# ******************* COMBINATIONS OF KEYS (EVENTS)
		self.window.bind_all("<Control-+>", self.size_max)
		self.window.bind_all("<Control-minus>", self.size_min)
		self.window.configure(menu=self.menu)

	def sub_menu_help(self):
		# ************* SUB OPTION IN HELP OPTION
		self.help.add_command(label="Acerca de Bloc de Notas", command=self.open_window_help)

	def open_window_help(self):
		# ************* CREATING NEW WINDOW TO HELP SECTION
		new_window = Toplevel()
		help_windwo = Help(new_window)
		new_window.mainloop()

	def size_max(self, event=None):
		self.original_size+=1
		self.text.configure(font=('Consolas', self.original_size))

	def size_min(self, event=None):
		self.original_size-=1
		self.text.configure(font=('Consolas', self.original_size))

	def new_file(self, event=None):
		self.path_open = None
		data = self.text.get("0.0","end-1c")
		if data != "":
			answer = messagebox.askyesnocancel(message="¿Quieres guardar este archivo?", title="Guardar...")
			if answer:
				directory = filedialog.asksaveasfilename(filetypes=(("Documentos de texto (*.txt)", "*.txt"),))
				if directory:
					file = open(directory, 'w', encoding='utf-8')
					file.write(data.encode('utf-8').decode())
					file.close()
					
					self.text.delete("0.0","end-1c") # ******** DELETE TEXT WROTE
			elif not answer and answer!=None:
				self.text.delete("0.0","end-1c") # ******** DELETE TEXT WROTE
				self.title = window.title("Sin título: Bloc de Notas") 

	def open_file(self, event=None):
		directory = filedialog.askopenfilename(filetypes=(
										("Documentos de texto (*.txt)", "*.txt"),))	
		if directory:
			self.text.delete("0.0","end-1c") # ******** DELETE TEXT WROTE
			file = open(directory, 'r', encoding='utf-8')
			information = file.read()
			information.encode('utf-8').decode()
			self.text.insert('end-1c', information)
			file.close()
			filename = os.path.basename(directory)[:len(os.path.basename(directory))-4]
			self.title = window.title(f"{filename}: Bloc de Notas") # *** CHANGE TITLE PROGRAM TO TITLE FILE
			self.path_open = directory

	def save_file(self, event=None):
		print(self.path_open)
		data = self.text.get("0.0","end-1c")
		if self.path_open:
			with open(self.path_open, 'w', encoding='utf-8') as file:
				file.write(data.encode('utf-8').decode())
		else:
			directory = filedialog.asksaveasfilename(filetypes=(
						("Documentos de texto (*.txt)", "*.txt"),),
						confirmoverwrite=True)
			if directory:
				with open(directory, 'w', encoding='utf-8') as file:
					file.write(data.encode('utf-8').decode())
				self.path_open = directory
				filename = os.path.basename(directory)[:len(os.path.basename(directory))-4]
				self.title = window.title(f"{filename}: Bloc de Notas") # *** CHANGE TITLE PROGRAM TO TITLE FILE

	def save_as_file(self):
		data = self.text.get("0.0","end-1c")
		directory = filedialog.asksaveasfilename(filetypes=(("Documentos de texto (*.txt)", "*.txt"),),confirmoverwrite=True)
		if directory:
			with open(directory, 'w', encoding='utf-8') as file:
				file.write(data.encode('utf-8').decode())
			self.path_open = directory
			filename = os.path.basename(directory)[:len(os.path.basename(directory))-4]
			self.title = window.title(f"{filename}: Bloc de Notas") # ***** CHANGE TITLE PROGRAM TO TITLE FILE

	def print_file(self):
		try:
			if self.path_open:
				win32api.ShellExecute(0, "print", self.path_open, None, ".", 0)
		except Exception as e:
			messagebox.showerror(message=str(e), title="Error")

# ***** FUNCTION TO CENTER MAIN WINDOW (STOLEN)
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2*frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth()//2 - win_width//2
    y = window.winfo_screenheight()//2 - win_height//2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.deiconify()

if __name__ == '__main__':
	window = Tk()
	window.geometry("900x500")
	center_window(window)
	bloc_notes = Notes(window)
	window.mainloop()