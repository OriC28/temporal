def count_function(iterable, item):
	try:
		count = 0
		for i in iterable:
			if i == item:
				count+=1
		return count
	except Exception as e:
		return e
		
print(count_function("hola todo bien", "o"))


