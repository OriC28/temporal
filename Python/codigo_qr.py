import qrcode

def create_qr_code(content):
	img = qrcode.make(content)
	try:
		with open("outputQR.png", "wb") as file:
			img.save(file)
		print("The QRCode has saved.")
	except Exception as e:
		print(e)

content = input("Insert a message to create a QR Code: ")

create_qr_code(content)


