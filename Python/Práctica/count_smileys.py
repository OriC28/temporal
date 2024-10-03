import re

def count_smileys(faces):
	faces_found = 0
	for face in faces:
		if re.search("^[:;][-~]?[)D]$", face):
			faces_found+=1

	return faces_found

print(count_smileys([";D", ":-(", ";~)", ":)", ";(", ";}", ":-D"]))



