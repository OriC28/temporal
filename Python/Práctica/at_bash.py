import string

def at_bash(text):
	new_text = ""
	letters_lower = str(string.ascii_lowercase)
	letters_upper = str(string.ascii_uppercase)
	
	first_part_lower = letters_lower[0:13]
	last_part_lower = letters_lower[13:][::-1]

	first_part_upper = letters_upper[0:13]
	last_part_upper = letters_upper[13:][::-1]

	for i in text:
		if first_part_lower.find(i)!=-1:
			new_text += last_part_lower[first_part_lower.find(i)]
		elif first_part_upper.find(i)!=-1:
			new_text += last_part_upper[first_part_upper.find(i)]
		elif last_part_lower.find(i)!=-1:
			new_text += first_part_lower[last_part_lower.find(i)]
		elif last_part_upper.find(i)!=-1:
			new_text += first_part_upper[last_part_upper.find(i)]
	
		if i not in str(string.ascii_lowercase + string.ascii_uppercase):
			new_text+=i

	return new_text


print(at_bash("Christmas is the 25th of December"))