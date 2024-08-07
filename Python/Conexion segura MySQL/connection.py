import mysql.connector
from cryptography.fernet import Fernet
from key import encrypted_password

# Abrir archivo donde está la clave
with open("key.key", "rb") as key_file:
    key = key_file.read()

# Cargar la contraseña encriptada desde el archivo
with open("encrypted_password.bin", "rb") as password_file:
    encrypted_password = password_file.read()

# Desencriptar la contraseña
cipher_suite = Fernet(key)
decrypted_password = cipher_suite.decrypt(encrypted_password_).decode("utf-8")

# Realizar la conexión a MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=decrypted_password,
    database="storedb"
)

# Verificar la conexión
if connection.is_connected():
    print("Conexión exitosa a la base de datos")
else:
    print("Error en la conexión a la base de datos")

# Crear cursor
cursor = connection.cursor()

# Realizar una consulta
query = "SELECT * FROM users;"
cursor.execute(query)
result = cursor.fetchall()

# Imprimir lo datos en pantalla
print(result)


# Cerrar la conexión
connection.close()