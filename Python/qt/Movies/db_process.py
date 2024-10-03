from connection import connection
import string
import random

class DB:
	def __init__(self):
		self.conn = connection
		self.cursor = self.conn.cursor()

	def generate_id(self):
		id_movie = []
		characters = string.ascii_uppercase + string.digits
		for i in range(12):
			id_movie.append(random.choice(characters))
		id_movie = "".join(id_movie)
		return id_movie

	def get_movies(self):
		query = "SELECT * FROM movies;"
		self.cursor.execute(query)
		movies = self.cursor.fetchall()
		self.cursor.close()
		return movies

	def insert_movie(self, title, year, genre, status, rate=None, director=None):
		id_movie = self.generate_id()
		query = '''INSERT INTO movies (id_movie, title_movie, year_movie, director_movie,
				genre_movie, status_movie, rating_movie) VALUES (%s, %s, %s, %s, %s, %s, %s)'''

		self.cursor.execute(query, (id_movie, title, year, director, genre, status, rate))
		self.conn.commit()
		self.cursor.close()

	def add_rate(self, title, rate):
		query = "UPDATE movies SET rating_movie = %s WHERE title_movie = %s;"
		self.cursor.execute(query, (rate, title))
		self.cursor.close()


	def edit_movie_in_db(self, id_passed, title, year, genre, status, director=None):
		query = '''UPDATE movies SET title_movie = %s, year_movie = %s, director_movie = %s,
					genre_movie = %s, status_movie = %s WHERE id_movie = %s;'''

		self.cursor.execute(query, (title, year, director, genre, status, id_passed))
		self.conn.commit()
		self.cursor.close()

	def remove_movie(self, id_passed):
		query = "DELETE FROM movies WHERE id_movie = %s;"
		self.cursor.execute(query, (id_passed,))
		self.conn.commit()
		self.cursor.close()

	def search_movie_to_db(self, query, data):
		if query:
			self.cursor.execute(query, (data,))
			data_output = self.cursor.fetchall()
			self.cursor.close()
			return data_output

