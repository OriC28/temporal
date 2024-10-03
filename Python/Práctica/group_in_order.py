
def grouping(numbers, size):
	result = []
	quantity_arrays = round(len(numbers)/size)
	# *** ADDING SUBARRAYS
	for i in range(quantity_arrays):
		result.append([])
	# *** ADDING NUMBERS EACH SUBARRAY
	l = 0
	for i in range(len(numbers)):
		result[l].append(numbers[i])
		i += 1
		l += 1
		if l == quantity_arrays:
			l = 0
	return result

print(grouping([1,2,3,4,5,6], 3))