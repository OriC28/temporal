import bcrypt
from connection import connection

query = "SELECT password FROM users;"
cursor = connection.cursor()
cursor.execute(query)
passwords = cursor.fetchall()
hashed =  "$2b$12$Gjiuyqa85lLOObhPs.HsXOQ4AXgWLz0YtIl.A7Y4pcJob84cB.gdK".encode("utf")
print(hashed)
password = '12345'.encode("utf-8")
print(password)


def verificar(password, hashed):
	if bcrypt.checkpw(password, hashed):
		print("Accediendo...")
	else:
		print("Incorrecto")

verificar(password, hashed)