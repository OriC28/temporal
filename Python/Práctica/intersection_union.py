
def intersection_union(list1, list2):
	# ADDING ITEMS THAT ARE IN BOTH LIST 
	intersection = [x for x in list1 if x in list2]
	# COMBINING BOTH LISTS 
	union = list1 + list2
	# REMOVING THE REPETITIONS INTO UNION LIST AND INTERSECTION LIST
	for i in intersection:
		for j in union:
			if intersection.count(i)>1:
				intersection.remove(i)
			elif union.count(j)>1:
				union.remove(j)
	# RETURN A LIST WITH INTERSECTION LIST AND UNION LIST EACH ONE ORDERED
	return [sorted(intersection), sorted(union)]

print(intersection_union([5, 6, 6, 6, 8, 9], [4, 5, 3, 3, 4, 5, 8]))