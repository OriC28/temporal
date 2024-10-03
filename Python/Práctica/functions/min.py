def min_function(iterable):
	are_int = []
	if type(iterable)==list:
		for i in range(len(iterable)):
			are_int.append(True) if type(iterable[i])==int else are_int.append(False)
		if all(are_int):
			min_num = iterable[0]
			for j in iterable[1:]:
				if min_num>j:
					min_num = j
			return min_num

print(min_function((2,4,5,7)))