def can_see_stage(array):
	row = len(array)
	column = len(array[0])
	k = 0
	for i in range(row):
		for j in range(column):
			if k>=column:
				break
			k = j - 1
			if array[k][j]>array[k-1][j]:
				print("Si")


can_see_stage([
	[1, 2, 3, 2, 1, 1],
	[2, 4, 4, 3, 2, 2],
	[5, 5, 5, 5, 4, 4],
	[6, 6, 7, 6, 5, 5]]
)