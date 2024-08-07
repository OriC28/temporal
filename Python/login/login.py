import flet as ft
from connection.connection import Connection
from cryptography.fernet import Fernet

class Login(ft.Container):
	def __init__(self, page):
		self.page = page
		self.conn = Connection()
		self.text = ft.Text("Welcome to login", size=30, weight=ft.FontWeight.BOLD)
		self.name = ft.TextField(label="Name", border_color="white")
		self.password = ft.TextField(label="Password",  border_color="white", password=True, can_reveal_password=True)
		self.button = ft.TextButton(text="Submit", style=ft.ButtonStyle(color="white", bgcolor = "blue",
									padding=15), on_click=self.register_user)
		self.recover_user = ft.TextButton(text="Have you forgotten your password?",
							style=ft.ButtonStyle(color="blue"))
		self.appbar = ft.AppBar(leading=ft.Container(
							ft.Image(src="icons/logo.png", width=100, height=100, tooltip="VibeHub"),
							on_click=lambda e: print("Returning to the beginning")),
			leading_width=40,
			color="white",
			title=ft.Text("VibeHub", size=20, weight=ft.FontWeight.BOLD),
			center_title=False,
			bgcolor="#040403",
			actions=[
				ft.IconButton(ft.icons.SUPERVISED_USER_CIRCLE),
				ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
				ft.PopupMenuButton(
					items=[
						ft.PopupMenuItem(text="Help"),
						ft.PopupMenuItem(),  # divider
						ft.PopupMenuItem(
							text="Support"),
					]
				),
			],
		)
		self.page.add(self.appbar)
		super().__init__(
			bgcolor="#040403",
			padding=10,
			margin=3,
			border_radius=10,
			border=ft.border.all(3, ft.colors.WHITE),
			width=320,
			height=510,
			content=ft.Column(
				alignment=ft.MainAxisAlignment.CENTER,
				controls=[
					ft.Text("Welcome to login", size=30, weight=ft.FontWeight.BOLD), 
					self.name, self.password, self.recover_user,
					ft.Container(ft.Row(
									alignment = ft.MainAxisAlignment.CENTER,
									controls=[self.button])
								)
						]	)
					)

	def register_user(self, e):
		key = Fernet.generate_key()
		f = Fernet(key)
		name = self.name.value
		password = str(self.password.value)
		password_crypt = f.encrypt(password.encode("utf-8"))
		user_exists = False
		users = self.conn.get_data()
		if len(name) and len(password)>0:
			for user in users:
				if user[1] == name:
					user_exists = True
					dlg_error = ft.AlertDialog(title=ft.Text("This user already registered."),
											actions_alignment=ft.MainAxisAlignment.CENTER)
					self.page.open(dlg_error)
					break 
			if not user_exists:
				self.conn.add_data(name, password_crypt)
				dlg_succes = ft.AlertDialog(title=ft.Text("Successful registration."),
											actions_alignment=ft.MainAxisAlignment.CENTER)
				self.page.open(dlg_succes)
		else:
			dlg_required = ft.AlertDialog(title=ft.Text("The fields are required."),
										actions_alignment=ft.MainAxisAlignment.CENTER)
			self.page.open(dlg_required)
		self.update()

def main(page: ft.Page):
	page.title = "VibeHub"
	page.bgcolor="#040403"
	page.vertical_alignment=ft.MainAxisAlignment.CENTER
	page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
	page.window_width=360        
	page.window_height=670       
	page.window_resizable=False
	login = Login(page)
	page.add(login)


ft.app(target=main, assets_dir="assets")