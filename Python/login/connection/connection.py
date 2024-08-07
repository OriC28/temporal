import sqlite3 as sql

class Connection:
	def __init__(self):
		self.connection = sql.connect("db/data.db", check_same_thread=False)

	def get_data(self):
		cursor = self.connection.cursor()
		query = "SELECT * FROM users"
		cursor.execute(query)
		return cursor.fetchall()

	def add_data(self, name, password):
		query = '''
			INSERT or REPLACE INTO users (Name, Password)
			VALUES (?, ?)
		'''
		self.connection.execute(query, (name, password))
		self.connection.commit()

	def delete_data(self, name):
		query = '''
			DELETE FROM users WHERE Name = ?
		'''
		self.connection.execute(query, (name,))
		self.connection.commit()

	def update_data(self, id_user, name, password):
		query = '''
			UPDATE users SET Name = ?, Password = ? WHERE ID = ?
		'''
		self.connection.execute(query, (id_user, name, password))
		self.connection.commit()

	def close_connection(self):
		self.connection.close()
