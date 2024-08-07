import sqlite3 as sql

class Conexion:
	def __init__(self):
		try:
			self.conn = sql.connect("banco.db")
			self.crear_tablas()
		except Exception as e:
			print(e)

	def crear_tablas(self):
		query_tabla1 = """CREATE TABLE IF NOT EXISTS usuarios (ID INTEGER PRIMARY KEY AUTOINCREMENT,
														Nombre TEXT, Usuario TEXT UNIQUE, Clave TEXT)"""
		cursor = self.conn.cursor()
		cursor.execute(query_tabla1)
		cursor.close()
		
	def conectar(self):
		return self.conn
