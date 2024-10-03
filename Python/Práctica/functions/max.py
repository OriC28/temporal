def max_function(iterable):
	are_int = []
	if type(iterable)==list:
		for i in range(len(iterable)):
			are_int.append(True) if type(iterable[i])==int else are_int.append(False)
		if all(are_int):
			max_num = iterable[0]
			for j in iterable[1:]:
				if max_num<j:
					max_num = j
			return max_num

print(max_function(['3,5','6']))