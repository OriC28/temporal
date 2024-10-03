
def split_function(string, separator):
	result = []
	count = 0
	j = 0
	for i in range(len(string)):
		if string[i] == separator:
			result.append(string[j:i])
			j = i + 1
			count+=1
			if count==string.count(separator):
				result.append(string[i+1:])
		
	return result

print(split_function("135-358-001-3156-000", "-"))