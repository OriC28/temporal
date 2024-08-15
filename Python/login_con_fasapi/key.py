from cryptography.fernet import Fernet

 # Crear clave
key = Fernet.generate_key()

# Guardando la clave generada (única)
with open("key.key", "wb") as key_file:
	key_file.write(key)

# Creando conjunto de cifrado
cipher_suite = Fernet(key) 

# Encriptando la contraseña de la base de datos
encrypted_password = cipher_suite.encrypt("Ori31525588$$.".encode("utf-8"))

# Guarda la contraseña encriptada en un archivo
with open("encrypted_password.bin", "wb") as password_file:
    password_file.write(encrypted_password)