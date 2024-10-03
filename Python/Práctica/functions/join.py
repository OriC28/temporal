
def join_function(iterable, separator):
	are_str = []
	new_string = ""
	for i in iterable:
		are_str.append(True) if type(i)==str else are_str.append(False)
	if all(are_str):
		for j in range(len(iterable)):
			if j!=len(iterable)-1:
				new_string+=iterable[j] + separator
			else:
				new_string+=iterable[j]
	return new_string

print(join_function(["a","b","c",1], "#"))
