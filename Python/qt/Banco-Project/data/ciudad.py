import conexion as conn

class CiudadData:
	def listado(self):
		self.db = conn.Conexion().conectar()
		self.cursor = self.db.cursor()
		resultado = self.cursor.execute("SELECT * FROM ciudades ORDER BY Nombre_Ciudad")
		ciudades = resultado.fetchall()
		self.cursor.close()
		self.db.close()
		return ciudades