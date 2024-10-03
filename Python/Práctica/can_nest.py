def can_nest(array1, array2):
	if array1 and array2!=0:
		return True if min(array1)>min(array2) and max(array1)<max(array2) else False
print(can_nest([1,3], [3]))