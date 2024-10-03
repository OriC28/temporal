def zip_function(iterable1, iterable2):
	result = []
	if len(iterable1)==len(iterable2):
		for i in range(len(iterable1)):
			result.append((iterable1[i], iterable2[i]))
	return result

print(zip_function([1,2,3], ['a','b','c','d']))
