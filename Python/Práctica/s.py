import string

def determine(word):
	phrase = string.ascii_lowercase
	print(phrase)
	phrase_indexes = 0
	word = word.lower().strip()

	r1 = phrase.find(word[0]) - phrase.find(word[-1])
	
	for i in word:
		if i not in phrase and i!=" ":
			return 0

	for i in range(1, len(word)-1):
		if phrase.find(word[i])!=-1:
			phrase_indexes+=phrase.find(word[i])
	return (r1 + phrase_indexes)*word.count(" ")*2  if word.count(" ")*2>=1 else r1 + phrase_indexes

print(determine("hola que tal"))






