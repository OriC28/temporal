import mysql.connector
from cryptography.fernet import Fernet
from key import encrypted_password

with open("key.key", "rb") as key_file:
    key = key_file.read()

with open("encrypted_password.bin", "rb") as password_file:
    encrypted_password = password_file.read()

cipher_suite = Fernet(key)
dcpassword = cipher_suite.decrypt(encrypted_password).decode("utf-8")

connection = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = dcpassword,
	database = "movies_app"
)