
def make_box(num):
	box = []
	v = ""
	spaces = ""
	for i in range(num):
		v+="#"
	box.append(v)
	temp = v
	v = ""
	for i in range(num-2):
		spaces+=" "

	for i in range(num-2):
		v = "#" + spaces + "#"
		box.append(v)
	box.append(temp)

	for c in box:
		print(c)

make_box(4)