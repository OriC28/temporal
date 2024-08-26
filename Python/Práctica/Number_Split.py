
def number_split(num):
	numbs = []
	if num % 2 == 0:
		numbs = [int(num/2), int(num/2)]
	else:
		numbs = [int(num/2), int(num/2) + 1] if (num>0) else [int(num/2) - 1, int(num/2)]
	return numbs


def number_split_mini(num):
	numbs = [int(num/2), int(num/2)] if (num % 2 == 0) else [int(num/2), int(num/2) + 1] if (num>0) else [int(num/2) - 1, int(num/2)]
	print(numbs)

number_split_mini(38)