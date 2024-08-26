
def consecutive_combo(list1, list2):
	list_result = sorted(list1 + list2)
	if list_result == [j for j in range(min(list_result), max(list_result)+1)]:
		return True
	return False
print(consecutive_combo([1,2,5,6,7,4], [3,8,9,10]))