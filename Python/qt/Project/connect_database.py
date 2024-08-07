import mysql.connector

class ConnectDatabase:
	def __init__(self):
		self._host = 'localhost'
		self._port = 3306
		self._user = 'root'
		self._password = 'Ori31525588$$.'
		self._database = 'db_students'
		self.conn = None
		self.cursor = None

	def connect_db(self):
		self.conn = mysql.connector.connect(
			host = self._host,
			port = self._port,
			database = self._database,
			user = self._user,
			password = self._password
			)

		self.cursor = self.conn.cursor(dictionary=True)

	def add_info(self, student_id, first_name, last_name, state, city, email_address):
		
		self.connect_db()

		query = '''INSERT INTO students (studentId, first_name, last_name, state, city, emailAddress) VALUES (%s, %s, %s, %s, %s, %s);'''
		try:
			self.cursor.execute(query, (student_id, first_name, last_name, state, city, email_address))
			self.conn.commit()

		except Exception as e:
			self.conn.rollback()
			return e

		finally:
			self.conn.close()

	def update_info(self, first_name, last_name, state, city, email_address, student_id):
		self.connect_db()
		query = '''UPDATE students SET first_name = %s, last_name = %s, state = %s, city = %s, emailAddress = %s WHERE studentId = %s;'''

		try:
			self.cursor.execute(query, (first_name, last_name, state, city, email_address, student_id))
			self.conn.commit()

		except Exception as e:
			self.conn.rollback()
			return e

		finally:
			self.conn.close()

	def delete_info(self, student_id):
		self.connect_db()
		query = '''DELETE FROM students WHERE studentId = %s;'''

		try:
			self.cursor.execute(query, (student_id,))
			self.conn.commit()

		except Exception as e:
			self.conn.rollback()
			return e

		finally:
			self.conn.close()

	def search_info(self, student_id=None, first_name=None, last_name=None, state=None, city=None, email_address=None):
		self.connect_db()
		query = "SELECT * FROM students"
		conditions = []
		params = []

		if student_id:
			conditions.append("studentId LIKE %s")
			params.append(f"%{student_id}%")
		if first_name:
			conditions.append("first_name LIKE %s")
			params.append(f"%{first_name}%")
		if last_name:
			conditions.append("last_name LIKE %s")
			params.append(f"%{last_name}%")
		if state:
			conditions.append("state = %s")
			params.append(state)
		if city:
			conditions.append("city = %s")
			params.append(city)
		if email_address:
			conditions.append("emailAddress LIKE %s")
			params.append(f"%{email_address}%")

		if conditions:
			query += " WHERE " + "".join(conditions)
		try:
			self.cursor.execute(query, params)
			result = self.cursor.fetchall()
			return result

		except mysql.connector.Error as e:
			return e

		finally:
			self.conn.close()

	def get_all_states(self):
		self.connect_db()
		query = '''SELECT state FROM students GROUP BY state'''

		try:
			self.cursor.execute(query)
			result = self.cursor.fetchall()
			return result

		except Exception as e:
			return e

		finally:
			self.conn.close()

	def get_all_cities(self):
		self.connect_db()
		query = '''SELECT city FROM students GROUP BY city'''

		try:
			self.cursor.execute(query)
			result = self.cursor.fetchall()
			return result

		except Exception as e:
			return e

		finally:
			self.conn.close()

