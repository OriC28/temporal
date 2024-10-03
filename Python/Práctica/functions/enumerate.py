 def enumerate_function(iterable):
	result = []
	for i in range(len(iterable)):
		result.append((i, iterable[i]))
	return result

for index, value in enumerate_function(["a", "b", "c", "d", "e"]):
	print(index, value)