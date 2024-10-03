
def get_numbers(numbers):
	sumatory = []
	temp = 0
	first_result = numbers[0]*2 + 3
	sumatory.append(first_result)

	for i in numbers[1:]:
		temp = first_result + i*2 + 3
		sumatory.append(temp)
		first_result = temp

	return sumatory

print(get_numbers([1,2,3,5,6,7]))


a = "Hola como ta"

print(''.join(a.split()))