def sum_function(iterable):
	are_int = []
	if type(iterable)==list or type(iterable)==tuple:
		for i in iterable:
			are_int.append(True) if type(i)==int else are_int.append(False)
		if all(are_int):
			sumatory = 0
			for j in iterable:
				sumatory+=j
			return sumatory

print(sum_function([1,2,4,5,65,1]))


