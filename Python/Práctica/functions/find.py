def find_function(iterable, item):
	try:
		for i in range(len(iterable)):
			if iterable[i] == item:
				return i
		return -1
	except Exception as e:
		return e

print(find_function("hola mamita mamasota", "m"))