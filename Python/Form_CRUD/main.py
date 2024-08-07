import flet as ft
from fpdf import FPDF
import pandas as pd
import datetime
from contact_manager import ContactManager

class PDF(FPDF):
	def header(self):
		self.set_font("Arial", "B", 12)
		self.cell(0, 10, "Tabla de datos", 0, 1, "C")

	def footer(self):
		self.set_y(-15)
		self.set_font("Arial", "I", 8)
		self.cell(0, 10, "Página {}".format(self.page_no()), 0, 0, "C")

class Form(ft.UserControl):
	def __init__(self, page):
		super().__init__(expand=True)
		self.page = page
		self.selected_row = None
		self.data = ContactManager()

		self.nombre = ft.TextField(label="Nombre", border_color="purple")
		self.edad = ft.TextField(label="Edad", border_color="purple",
								input_filter=ft.NumbersOnlyInputFilter(),
								max_length=2)
		self.email = ft.TextField(label="Correo", border_color="purple")
		self.tlf = ft.TextField(label="Teléfono ", border_color="purple",
								input_filter=ft.NumbersOnlyInputFilter(),
								max_length=11,)
		self.search_field = ft.TextField(label="Buscar por nombre",
										suffix_icon=ft.icons.SEARCH,
										border=ft.InputBorder.UNDERLINE,
										label_style=ft.TextStyle(color="white"),
										on_change = self.search_data)
		self.data_table = ft.DataTable(
				expand=True,
				border = ft.border.all(2, "purple"),
				data_row_color = {ft.MaterialState.SELECTED: "purple",
								ft.MaterialState.PRESSED: "black"},
				border_radius = 10,
				show_checkbox_column = True,

				columns=[
					ft.DataColumn(ft.Text("Nombre", color="purple", weight="bold")),
					ft.DataColumn(ft.Text("Edad", color="purple", weight="bold"), numeric=True),
					ft.DataColumn(ft.Text("Correo", color="purple", weight="bold")),
					ft.DataColumn(ft.Text("Teléfono", color="purple", weight="bold"), numeric=True)
				]
			)

		self.show_data()

		self.form = ft.Container(
			bgcolor = "#222222",
			border_radius = 10,
			padding = 10,
			col = 4,
			content=ft.Column(
				alignment = ft.MainAxisAlignment.SPACE_AROUND,
				horizontal_alignment = ft.CrossAxisAlignment.CENTER,
				controls=[
					ft.Text("Ingrese sus datos", size=40,
							text_align="center", font_family="vivaldi",),
					self.nombre,
					self.edad,
					self.email,
					self.tlf,
					ft.Container(
						content = ft.Row(
							spacing = 5,
							alignment = ft.MainAxisAlignment.CENTER,
							controls=[
								ft.TextButton(text="Guardar",
											icon = ft.icons.SAVE,
											style=ft.ButtonStyle(
											color="white",
											bgcolor = "purple"),
											on_click=self.add_data),
								ft.TextButton(text="Actualizar",
											icon = ft.icons.UPDATE,
											style=ft.ButtonStyle(
											color="white",
											bgcolor = "purple"),
											on_click = self.update_data),
								ft.TextButton(text="Borrar",
											icon = ft.icons.DELETE,
											style=ft.ButtonStyle(
											color="white",
											bgcolor = "purple"),
											on_click=self.delete_data),
							]
						)
					)
				]
			)
		)

		self.table = ft.Container(
			bgcolor = "#222222",
			border_radius = 10,
			col = 8,
			content = ft.Column(
				controls=[
						ft.Row(
							controls=[
								self.search_field,
								ft.IconButton(
									tooltip="Editar",
									icon=ft.icons.EDIT,
									icon_color="white",
									on_click = self.select_filed_text),
								ft.IconButton(
									tooltip="Descargar PDF",
									icon=ft.icons.PICTURE_AS_PDF,
									icon_color="white",
									on_click=self.export_pdf),
								ft.IconButton(
									tooltip="Descargar Excel",
									icon=ft.icons.SAVE_ALT,
									icon_color="white",
									on_click=self.export_excel)

							]
						),
						ft.Container(
						ft.Column(
							expand=True,
							scroll="auto",
							controls=[
								ft.ResponsiveRow([
									self.data_table
								])
							]
						),
						padding = 15
					)
				]
			)
		)

		self.cont = ft.ResponsiveRow(
				controls=[self.form, self.table]
			)

	def export_pdf(self, e):
		pdf = PDF()
		pdf.add_page()
		column_widths = [10, 40, 20, 80, 40]
		data = self.data.get_contacts()
		header = ("ID", "NOMBRE", "EDAD", "CORREO", "TELEFONO")
		data.insert(0, header)
		for row in data:
			for item, width in zip(row, column_widths):
				pdf.cell(width, 10, str(item), border=1)
			pdf.ln()

		file_name = datetime.datetime.now()
		file_name = file_name.strftime("DATA %Y-%m-%d_%H-%M-%S") + ".pdf"
		pdf.output(file_name)

	def export_excel(self, e):
		data = self.data.get_contacts()
		file_name = datetime.datetime.now()
		file_name = file_name.strftime("DATA %Y-%m-%d_%H-%M-%S") + ".xlsx"
		df = pd.DataFrame(data, columns=["ID", "NOMBRE", "EDAD", "CORREO", "TELEFONO"])
		df.to_excel(file_name, index=False)

	def clean_fields(self):
		self.nombre.value = ""
		self.edad.value = ""
		self.email.value = ""
		self.tlf.value = ""

	def get_index(self, e):
		if e.control.selected:
			e.control.selected = False
		else:
			e.control.selected = True
		
		nombre = e.control.cells[0].content.value
		for row in self.data.get_contacts():
			if row[1] == nombre:
				self.selected_row = row
				break
		self.update()

	def select_filed_text(self, e):
		try:
			self.nombre.value = self.selected_row[1]
			self.edad.value = self.selected_row[2]
			self.email.value = self.selected_row[3]
			self.tlf.value = self.selected_row[4]
			self.update()
		except TypeError:
			print("Error")

	def update_data(self, e):
		contact_id = self.selected_row[0]
		nombre = self.nombre.value
		edad = str(self.edad.value)
		email = self.email.value
		tlf = str(self.tlf.value)

		if len(nombre) and len(edad) and len(email) and len(tlf)>0:
			self.clean_fields(contact_id, nombre, edad, email, tlf)
			self.show_data()

	def add_data(self, e):
		nombre = self.nombre.value
		edad = str(self.edad.value)
		email = self.email.value
		tlf = str(self.tlf.value)

		if len(nombre) and len(edad) and len(email) and len(tlf)>0:
			contact_existe = False
			for row in self.data.get_contacts():
				if row[1] == nombre:
					contacts_existe = True
					break
				if not contact_existe:
					self.clean_fields()
					self.data.add_contact(nombre, edad, email, tlf)
					self.show_data()

	def delete_data(self, e):
		try:
			self.data.delete_contact(self.selected_row[1])
			self.show_data()
		except TypeError:
			print("Error, seleccione el dato a eliminar")

	def search_data(self, e):
		name_search = self.search_field.value.lower()
		nombres = list(filter(lambda x: name_search in x[1].lower(), self.data.get_contacts()))
		self.data_table.rows = []
		if not self.search_field.value == "":
			if len(nombres)>0:
				for x in nombres:
					self.data_table.rows.append(
						ft.DataRow(
							on_select_changed = self.get_index,
							cells=[
								ft.DataCell(ft.Text(x[1])),
								ft.DataCell(ft.Text(str(x[2]))),
								ft.DataCell(ft.Text(x[3])),
								ft.DataCell(ft.Text(str(x[4])))
							]
						)
					)

					self.update()
		else:
			self.show_data()

	def show_data(self):
		self.data_table.rows = []
		for x in self.data.get_contacts():
			self.data_table.rows.append(
				ft.DataRow(
					on_select_changed = self.get_index,
					cells=[
						ft.DataCell(ft.Text(x[1])),
						ft.DataCell(ft.Text(str(x[2]))),
						ft.DataCell(ft.Text(x[3])),
						ft.DataCell(ft.Text(str(x[4])))
					]
				)
			)
		self.update()

	def build(self):
		return self.cont


def main(page: ft.Page):
	page.bgcolor = "black"
	page.title = "CRUD Sqlite3"
	page.window.min_height = 500
	page.window_min_width = 1100 

	page.add(Form(page))


ft.app(main)