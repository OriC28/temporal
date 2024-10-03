
def zeroes_to_end(numbers):
	j = 0
	array_temp = []
	for i in range(1, len(numbers)):
		temp = numbers[i]
		j = i-1

		while(j>=0 and temp<numbers[j]):
			numbers[j+1] = numbers[j]
			j-=1

		numbers[j+1] = temp

	for k in range(len(numbers)):
		if len(numbers) != numbers.count(0):
			while(numbers[0]==0):
				array_temp.append(numbers[k])
				numbers.remove(numbers[k])

	numbers += array_temp
	return numbers

print(zeroes_to_end([0,0,6]))