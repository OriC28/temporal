
def map_function(function, iterable):
	result = []
	for i in iterable:
		result.append(function(i))
	return result

print(map_function(lambda x: x + "-puta", ["a","b","c"]))