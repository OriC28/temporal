
def reversed_function(iterable):
	list_reversed = []
	j = 0
	for i in range(len(iterable)):
		j = j - 1
		list_reversed.append(iterable[j])
	return list_reversed
	
print(reversed_function([1,2,3,4,5,8,9,6]))
