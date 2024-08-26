import re

value = "12 // 0"

def arithmetic_operation(value):
	if re.findall(r'\d\s[+*-]\s\d', value) or re.findall(r'\d\s//\s\d', value):
		data = value.split(" ")
		if '+' in value:
			return int(data[0]) + int(data[-1])
		elif '-' in value:
			return int(data[0]) - int(data[-1])
		elif '*' in value:
			return int(data[0])*int(data[-1])
		elif '//' in value:
			if int(data[-1]) == 0:
				return -1
			return int(data[0])//int(data[-1])
	else:
		return 0

print(arithmetic_operation(value))