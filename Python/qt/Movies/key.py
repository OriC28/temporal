from cryptography.fernet import Fernet

key = Fernet.generate_key()


with open("key.key", "wb") as file:
	file.write(key)


cipher_suite = Fernet(key)

encrypted_password = cipher_suite.encrypt("Ori31525588$$.".encode("utf-8"))

with open("encrypted_password.bin", "wb") as password_file:
    password_file.write(encrypted_password)
