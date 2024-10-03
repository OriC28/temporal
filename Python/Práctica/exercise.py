
def invert_num(num):
	temp = ""
	str_num = str(int(num%10)) + str(int((num/10)%10)) + str(int((num/10)/10))
	if len(str_num) != len(str(num)):
		for i in range(len(str(num))):
			temp+=str_num[i]
		new_num = num - int(temp)
	else:
		new_num = num - int(str_num)

	return new_num if (new_num>0) else 0

print(invert_num(665))



