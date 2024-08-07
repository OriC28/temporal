import conexion as conn
from model.usuario import Usuario

class UsuarioData:
	def __init__(self):
		try:
			self.db = conn.Conexion().conectar()
			self.cursor = self.db.cursor()
			query_admin = """INSERT INTO usuarios VALUES (NULL, ?, ?, ?)"""
			self.cursor.execute(query_admin, ("Administrador", "Admin", "Admin"))
			self.db.commit()
		except Exception as e:
			print("El usuario ingresado ya se ha creado.", e)
		finally:
			self.cursor.close()
			self.db.close()

	def login(self, usuario: Usuario): 
		self.db = conn.Conexion().conectar()
		self.cursor = self.db.cursor()
		resultado = self.cursor.execute("""SELECT * FROM usuarios WHERE Usuario = ? AND Clave = ?""",
										(usuario._usuario, usuario._clave))
		fila_usuario = resultado.fetchone()
		self.cursor.close()
		self.db.close()
		if fila_usuario:
			usuario = Usuario(nombre=fila_usuario[1], usuario=fila_usuario[2])
			return usuario
		else:
			return None