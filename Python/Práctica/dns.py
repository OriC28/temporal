import socket 

host = "8.8.8.8"

def get_domain(host):
	try:
		name, alias, addresslist = socket.gethostbyaddr(host)
		return name
	except socket.gaierror as e:
		print("Host incorrect, please check the host to search.")
	except socket.herror:
		print("Host not found, try again.")

print(f"Domain of {host}:", get_domain(host))