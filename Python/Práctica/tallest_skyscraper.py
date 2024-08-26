
a = [
	[0, 1, 0],
	[0, 1, 1],
	[0, 1, 1],
]

def tallest_skycraper(array):
	count = 0
	k = 0
	j = 0
	data = []
	col = len(array[0])-1
	row = len(array)-1
	while(1):
		if array[j][k] == 1:
			count+=1
		if j == row:
			data.append(count)
			count=0
			j = 0
			k+=1
		else:
			j+=1
		if j==row and k==col:
			if array[j][k] == 1:
				count+=1
				data.append(count)
			break
	return max(data)

print(tallest_skycraper(a))