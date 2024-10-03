
def len_function(iterable):
	count = 0
	try:
		for i in iterable:
			count+=1
		return count
	except Exception as e:
		return e

print(len_function((True, False, False)))