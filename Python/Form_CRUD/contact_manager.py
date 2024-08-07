import sqlite3 as sql

class ContactManager:
	def __init__(self):
		self.connection = sql.connect("ContactsDB.db", check_same_thread=False)


	def add_contact(self, nombre, edad, email, tlf):
		query = '''
			INSERT OR REPLACE INTO datos (NOMBRE, EDAD, CORREO, TELEFONO)
			VALUES (?,?,?,?)
		'''
		self.connection.execute(query, (nombre, edad, email, tlf))
		self.connection.commit()

	def get_contacts(self):
		cursor = self.connection.cursor()
		query = '''SELECT * FROM datos'''
		cursor.execute(query)
		contacts = cursor.fetchall()
		return contacts

	def delete_contact(self, nombre):
		query = '''
			DELETE FROM datos WHERE NOMBRE = ?
		'''
		self.connection.execute(query, (nombre,))
		self.connection.commit()

	def update_contact(self, contact_id, nombre, edad, email, tlf):
		query = '''
			UPDATE datos SET NOMBRE = ?, EDAD = ?,
			CORREO = ?, TELEFONO = ? WHERE ID = ?
		'''
		self.connection.execute(query, nombre, edad, email, tlf, contact_id)
		self.connection.commit()

	def close_connection(self):
		self.connection.close()
